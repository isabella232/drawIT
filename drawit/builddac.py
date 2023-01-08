# @file builddac.py
#
# Copyright contributors to the drawIT project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Hierarchy:
#   diagram.py - optional diagram-as-code in python, invokes draw.py 
#   colors.py - optional colors for use by diagram-as-code in python
#   draw.py - iterate diagram objects, invokes shapes.py
#   shapes.py - build ibm types, invokes types.py
#   types.py - build drawio types, invokes xml.py with tables.py
#   elements.py - build drawio objects  

from os import path
from math import isnan

from .colors import Colors
from .common import Common
from .constants import ParamAlternates, ParamClusterShapes, ParamDirections, ParamEdgeStyles
from .constants import ParamFonts, ParamNodeShapes, ParamOutFormats, ParamProviders
from .constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from .shapesdac import Shapes
from .iconsdac import Icons

DIAGRAM_NAME_DEFAULT = "diagram"
DIAGRAM_DIRECTION_DEFAULT = "LR"
DIAGRAM_ALTERNATE_DEFAULT = "WHITE"
DIAGRAM_PROVIDER_DEFAULT = "IBM"
DIAGRAM_FONTNAME_DEFAULT = "IBM Plex Sans"
DIAGRAM_FONTSIZE_DEFAULT = 14
DIAGRAM_OUTFORMAT_DEFAULT = "SVG"

CLUSTER_LABEL_DEFAULT = "Cluster"
CLUSTER_DIRECTION_DEFAULT = "LR"
CLUSTER_ALTERNATE_DEFAULT = "WHITE"
CLUSTER_PROVIDER_DEFAULT = "IBM"
CLUSTER_SHAPE_DEFAULT = "LOCATION"
CLUSTER_ICON_DEFAULT = "undefined"
CLUSTER_FONTNAME_DEFAULT = "IBM Plex Sans"
CLUSTER_FONTSIZE_DEFAULT = 14

NODE_LABEL_DEFAULT = "Node"
NODE_DIRECTION_DEFAULT = "LR"
NODE_PROVIDER_DEFAULT = "IBM"
NODE_SHAPE_DEFAULT = "NODE"
NODE_ICON_DEFAULT = "undefined"
NODE_FONTNAME_DEFAULT = "IBM Plex Sans"
NODE_FONTSIZE_DEFAULT = 14

EDGE_STYLE_DEFAULT = "solid"
EDGE_FONTNAME_DEFAULT = "IBM Plex Sans"
EDGE_FONTSIZE_DEFAULT = 12

