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
   operator = None
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
      print("node sub:")
      print(self.attributes["label"])
      print(node.attributes["label"])
      edge = Edge(source=self.nodeid, target=node.nodeid, operator="sub", fontname=self.fontname, fontsize=12)
      return node

   def __lshift__(self, node = None):
      print("node lshift:")
      print(self.attributes["label"])
      print(node.attributes["label"])
      self.node = node
      self.node.operator = "lshift"
      node.node = self
      node.operator = "lshift"
      edge = Edge(source=node.nodeid, target=self.nodeid, operator="lshift", fontname=self.fontname, fontsize=12)
      return node

   def __rshift__(self, node = None):
      print("node rshift:")
      print(self.attributes["label"])
      print(node.attributes["label"])
      self.node = node
      self.node.operator = "rshift"
      edge = Edge(source=self.nodeid, target=node.nodeid, operator="rshift", fontname=self.fontname, fontsize=12)
      return node


class Edge:
   common = None
   edgeid = None
   sourceid = None
   targetid = None
   operator = None
   style = ""
   attributes = {}

   def __init__(self, 
                label: str = "", 
                node: "Node" = None,
                source: "Node" = None,
                target: "Node" = None,
                style: str = "solid",
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
      self.operator = operator

      self.edgeid = randomid()

      self.attributes = {"label": label, "sourceid": self.sourceid, "targetid": self.targetid, "style": self.style, "operator": self.operator, "fontname": fontname, "fontsize": fontsize}

      _edges[self.edgeid] = self.attributes

      return

   #def setSourceID(sourceid):
   #   self.setSourceID(sourceid)
   #   return

   #def setTargetID(targetid):
   #   self.setTargetID(targetid)
   #   return

   """
   def __lshift__(self, node):
      print("edge lshift3:")
      print(self.attributes["label"])
      print(node.attributes["label"])
      print(node.operator)
      self.operator = "lshift"
      return node

   def __rshift__(self, node):
      print("edge rshift3:")
      print(self.attributes["label"])
      print(self.node.attributes["label"])
      print(self.operator)
      print(node.attributes["label"])
      print(node.operator)
      self.operator = "rshift"
      return node
   """
