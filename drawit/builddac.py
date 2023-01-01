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

from math import isnan

from .colors import Colors
from .common import Common

from .constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from .shapesdac import Shapes

class BuildDAC:
   common = None
   shapes = None
   cloudname = ""
   clusters = {}
   nodes = {}
   links = {}
   tops = []
   bottoms = []

   def __init__(self, common, clusters, nodes, edges):
      self.common = common
      self.clusters = clusters
      self.nodes = nodes
      self.edges = edges

      self.shapes = Shapes(common)

      self.addKeys()
      self.addChildren()
      self.alternateFills()
      self.addNodes()
      self.calculateNodeGeometry()
      self.calculateClusterGeometry()
      #self.printClusters()
      #self.printNodes()
      #self.printTops()
      #self.printBottoms()
      self.mergeNodes()

   def buildDiagrams(self):
      outputFolder = self.common.getOutputFolder()
      if outputFolder[-1] != '/':
         self.common.setOutputFolder(outputFolder + '/')

      clouddata = self.buildAll()

      for regionname, regionvalues in clouddata.items():
         self.shapes.buildXML(regionvalues, regionname)
         self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())
         self.shapes.resetXML()

      return

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

      regiondata["IBM Cloud"] = {'nodes': nodes, 'links': links, 'values': values}

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
            if direction == "LR":
               # Set node geometry.
               if nodecount == 1 and childcount == 0:
                  # Center single node in cluster.
                  x = (minclusterwidth / 2) - (minnodewidth / 2)
               else:
                  # Left justify first of multiple nodes in cluster.
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
      minnodespace = 30
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
                        y = nodeheight
                        totalheight += nodeheight + height
                        self.clusters[childid]["geometry"] = [x, y, width, height]
                     else:
                        totalheight += height + minshapespace
                  else:
                     # Reset start position of clusters after first cluster.
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

      return

   def alternateChild(self, clusterid, flag):
      attributes = self.clusters[clusterid]
      if flag:
         if attributes["shape"].upper() == "ZONE":
            attributes["bgcolor"] = "none"
         else:
            pencolor = attributes["pencolor"]
            hexvalue = Colors.lines[pencolor]
            fillname = "light" + Colors.names[hexvalue]
            hexvalue = Colors.names[fillname]
            attributes["bgcolor"] = hexvalue
      else:
         attributes["bgcolor"] = "#ffffff"

      children = attributes["children"]
      for child in children:
         self.alternateChild(child, not flag)

      return

   def alternateFills(self):
      for top in self.tops:
         attributes = self.clusters[top]
         children = attributes["children"]
         for child in children:
            self.alternateChild(child, True)
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
