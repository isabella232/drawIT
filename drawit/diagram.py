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

DIRECTIONS = ("TB", "BT", "LR", "RL")
OUTPUTFORMAT = ("jpg", "pdf", "png", "svg", "xml")
NODESHAPES = ("nodel", "nodep", "compl", "compp")
CLUSTERSHAPES = ("locl", "locp", "nodel-expanded", "nodep-expanded", "compl-expanded", "compp-expanded", "zone")
FONTS = ("ibm plex sans", "ibm plex sans arabic", "ibm plex sans devanagari", "ibm plex sans hebrew", "ibm plex sans jp", "ibm plex sans kr", "ibm plex sans thai")

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

@staticmethod
def randomid():
   return uuid4().hex

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
      setDiagram(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      self.diagram  = BuildDAC(self.common, _clusters, _nodes)
      self.diagram.buildDiagrams()
      outputfolder = self.common.getOutputFolder()
      outputfile = self.common.getOutputFile()
      self.common.printDone(path.join(outputfolder, outputfile), "IBM")
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

      if not self.validDirection(direction):
         self.common.printInvalidDirection(direction)
         sys_exit()

      if not self.validFont(fontname):
         self.common.printInvalidFont(fontname)
         sys_exit()

      if not self.validShape(shape):
         self.common.printInvalidShape(shape)
         sys_exit()

      if not self.icons.validIcon(icon):
         self.common.printInvalidIcon(icon)
         sys_exit()

      hexpencolor = self.validLineColor(pencolor)
      if hexpencolor == None:
         self.common.printInvalidLineColor(pencolor)
         sys_exit()

      hexbgcolor = "#ffffff"
      if bgcolor != None:
         hexbgcolor = self.validFillColor(hexpencolor, bgcolor)
         if hexbgcolor == None:
            self.common.printInvalidFillColor(bgcolor)
            sys_exit()

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
      #if self.parent:
      #   setCluster(self.parent)
      _clusters[self.clusterid] = self.attributes
      if self.parent:
         setCluster(self.parent)
      return

   def validDirection(self, direction):
      return direction.upper() in DIRECTIONS

   def validFont(self, font):
      return font.lower() in FONTS

   def validShape(self, shape):
      return shape.lower() in CLUSTERSHAPES

   # Line color can be component name, color name, or hex value.
   def validLineColor(self, pencolor):
      hexpenvalue = None 
      if pencolor.lower() in Colors.lines:
         hexpenvalue = Colors.lines[pencolor.lower()]
      return hexpenvalue

   # Fill color can be transparent, white, or light color from same family as line color.
   def validFamilyColor(self, hexpencolor, hexbgcolor):
      bgcolor = Colors.names[hexbgcolor]
      if bgcolor == "white" or bgcolor == "none":
         return hexbgcolor

      pencolor = Colors.names[hexpencolor]
      lightpencolor = "light" + pencolor

      if bgcolor == lightpencolor:
         return hexbgcolor

      return None

   # Fill color can be transparent, white, or light color from same family as line color.
   def validFillColor(self, hexpencolor, bgcolor):
      hexbgvalue = None 
      if bgcolor.lower() in Colors.fills:
         hexbgvalue = Colors.fills[bgcolor.lower()]
         hexbgvalue = validFamilyColor(hexpencolor, hexbgcolor) 

      return hexbgvalue

class Node:
   common = None
   icons = None
   nodeid = None
   parentid = None
   parent = None

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
                fontsize = 14):

      self.common = Common()
      self.icons = Icons(self.common)

      if not self.validDirection(direction):
         self.common.printInvalidDirection(direction)
         sys_exit()

      if not self.validFont(fontname):
         self.common.printInvalidFont(fontname)
         sys_exit()

      if not self.validShape(shape):
         self.common.printInvalidShape(shape)
         sys_exit()

      if not self.icons.validIcon(icon):
         self.common.printInvalidIcon(icon)
         sys_exit()

      hexpencolor = self.validLineColor(pencolor)
      if hexpencolor == None:
         self.common.printInvalidLineColor(pencolor)
         sys_exit()

      hexbgcolor = ""
      if bgcolor != None:
         hexbgcolor = self.validFillColor(hexpencolor, bgcolor)
         if hexbgcolor == None:
            self.common.printInvalidFillColor(bgcolor)
            sys_exit()

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

   def validDirection(self, direction):
      return direction.upper() in DIRECTIONS

   def validFont(self, font):
      return font.lower() in FONTS

   def validShape(self, shape):
      return shape.lower() in NODESHAPES

   # Line color can be component name, color name, or hex value.
   def validLineColor(self, pencolor):
      hexvalue = None 
      if pencolor.lower() in Colors.lines:
         hexvalue = Colors.lines[pencolor.lower()]
      return hexvalue

   # Fill color can be transparent, white, or light color from same family as line color.
   def validFamilyColor(self, hexpencolor, hexbgcolor):
      bgcolor = Colors.names[hexbgcolor]
      if bgcolor == "white" or bgcolor == "none":
         return hexbgcolor

      pencolor = Colors.names[hexpencolor]
      lightpencolor = "light" + pencolor

      if bgcolor == lightpencolor:
         return hexbgcolor

      return None

   # Fill color can be transparent, white, or light color from same family as line color.
   def validFillColor(self, hexpencolor, bgcolor):
      hexbgvalue = None 
      if bgcolor.lower() in Colors.fills:
         hexbgvalue = Colors.fills[bgcolor.lower()]
         hexbgvalue = validFamilyColor(hexpencolor, hexbgcolor) 

      return hexbgvalue
