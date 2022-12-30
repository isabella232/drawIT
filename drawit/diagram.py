# @file diagram.py
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

from os import path
from sys import exit as sys_exit
from contextvars import ContextVar
from uuid import uuid4
#from typing import List, Union, Dict

from .colors import Colors
from .common import Common
from .icons import Icons
from .builddac import BuildDAC

_diagram = ContextVar("diagram")
_cluster = ContextVar("cluster")

_clusters = {} # Dictionary of clusters.
_nodes = {}    # Dictionary of nodes.
_edges = {}    # Dictionary of edges.

DIRECTIONS = ("TB", "BT", "LR", "RL")
OUTPUTFORMAT = ("jpg", "pdf", "png", "svg", "xml")
NODESHAPES = ("nodel", "nodep", "compl", "compp")
CLUSTERSHAPES = ("locl", "locp", "nodel-expanded", "nodep-expanded", "compl-expanded", "compp-expanded", "zone")
FONTS = ("ibm plex sans", "ibm plex sans arabic", "ibm plex sans devanagari", "ibm plex sans hebrew", "ibm plex sans jp", "ibm plex sans kr", "ibm plex sans thai")

EDGESTYLES = ("solid", "dashed")
EXTENDED_EDGESTYLES = {  
   # Allows customization of lines and arrows.
   "solidline": "dashed=0;",
   "dashedline": "dashed=1;",
   "noarrow": "endArrow=none;", 
   "singlearrow": "endArrow=block;endFill=1;", 
   "doublearrow": "endArrow=block;endFill=1;startArrow=block;startFill=1;"} 

def getDiagram():
   try:
      return _diagram.get()
   except LookupError:
      return None

def setDiagram(diagram):
   _diagram.set(diagram)

def getCluster():
   try:
      return _cluster.get()
   except LookupError:
      return None

def setCluster(cluster):
   _cluster.set(cluster)


# Return a unique id for clusterid and nodeid.
@staticmethod
def randomid():
   return uuid4().hex

# Valid direction must be one of the supported directions.
def validDirection(direction):
   return direction.upper() in DIRECTIONS

# Valid font must be and an IBM Plex Sans font.
def validFont(font):
   return font.lower() in FONTS

# Valid cluster shape must be a valid IBM2 expanded shape.
def validClusterShape(shape):
   return shape.lower() in CLUSTERSHAPES

# Valid node shape must be a valid IBM2 collapsed shape.
def validNodeShape(shape):
   return shape.lower() in NODESHAPES

# Valid edge style must be one of the basic or extended edge styles (planned). 
def validEdgeStyle(style):
   return style.lower() in EDGESTYLES

# Valid line color must be from IBM Color Palette and can be component name, color name, or hex value.
def validLineColor(pencolor):
   hexvalue = None 
   if pencolor.lower() in Colors.lines:
      hexvalue = Colors.lines[pencolor.lower()]
   return hexvalue

# Valid family color ensures that fill color is from same family as line color or transparent or white..
def validFamilyColor(hexpencolor, hexbgcolor):
   bgcolor = Colors.names[hexbgcolor]
   if bgcolor == "white" or bgcolor == "none":
      return hexbgcolor

   pencolor = Colors.names[hexpencolor]
   lightpencolor = "light" + pencolor

   if bgcolor == lightpencolor:
      return hexbgcolor

   return None

# Valid fill color must be from IBM Color Palette and can be transparent, white, or light color from same family as line color.
def validFillColor(hexpencolor, bgcolor):
   hexbgvalue = None 
   if bgcolor.lower() in Colors.fills:
      hexbgvalue = Colors.fills[bgcolor.lower()]
      hexbgvalue = validFamilyColor(hexpencolor, hexbgcolor) 
   return hexbgvalue