class BuildDAC:
   common = None
   shapes = None
   #icons = None
   cloudname = ""
   diagrams = {}
   clusters = {}
   nodes = {}
   edges = {}
   tops = []
   bottoms = []

   def __init__(self, common, diagrams, clusters, nodes, edges):
      self.common = common
      self.shapes = Shapes(self.common)
      self.diagrams = diagrams
      self.clusters = clusters
      self.nodes = nodes
      self.edges = edges
      return

   def buildDiagrams(self):
      self.checkAll()

      if self.diagrams == None or self.clusters == None or self.nodes == None or self.edges == None:
         self.common.printExit()
         return

      for diagramid, attributes in self.diagrams.items():
         # Only single entry.
         self.common.printStartFile(attributes["filename"] + ".py", attributes["provider"].upper())

      self.setupAll()

      if self.diagrams == None or self.clusters == None or self.nodes == None or self.edges == None:
         self.common.printExit()
         return

      outputFolder = self.common.getOutputFolder()
      if outputFolder[-1] != '/':
         self.common.setOutputFolder(outputFolder + '/')

      clouddata = self.buildAll()

      for regionname, regionvalues in clouddata.items():
         self.shapes.buildXML(regionvalues, regionname)
         self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())
         self.shapes.resetXML()

      outputfolder = self.common.getOutputFolder()
      outputfile = self.common.getOutputFile()
      self.common.printDone(path.join(outputfolder, outputfile), self.common.getCloudType().value.upper())

      return

   def checkAll(self):
      self.diagrams = self.checkDiagrams(self.diagrams)
      self.clusters = self.checkClusters(self.clusters)
      self.nodes = self.checkNodes(self.nodes)
      self.edges = self.checkEdges(self.edges)

   def setupAll(self):
      self.addKeys()
      self.addChildren()

      if not self.common.isAlternateUser():
         self.alternateFills()

      self.addNodes()
      self.calculateNodeGeometry()
      self.calculateClusterGeometry()
      #self.printClusters()
      #self.printNodes()
      #self.printTops()
      #self.printBottoms()
      self.mergeNodes()
      self.eliminateZoneParents()

   def buildAll(self):
      nodes = []
      links = []
      values = []

      regiondata = {}

      for clusterid in self.tops:
         clusternodes, clusterlinks, clustervalues = self.buildClusters([clusterid])
         nodes += clusternodes
         links += clusterlinks
         values += clustervalues

      for edgeid, attributes in self.edges.items():
         edgenodes, edgelinks, edgevalues = self.buildEdgeShape(edgeid, attributes)
         nodes += edgenodes
         links += edgelinks
         values += edgevalues

      regiondata["Cloud"] = {'nodes': nodes, 'links': links, 'values': values}

      return regiondata

   def buildClusters(self, clusterids):
      nodes = []
      links = []
      values = []

      for clusterid in clusterids:
         attributes = self.clusters[clusterid]
         childids = attributes["children"]

         if len(childids) > 0:
            clusternodes, clusterlinks, clustervalues = self.buildClusters(childids)
            nodes += clusternodes
            links += clusterlinks
            values += clustervalues
         #else:
         clusternodes, clusterlinks, clustervalues = self.buildClusterShape(clusterid, attributes)
         nodes += clusternodes
         links += clusterlinks
         values += clustervalues

      return nodes, links, values

   def buildClusterShape(self, clusterid, attributes):
      nodes = []
      links = []
      values = []

      geometry = attributes["geometry"]
      x = geometry[0]
      y = geometry[1]
      width = geometry[2]
      height = geometry[3]

      meta = None

      shapenode = self.shapes.buildShape(clusterid, attributes, x, y, width, height, meta)
      nodes.append(shapenode)

      return nodes, links, values

   def buildEdgeShape(self, edgeid, attributes):
      nodes = []
      links = []
      values = []

      sourceid = attributes["sourceid"]
      targetid = attributes["targetid"]
      arrow = attributes["arrow"]
      label = attributes["label"]

      if arrow == "noarrow":
         edgenode = self.shapes.buildSolidLink(edgeid, label, sourceid, targetid, None)
      elif arrow == "singlearrow":
         edgenode = self.shapes.buildSingleArrow(edgeid, label, sourceid, targetid, None)
      else:  # "doublearrow"
         edgenode = self.shapes.buildDoubleArrow(edgeid, label, sourceid, targetid, None)

      links.append(edgenode)

      return nodes, links, values

   def checkDiagrams(self, diagrams):
      for diagramid, attributes in diagrams.items():
         name = attributes["name"]
         if name == "":
            name = DIAGRAM_NAME_DEFAULT
         diagrams[diagramid]["name"] = name

         filename = attributes["filename"]
         if filename == "":
            filename = name
         diagrams[diagramid]["filename"] = filename
         self.common.setOutputFile(filename + ".xml")

         direction = attributes["direction"]
         if direction == "":
            direction = DIAGRAM_DIRECTION_DEFAULT
         elif not direction.upper() in [parm.value for parm in ParamDirections]:
            self.common.printInvalidDirection(direction)
            return None
         diagrams[diagramid]["direction"] = direction

         alternate = attributes["alternate"]
         if alternate == "":
            alernate = DIAGRAM_ALTERNATE_DEFAULT
         elif not alternate.upper() in [parm.value for parm in ParamAlternates]:
            self.common.printInvalidAlternate(alternate)
            return None
         diagrams[diagramid]["alternate"] = alternate

         provider = attributes["provider"]
         if provider == "":
            provider = DIAGRAM_PROVIDER_DEFAULT
         elif not provider.upper() in [parm.value for parm in ParamProviders]:
            self.common.printInvalidProvider(provider)
            return None
         diagrams[diagramid]["provider"] = provider

         fontname = attributes["fontname"]
         if fontname == "":
            fontname = DIAGRAM_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in ParamFonts]:
            self.common.printInvalidFontName(fontname)
            return None
         diagrams[diagramid]["fontname"] = fontname

         fontsize = attributes["fontsize"]
         if fontsize == 0:
            fontsize = DIAGRAM_FONTSIZE_DEFAULT
         diagrams[diagramid]["fontsize"] = fontsize

         outformat = attributes["outformat"]
         if outformat == "":
            outformat = DIAGRAM_OUTFORMAT_DEFAULT
         elif not outformat.upper() in [parm.value for parm in ParamOutFormats]:
            self.common.printInvalidOutputFormat(outformat)
            return None
         diagrams[diagramid]["outformat"] = outformat

         if direction.upper() == "LR":
            self.common.setDirectionLR()
         elif direction.upper() == "TB":
            self.common.setDirectionTB()

         if alternate.upper() == "WHITE":
            self.common.setAlternateWhite()
         elif alternate.upper() == "LIGHT":
            self.common.setAlternateLight()
         elif alternate.upper() == "NONE":
            self.common.setAlternateNone()
         elif alternate.upper() == "USER":
            self.common.setAlternateUser()

         if provider.upper() == "ANY":
            self.common.setProviderAny()
         elif provider.upper() == "IBM":
            self.common.setProviderIBM()

      return diagrams

   def checkClusters(self, clusters):
      for clusterid, attributes in clusters.items():
         label = attributes["label"]
         if label == "":
            label = CLUSTER_LABEL_DEFAULT
         clusters[clusterid]["label"] = label

         direction = attributes["direction"]
         if direction == "":
            direction = CLUSTER_DIRECTION_DEFAULT
         elif not direction.upper() in [parm.value for parm in ParamDirections]:
            self.common.printInvalidDirection(direction)
            return None
         clusters[clusterid]["direction"] = direction

         alternate = attributes["alternate"]
         if alternate == "":
            alternate = CLUSTER_ALTERNATE_DEFAULT
         elif not alternate.upper() in [parm.value for parm in ParamAlternates]:
            self.common.printInvalidAlternate(alternate)
            return None
         clusters[clusterid]["alternate"] = alternate

         provider = attributes["provider"]
         if provider == "":
            provider = CLUSTER_PROVIDER_DEFAULT
         elif not provider.upper() in [parm.value for parm in ParamProviders]:
            self.common.printInvalidProvider(provider)
            return None
         clusters[clusterid]["provider"] = provider

         fontname = attributes["fontname"]
         if fontname == "":
            fontname = CLUSTER_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in ParamFonts]:
            self.common.printInvalidFont(fontname)
            return None
         clusters[clusterid]["fontname"] = fontname

         fontsize = attributes["fontsize"]
         if fontsize == 0:
            fontsize = CLUSTER_FONTSIZE_DEFAULT
         clusters[clusterid]["fontsize"] = fontsize

         icon = attributes["icon"]
         if icon == "":
            icon = CLUSTER_ICON_DEFAULT
         elif not self.common.validIcon(icon):
            self.common.printInvalidIcon(icon)
            return None

         pencolor = attributes["pencolor"]
         if pencolor == "":
            iconname, pencolor, iconshape = self.common.getIcon(icon)

         clusters[clusterid]["icon"] = iconname

         shape = attributes["shape"]
         if shape == "":
            if iconshape == "":
               self.clusters[clusterid]["shape"] = CLUSTER_SHAPE_DEFAULT
            else:
               self.clusters[clusterid]["shape"] = iconshape
         elif not shape.upper() in [parm.value for parm in ParamClusterShapes]:
            self.common.printInvalidClusterShape(shape)
            return None

         hexpencolor = self.checkLineColor(pencolor)
         if hexpencolor == None:
            self.common.printInvalidLineColor(pencolor)
            return None
         clusters[clusterid]["pencolor"] = hexpencolor

         hexbgcolor = "#ffffff"
         bgcolor = attributes["bgcolor"]
         if self.common.isAlternateUser() and bgcolor != "":
            hexbgcolor = self.checkFillColor(hexpencolor, bgcolor)
            if hexbgcolor == None:
               self.common.printInvalidFillColor(bgcolor)
               return None
         clusters[clusterid]["bgcolor"] = hexbgcolor

      return clusters

   def checkNodes(self, nodes):
      for nodeid, attributes in nodes.items():
         label = attributes["label"]
         if label == "":
            label = NODE_LABEL_DEFAULT
         nodes[nodeid]["label"] = label

         direction = attributes["direction"]
         if direction == "":
            direction = NODE_DIRECTION_DEFAULT
         elif not direction.upper() in [parm.value for parm in ParamDirections]:
            self.common.printInvalidDirection(direction)
            return None
         nodes[nodeid]["direction"] = direction

         fontname = attributes["fontname"]
         if fontname == "":
            fontname = NODE_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in ParamFonts]:
            self.common.printInvalidFont(fontname)
            return None
         nodes[nodeid]["fontname"] = fontname

         fontsize = attributes["fontsize"]
         if fontsize == 0:
            fontsize = NODE_FONTSIZE_DEFAULT
         nodes[nodeid]["fontsize"] = fontsize

         icon = attributes["icon"]
         if icon == "":
            icon = NODE_ICON_DEFAULT
         elif not self.common.validIcon(icon):
            self.common.printInvalidIcon(icon)
            return None

         pencolor = attributes["pencolor"]
         if pencolor == "":
            iconname, pencolor, iconshape = self.common.getIcon(icon)

         nodes[nodeid]["icon"] = iconname

         shape = attributes["shape"]
         if shape == "":
            if iconshape == "":
               nodes[nodeid]["shape"] = NODE_SHAPE_DEFAULT
            else:
               nodes[nodeid]["shape"] = iconshape
         else:
            if not shape.upper() in [parm.value for parm in ParamNodeShapes]:
               self.common.printInvalidNodeShape(shape)
               return None

         hexpencolor = self.checkLineColor(pencolor)
         if hexpencolor == None:
            self.common.printInvalidLineColor(pencolor)
            return None
         nodes[nodeid]["pencolor"] = hexpencolor

         hexbgcolor = pencolor
         bgcolor = attributes["bgcolor"]
         if bgcolor != "":
            hexbgcolor = checkFillColor(hexpencolor, bgcolor)
            if hexbgcolor == None:
               self.common.printInvalidFillColor(bgcolor)
               return None
         nodes[nodeid]["bgcolor"] = hexbgcolor

      return nodes

   def checkEdges(self, edges):
      for edgeid, attributes in edges.items():
         style = attributes["style"]
         if style == "":
            style = EDGE_STYLE_DEFAULT
         elif not style.upper() in [parm.value for parm in ParamEdgeStyles]:
            self.common.printInvalidEdgeStyle(style)
            return None
         edges[edgeid]["style"] = style

         fontname = attributes["fontname"]
         if fontname == "":
            fontname = EDGE_FONTNAME_DEFAULT
         elif not fontname in [parm.value for parm in ParamFonts]:
            self.common.printInvalidFont(fontname)
            return None
         edges[edgeid]["fontname"] = fontname

         fontsize = attributes["fontsize"]
         if fontsize == 0:
            fontsize = EDGE_FONTSIZE_DEFAULT
         edges[edgeid]["fontsize"] = fontsize

      return edges

   # Line color must be from IBM Color Palette and can be component name, color name, or hex value.
   def checkLineColor(self, pencolor):
      hexvalue = None 
      if pencolor.lower() in Colors.lines:
         hexvalue = Colors.lines[pencolor.lower()]
      return hexvalue

   # Family color ensures that fill color is from same family as line color or transparent or white..
   def checkFamilyColor(self, hexpencolor, hexbgcolor):
      bgcolor = Colors.names[hexbgcolor]
      if bgcolor == "white" or bgcolor == "none":
         return hexbgcolor

      pencolor = Colors.names[hexpencolor]
      lightpencolor = "light" + pencolor

      if bgcolor == lightpencolor:
         return hexbgcolor

      return None

   # Fill color must be from IBM Color Palette and can be transparent, white, or light color from same family as line color.
   def checkFillColor(self, hexpencolor, bgcolor):
      hexbgvalue = None 
      if bgcolor.lower() in Colors.fills:
         hexbgvalue = Colors.fills[bgcolor.lower()]
         hexbgvalue = validFamilyColor(hexpencolor, hexbgcolor) 
      return hexbgvalue

   def addKeys(self):
      # Add additional keys to cluster dictionary.
      for clusterid, attributes in self.clusters.items():
          self.clusters[clusterid]["geometry"] = [0, 0, 0, 0]
          self.clusters[clusterid]["children"] = []
          self.clusters[clusterid]["nodes"] = []

      # Add additional keys to node dictionaries.
      for nodeid, attributes in self.nodes.items():
          self.nodes[nodeid]["geometry"] = [0, 0, 0, 0]
          self.nodes[nodeid]["children"] = []
          self.nodes[nodeid]["nodes"] = []

      return

   def addChildren(self):
      for clusterid, attributes in self.clusters.items():
         parentid = attributes["parentid"] 
         if parentid != None:
            # Add children list to cluster dictionary.
            self.clusters[parentid]["children"].append(clusterid)
         else:
            # Add cluster to outermost list since no parent. 
            self.tops.append(clusterid)

      for clusterid, attributes in self.clusters.items():
         children = attributes["children"] 
         if len(children) == 0:
            # Add cluster to innermost list since no children.
            self.bottoms.append(clusterid)

      return

   def addNodes(self):
      # Add node list to cluster dictionary.`
      for nodeid, attributes in self.nodes.items():
         parentid = attributes["parentid"] 
         if parentid != None:
            self.clusters[parentid]["nodes"].append(nodeid)
      return

   def mergeNodes(self):
      # Combine node list with children list.
      for clusterid, attributes in self.clusters.items():
         nodes = attributes["nodes"] 
         for nodeid in nodes:
            self.clusters[clusterid]["children"].insert(0, nodeid)

      # Combine node dictionary with cluster dictionary. 
      for nodeid, attributes in self.nodes.items():
         self.clusters[nodeid] = attributes

      # Delete node list from clusters. 
      for clusterid, attributes in self.clusters.items():
         del self.clusters[clusterid]["nodes"]

      return

   def calculateNodeGeometry(self):
      mintopspace = 60
      minshapespace = 20
      minnodespace = 60
      minnodewidth = 48
      minnodeheight = 48
      minclusterwidth = 240
      minclusterheight = 152

      for clusterid, attributes in self.clusters.items():
         direction = attributes["direction"]
         childids = attributes["children"]
         childcount = len(childids)
         nodeids = attributes["nodes"]
         nodecount = len(nodeids)
         if nodecount > 0:
            # Set node geometry.
            if direction == "LR":
               if childcount == 0:
                  if nodecount == 1:
                     # Center single node in cluster.
                     x = (minclusterwidth / 2) - (minnodewidth / 2)
                  else:
                     # Left justify first of multiple nodes in cluster.
                     x = minnodespace
               else:
                  # Left justify first of multiple nodes and clusters.
                  x = minnodespace
            elif direction == "TB":
               # Center nodes in cluster.
               x = (minclusterwidth / 2) - (minnodewidth / 2)
            y = mintopspace
            width = minnodewidth
            height = minnodeheight

            for nodeid in nodeids:
               self.nodes[nodeid]["geometry"] = [x, y, width, height]
               # Future: Put long list of nodes on multiple rows.
               if direction == "LR":
                  x += width + minnodespace
               elif direction == "TB":
                  y += height + minnodespace + minshapespace

            # Set cluster geometry of node's parent.
            geometry = attributes["geometry"]
            x = minshapespace
            y = mintopspace
            if direction == "LR":
               width = (nodecount * minnodewidth) + (nodecount * minnodespace) + minnodespace
               height = minclusterheight 
            elif direction == "TB":
               width = minclusterwidth  
               height = (nodecount * minnodeheight) + (nodecount * (minnodespace + minshapespace)) + minnodespace

            width = max(width, minclusterwidth)
            height = max(height, minclusterheight)
            self.clusters[clusterid]["geometry"] = [x, y, width, height]
         else:
            # Set empty cluster geometry. 
            x = minshapespace
            y = mintopspace
            width = minclusterwidth
            height = minclusterheight
            self.clusters[clusterid]["geometry"] = [x, y, width, height]
      return

   def calculateClusterGeometry(self):
      mintopspace = 60
      minshapespace = 20
      #minnodespace = 30
      minnodespace = 60
      minnodewidth = 48
      minnodeheight = 48
      minclusterwidth = 240
      minclusterheight = 152

      for clusterid in self.bottoms:
         while True:
            # Get current cluster details.
            cluster = self.clusters[clusterid]

            parentid = cluster["parentid"]
            direction = cluster["direction"]

            nodeids = cluster["nodes"]
            nodecount = len(nodeids)
            nodewidth = 0

            if direction == "LR":
               saveheight = 0
               totalwidth = 0
               if nodecount > 0:
                  nodewidth = (nodecount * minnodewidth) + (nodecount * minnodespace) + minnodespace

            elif direction == "TB":
               savewidth = 0
               totalheight = 0
               if nodecount > 0:
                  nodeheight = (nodecount * minnodeheight) + (nodecount * minnodespace) + minnodespace
            
            childids = cluster["children"]
            childcount = len(childids)

            count = 0

            # Reset starting position of cluster's children.
            for childid in childids:
               count += 1

               child = self.clusters[childid] 
               label = child["label"]
               geometry = child["geometry"]
               x = geometry[0]
               y = geometry[1]
               width = geometry[2]
               height = geometry[3]

               if direction == "LR":
                  if count == 1:
                     if nodecount > 0:
                        # Reset start position of clusters accounting for nodes.
                        x = nodewidth
                        totalwidth += nodewidth + width
                        self.clusters[childid]["geometry"] = [x, y, width, height]
                     else:
                        totalwidth += width + minshapespace
                  else:
                     # Reset start position of clusters after first cluster.
                     x = totalwidth + minshapespace
                     totalwidth += width + minshapespace
                     self.clusters[childid]["geometry"] = [x, y, width, height]
                  saveheight = max(height, saveheight)
               elif direction == "TB":
                  if count == 1:
                     if nodecount > 0:
                        # Reset start position of clusters accounting for nodes.
                        #y = nodeheight
                        y = nodeheight + (2 * minshapespace) 
                        #totalheight += nodeheight + height
                        totalheight += nodeheight + height + (2 * minshapespace)
                        self.clusters[childid]["geometry"] = [x, y, width, height]
                     else:
                        totalheight += height + minshapespace
                  else:
                     # Reset start position of clusters after first cluster.
                     if nodecount > 0:
                        y = totalheight + minshapespace
                     else:
                        y = totalheight + (3 * minshapespace)
                     totalheight += height + minshapespace
                     self.clusters[childid]["geometry"] = [x, y, width, height]
                  savewidth = max(width, savewidth)

            if childcount > 0:
               geometry = self.clusters[clusterid]["geometry"]
               x = minshapespace
               y = mintopspace
               if direction == "LR":
                  width = totalwidth + minshapespace 
                  height = saveheight + mintopspace + minshapespace
               elif direction =="TB":
                  width = savewidth + (2 * minshapespace)
                  #height = totalheight + mintopspace
                  if nodecount > 0:
                     height = totalheight + mintopspace - (2 * minshapespace)
                  else:
                     height = totalheight + mintopspace
               width = max(width, minclusterwidth)
               height = max(height, minclusterheight)
               self.clusters[clusterid]["geometry"] = [x, y, width, height]

            if parentid == None:
               break
            else:
               # Add current cluster geometry to parent cluster.
               clusterid = parentid
               x = minshapespace
               y = mintopspace
               if direction == "LR":
                  width = totalwidth 
                  height = saveheight + mintopspace + minshapespace
               elif direction =="TB":
                  width = savewidth + minshapespace + minshapespace 
                  height = totalheight + mintopspace + minshapespace
               width = max(width, minclusterwidth)
               height = max(height, minclusterheight)
               self.clusters[clusterid]["geometry"] = [x, y, width, height]

               if direction =="TB":
                  # Recenter nodes.
                  clusterwidth = width
                  for nodeid in nodeids:
                     geometry = self.nodes[nodeid]["geometry"]
                     x = (clusterwidth / 2) - (minnodewidth / 2)
                     y = geometry[1]
                     width = geometry[2]
                     height = geometry[3]
                     self.nodes[nodeid]["geometry"] = [x, y, width, height]

      return

   def alternateChild(self, clusterid, lastColor):
      attributes = self.clusters[clusterid]
      if attributes["shape"].upper() == "ZONE" or  self.common.isAlternateNone():
         attributes["bgcolor"] = "none"
      elif lastColor == "WHITE":
         pencolor = attributes["pencolor"]
         hexvalue = Colors.lines[pencolor]
         fillname = "light" + Colors.names[hexvalue]
         hexvalue = Colors.names[fillname]
         self.clusters[clusterid]["bgcolor"] = hexvalue
         lastColor = "LIGHT"
      elif lastColor == "LIGHT":
         self.clusters[clusterid]["bgcolor"] = "#ffffff"
         lastColor = "WHITE"

      children = attributes["children"]
      for childid in children:
         attributes = self.clusters[childid]
         self.alternateChild(childid, lastColor)

      return

   def alternateFills(self):
      for topid in self.tops:
         attributes = self.clusters[topid]
         # Handle top-level zone.
         if attributes["shape"].upper() == "ZONE" or  self.common.isAlternateNone():
            self.clusters[topid]["bgcolor"] = "none"
         elif self.common.isAlternateLight():
            pencolor = attributes["pencolor"]
            hexvalue = Colors.lines[pencolor]
            fillname = "light" + Colors.names[hexvalue]
            hexvalue = Colors.names[fillname]
            attributes["bgcolor"] = hexvalue
            self.clusters[topid]["bgcolor"] = hexvalue
            lastColor = "LIGHT"
         elif self.common.isAlternateWhite():
            self.clusters[topid]["bgcolor"] = "#ffffff"
            lastColor = "WHITE"

         children = attributes["children"]
         for childid in children:
            attributes = self.clusters[childid]
            self.alternateChild(childid, lastColor)
      return

   # For containers nested inside zones:
   #   Set nested container parent to first container outside of zone.
   #   Set nested container x, y to be relative to first container outside of zone.
   def eliminateZoneParents(self):
      for bottomid in self.bottoms:
         childid = bottomid
         childattributes = self.clusters[childid]
         if childattributes["shape"].upper() == "ZONE":
            continue
        
         parentid = childattributes["parentid"] 
         while parentid != None:
            parentattributes = self.clusters[parentid]

            savex = 0
            savey = 0
            zonesFound = False

            while parentattributes["shape"].upper() == "ZONE":
               zoneid = parentid
               zoneattributes = parentattributes
               zonegeometry = zoneattributes["geometry"]
               savex += zonegeometry[0]
               savey += zonegeometry[1]
               parentid = zoneattributes["parentid"] 
               parentattributes = self.clusters[parentid]
               self.clusters[zoneid]["parentid"] = parentid
               zonesFound = True
               
            if zonesFound == True:
               zonegeometry = zoneattributes["geometry"]
               childgeometry = childattributes["geometry"]
               direction = childattributes["direction"]
               childx = savex + childgeometry[0]
               childy = savey + childgeometry[1]
               childwidth = childgeometry[2]
               childheight = childgeometry[3]
               self.clusters[childid]["geometry"] = [childx, childy, childwidth, childheight]
               self.clusters[childid]["parentid"] = parentid
               savex = 0
               savey = 0

            childid = parentid
            childattributes = self.clusters[childid]
            parentid = childattributes["parentid"] 

      return

   def printClusters(self):
      print("")
      print("Clusters:")
      for key, value in self.clusters.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printNodes(self):
      print("")
      print("Nodes:")
      for key, value in self.nodes.items():
         print("")
         print(f'"{key}": {value}')
      return

   def printBottoms(self):
      print("")
      print("Bottoms:")
      for clusterid in self.bottoms:
         print("")
         print(f'"{clusterid}"')
      return

   def printTops(self):
      print("")
      print("Tops:")
      for clusterid in self.tops:
         print("")
         print(f'"{clusterid}"')
      return

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = ZoneCIDR.AU_SYD_1
         case 'au-syd-2': cidr = ZoneCIDR.AU_SYD_2
         case 'au-syd-3': cidr = ZoneCIDR.AU_SYD_3

         case 'br-sao-1': cidr = ZoneCIDR.BR_SAO_1
         case 'br-sao-2': cidr = ZoneCIDR.BR_SAO_2
         case 'br-sao-3': cidr = ZoneCIDR.BR_SAO_3

         case 'ca-tor-1': cidr = ZoneCIDR.CA_TOR_1
         case 'ca-tor-2': cidr = ZoneCIDR.CA_TOR_2
         case 'ca-tor-3': cidr = ZoneCIDR.CA_TOR_3

         case 'eu-de-1': cidr = ZoneCIDR.EU_DE_1
         case 'eu-de-2': cidr = ZoneCIDR.EU_DE_2
         case 'eu-de-3': cidr = ZoneCIDR.EU_DE_3

         case 'eu-gb-1': cidr = ZoneCIDR.EU_GB_1
         case 'eu-gb-2': cidr = ZoneCIDR.EU_GB_2
         case 'eu-gb-3': cidr = ZoneCIDR.EU_GB_3

         case 'jp-osa-1': cidr = ZoneCIDR.JP_OSA_1
         case 'jp-osa-2': cidr = ZoneCIDR.JP_OSA_2
         case 'jp-osa-3': cidr = ZoneCIDR.JP_OSA_3

         case 'jp-tok-1': cidr = ZoneCIDR.JP_TOK_1
         case 'jp-tok-2': cidr = ZoneCIDR.JP_TOK_2
         case 'jp-tok-3': cidr = ZoneCIDR.JP_TOK_3

         case 'us-east-1': cidr = ZoneCIDR.US_EAST_1
         case 'us-east-2': cidr = ZoneCIDR.US_EAST_2
         case 'us-east-3': cidr = ZoneCIDR.US_EAST_3

         case 'us-south-1': cidr = ZoneCIDR.US_SOUTH_1
         case 'us-south-2': cidr = ZoneCIDR.US_SOUTH_2
         case 'us-south-3': cidr = ZoneCIDR.US_SOUTH_3

         case _: cidr = ZoneCIDR.NONE

      return cidr.value