class Diagram:
   common = None
   attributes = {}
   data = {}
   diagramid = None
   diagram = None
   name = ""

   def __init__(self, 
                name: str = "",
                filename: str = "",
                direction: str = "LR",
                outformat: str = "png"):
      self.name = name if name else "diagram"
      self.filename = filename if filename else self.name

      self.common = Common()
      self.common.setOutputFile(self.filename + ".xml")

      self.diagramid = randomid()

      if not self.validDirection(direction):
         self.common.printInvalidDirection(direction)
         sys_exit()

      if not self.validOutputFormat(outformat):
         self.common.printInvalidOutputFormat(outformat)
         sys_exit()

      return

   def __enter__(self):
      self.common.printStartFile(self.filename + ".py", self.common.getCloudType().value.upper())
      setDiagram(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      self.diagram  = BuildDAC(self.common, _clusters, _nodes, _edges)
      self.diagram.buildDiagrams()
      outputfolder = self.common.getOutputFolder()
      outputfile = self.common.getOutputFile()
      self.common.printDone(path.join(outputfolder, outputfile), self.common.getCloudType().value.upper())
      setDiagram(None)
      setCluster(None)
      return

   def validDirection(self, direction):
      return direction.upper() in DIRECTIONS

   def validOutputFormat(self, outformat):
      return outformat.lower() in OUTPUTFORMAT


class Cluster:
   common = None
   icons = None
   clusterid = None
   parentid = None
   parent = None
   fontname = None
   fontsize = 14

   def __init__(self, 
                label: str = "cluster", 
                sublabel: str = "", 
                shape: str = "locp",
                pencolor: str = "#1192e8",
                bgcolor: str = None,
                badgetext: str = "", 
                badgeshape: str = None,
                badgepencolor: str = None,
                badgebgcolor: str = None,
                icon: str = "undefined",
                direction: str = "LR", 
                fontname: str = "IBM Plex Sans",
                fontsize: int = 14):

      self.common = Common()
      self.icons = Icons(self.common)

      if not validDirection(direction):
         self.common.printInvalidDirection(direction)
         sys_exit()

      if not validFont(fontname):
         self.common.printInvalidFont(fontname)
         sys_exit()

      if not validClusterShape(shape):
         self.common.printInvalidClusterShape(shape)
         sys_exit()

      if not self.icons.validIcon(icon):
         self.common.printInvalidIcon(icon)
         sys_exit()

      hexpencolor = validLineColor(pencolor)
      if hexpencolor == None:
         self.common.printInvalidLineColor(pencolor)
         sys_exit()

      hexbgcolor = "#ffffff"
      if bgcolor != None:
         hexbgcolor = validFillColor(hexpencolor, bgcolor)
         if hexbgcolor == None:
            self.common.printInvalidFillColor(bgcolor)
            sys_exit()

      self.fontname = fontname
      self.fontsize = fontsize

      self.clusterid = randomid()

      self.parent = getCluster()
      if self.parent:
         self.parentid = self.parent.clusterid
      else:
         self.parent = None

      self.attributes = {"label": label, "sublabel": sublabel, "shape": shape, "pencolor": hexpencolor, "bgcolor": hexbgcolor, "badgetext": badgetext, "badgeshape": badgeshape, "badgepencolor": badgepencolor, "badgebgcolor": badgebgcolor, "icon": icon, "direction": direction, "fontname": fontname, "fontsize": fontsize, "parentid": self.parentid}

      return

   def __enter__(self):
      setCluster(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      _clusters[self.clusterid] = self.attributes
      if self.parent:
         setCluster(self.parent)
      return


class Node:
   common = None
   icons = None
   nodeid = None
   parentid = None
   parent = None
   arrow = ""
   operator = ""
   node = None
   edge = None
   fontname = None
   fontsize = 14
   attributes = {}

   def __init__(self, 
                label: str = "node", 
                sublabel: str = "", 
                shape: str = "nodep",
                pencolor: str = "#1192e8",
                bgcolor: str = None,
                badgetext: str = "", 
                badgeshape: str = None,
                badgepencolor: str = None,
                badgebgcolor: str = None,
                icon: str = "undefined",
                direction: str = "LR",
                fontname: str = "IBM Plex Sans",
                fontsize: int = 14):

      self.common = Common()
      self.icons = Icons(self.common)

      if not validDirection(direction):
         self.common.printInvalidDirection(direction)
         sys_exit()

      if not validFont(fontname):
         self.common.printInvalidFont(fontname)
         sys_exit()

      if not validNodeShape(shape):
         self.common.printInvalidNodeShape(shape)
         sys_exit()

      if not self.icons.validIcon(icon):
         self.common.printInvalidIcon(icon)
         sys_exit()

      hexpencolor = validLineColor(pencolor)
      if hexpencolor == None:
         self.common.printInvalidLineColor(pencolor)
         sys_exit()

      hexbgcolor = ""
      if bgcolor != None:
         hexbgcolor = validFillColor(hexpencolor, bgcolor)
         if hexbgcolor == None:
            self.common.printInvalidFillColor(bgcolor)
            sys_exit()

      self.fontname = fontname
      self.fontsize = fontsize

      self.nodeid = randomid()

      self.parent = getCluster()
      #if self.parent:
      self.parentid = self.parent.clusterid
      setCluster(self.parent)
      #else:
      #   self.parent = None

      self.attributes = {"label": label, "sublabel": sublabel, "shape": shape, "pencolor": hexpencolor, "bgcolor": hexbgcolor, "badgetext": badgetext, "badgeshape": badgeshape, "badgepencolor": badgepencolor, "badgebgcolor": badgebgcolor, "icon": icon, "direction": direction, "fontname": fontname, "fontsize": fontsize, "parentid": self.parentid}

      _nodes[self.nodeid] = self.attributes

      return

   #def __repr__(self):
   #   print("repr:")
   #   print(self.attributes)

   #def __str__(self):
   #   print("str:")
   #   return self.attributes["label"]

   def __sub__(self, node = None):
      # node - node or node - edge
      if isinstance(node, Node):
         edge = Edge(source=self.nodeid, target=node.nodeid, arrow="noarrow", operator="sub", fontname=self.fontname, fontsize=12)
      else:  # isinstance(node, Edge)
         edge = node
         edge.nodeid = self.nodeid
         edge.arrow = "noarrow"
         edge.operator = "sub"
      return node

   def __lshift__(self, node = None):
      # node << node or node << edge
      if isinstance(node, Node):
         edge = Edge(source=node.nodeid, target=self.nodeid, arrow="singlearrow", operator="lshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(node, Edge)
         edge = node
         edge.nodeid = self.nodeid
         edge.arrow = "unknown"
         edge.operator = "lshift"
      return node

   def __rshift__(self, node = None):
      # node >> node or node >> edge
      if isinstance(node, Node):
         edge = Edge(source=self.nodeid, target=node.nodeid, arrow="singlearrow", operator="rshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(node, Edge)
         edge = node
         edge.nodeid = self.nodeid
         edge.arrow = "unknown"
         edge.operator = "rshift"
      return node


class Edge:
   common = None
   edgeid = None
   nodeid = None
   sourceid = None
   targetid = None
   node = None
   nodeid = None
   arrow = None
   operator = ""
   style = ""
   attributes = {}

   def __init__(self, 
                label: str = "", 
                #node: "Node" = None,
                source: "Node" = None,
                target: "Node" = None,
                style: str = "solid",
                arrow: str = "singlearrow",
                operator: str = "",
                fontname: str = "IBM Plex Sans",
                fontsize: int = 12):

      self.common = Common()

      if not validEdgeStyle(style):
         self.common.printInvalidEdgeStyle(style)
         sys_exit()

      if not validFont(fontname):
         self.common.printInvalidFont(fontname)
         sys_exit()

      self.sourceid = source
      self.targetid = target
      self.style = style
      self.arrow = arrow
      self.operator = operator

      self.edgeid = randomid()

      self.attributes = {"label": label, "sourceid": self.sourceid, "targetid": self.targetid, "style": self.style, "arrow": self.arrow, "fontname": fontname, "fontsize": fontsize}

      _edges[self.edgeid] = self.attributes

      return

   def __sub__(self, node = None):
      # edge - node
      if isinstance(node, Node):
         if self.nodeid != None:
            selfnodeid = self.nodeid
            selfarrow = self.arrow
            selfoperator = self.operator

            _edges[self.edgeid]["sourceid"] = node.nodeid
            _edges[self.edgeid]["targetid"] = selfnodeid
            _edges[self.edgeid]["arrow"] = selfarrow
         else:
            # Minus has precedence over << so nodeid hasn't been set yet.
            print("Edge.__sub__: node << edge - node not supported")
            sys_exit()
      else:
         print("Edge.__sub__: edge - node not supported")
         sys_exit()

      return node

   def __lshift__(self, node):
      # edge << node
      if isinstance(node, Node):
         #self.operator = "lshift"
         selfnodeid = self.nodeid
         selfarrow = self.arrow
         selfoperator = self.operator

         _edges[self.edgeid]["sourceid"] = node.nodeid
         _edges[self.edgeid]["targetid"] = selfnodeid
         arrow = "doublearrow" if selfoperator == "rshift" else "singlearrow" 
         _edges[self.edgeid]["arrow"] = arrow
      else:
         print("Edge.__lshift__: edge << node not supported")
         sys_exit()
      return node

   def __rshift__(self, node):
      # edge >> node
      if isinstance(node, Node):
         #self.operator = "rshift"
         selfnodeid = self.nodeid
         selfarrow = self.arrow
         selfoperator = self.operator

         _edges[self.edgeid]["sourceid"] = selfnodeid
         _edges[self.edgeid]["targetid"] = node.nodeid
         arrow = "doublearrow" if selfoperator == "lshift" else "singlearrow" 
         _edges[self.edgeid]["arrow"] = arrow
      else:
         print("Edge.__rshift__: edge >> node not supported")
         sys_exit()
      return node
