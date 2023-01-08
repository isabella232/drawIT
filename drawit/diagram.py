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

from sys import exit as sys_exit
from contextvars import ContextVar
from enum import Enum
from uuid import uuid4

from .common import Common
from .builddac import BuildDAC

_diagram = ContextVar("diagram")
_cluster = ContextVar("cluster")

_diagrams = {} # Dictionary of diagrams.
_clusters = {} # Dictionary of clusters.
_nodes = {}    # Dictionary of nodes.
_edges = {}    # Dictionary of edges.


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


class Diagram:
   common = None
   attributes = {}
   diagramid = None
   diagram = None

   def __init__(self, 
                name = "",
                filename = "",
                direction = "",
                alternate = "",
                provider = "",
                fontname = "",
                fontsize = 0,
                outformat = ""):
      self.common = Common()
      self.diagramid = randomid()

      self.attributes = {"name": name, "filename": filename, "direction": direction, "alternate": alternate, "provider": provider, "fontname": fontname, "fontsize": fontsize,  "outformat": outformat}
      _diagrams[self.diagramid] = self.attributes
      return

   def __enter__(self):
      setDiagram(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      self.diagram  = BuildDAC(self.common, _diagrams, _clusters, _nodes, _edges)
      self.diagram.buildDiagrams()
      setDiagram(None)
      setCluster(None)
      return


class Cluster:
   common = None
   icons = None
   shapeid = None
   parentid = None
   sourceid = None
   targetid = None
   parent = None
   node = None
   edge = None
   attributes = {}

   def __init__(self, 
                label = "",
                sublabel = "",
                shape = "",
                pencolor = "",
                bgcolor = "",
                icon = "",
                direction = "",
                alternate = "",
                provider = "",
                fontname = "",
                fontsize = 0,
                badgetext = "", 
                badgeshape = "",
                badgepencolor = "",
                badgebgcolor = ""):
      self.common = Common()
      self.shapeid = randomid()

      self.parent = getCluster()
      if self.parent:
         self.parentid = self.parent.shapeid
      else:
         self.parent = None

      self.attributes = {"label": label, "sublabel": sublabel, "shape": shape, "pencolor": pencolor, "bgcolor": bgcolor, "badgetext": badgetext, "badgeshape": badgeshape, "badgepencolor": badgepencolor, "badgebgcolor": badgebgcolor, "icon": icon, "direction": direction, "alternate": alternate, "provider": provider, "fontname": fontname, "fontsize": fontsize, "parentid": self.parentid}

      return

   def __enter__(self):
      setCluster(self)
      return self

   def __exit__(self, exception_type, exception_value, traceback):
      _clusters[self.shapeid] = self.attributes
      if self.parent:
         setCluster(self.parent)
      return

   def __sub__(self, shape = None):
      # cluster - cluster or cluster - node or cluster - edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=self.shapeid, targetid=shape.shapeid, arrow="noarrow", operator="sub", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "noarrow"
         shape.operator = "sub"
      return shape

   def __lshift__(self, shape = None):
      # shape << shape or shape << edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=shape.shapeid, targetid=self.shapeid, arrow="singlearrow", operator="lshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "unknown"
         shapee.operator = "lshift"
      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=self.shapeid, targetid=shape.shapeid, arrow="singlearrow", operator="rshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "unknown"
         shape.operator = "rshift"
      return shape

class Node:
   common = None
   icons = None
   shapeid = None
   parentid = None
   sourceid = None
   targetid = None
   parent = None
   arrow = ""
   operator = ""
   style = ""
   node = None
   edge = None
   attributes = {}

   def __init__(self, 
                label = "", 
                sublabel = "", 
                shape = "",
                pencolor = "",
                bgcolor = "",
                icon = "",
                direction = "",
                provider = "",
                fontname = "",
                fontsize = 0,
                badgetext = "", 
                badgeshape = "",
                badgepencolor = "",
                badgebgcolor = ""):
      self.common = Common()
      self.shapeid = randomid()
      self.parent = getCluster()
      self.parentid = self.parent.shapeid
      setCluster(self.parent)

      self.attributes = {"label": label, "sublabel": sublabel, "shape": shape, "pencolor": pencolor, "bgcolor": bgcolor, "badgetext": badgetext, "badgeshape": badgeshape, "badgepencolor": badgepencolor, "badgebgcolor": badgebgcolor, "icon": icon, "direction": direction, "provider": provider, "fontname": fontname, "fontsize": fontsize, "parentid": self.parentid}

      _nodes[self.shapeid] = self.attributes

      return

   #def __repr__(self):
   #   print("repr:")
   #   print(self.attributes)

   #def __str__(self):
   #   print("str:")
   #   return self.attributes["label"]

   def __sub__(self, shape = None):
      # node - node or node - edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=self.shapeid, targetid=shape.shapeid, arrow="noarrow", operator="sub", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "noarrow"
         shape.operator = "sub"
      return shape

   def __lshift__(self, shape = None):
      # shape << shape or shape << edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=shape.shapeid, targetid=self.shapeid, arrow="singlearrow", operator="lshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "singlearrow"
         shape.operator = "lshift"
      return shape

   def __rshift__(self, shape = None):
      # shape >> shape or shape >> edge
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         edge = Edge(sourceid=self.shapeid, targetid=shape.shapeid, arrow="singlearrow", operator="rshift", fontname=self.fontname, fontsize=12)
      else:  # isinstance(shape, Edge)
         shape.sourceid = self.shapeid
         shape.arrow = "singlearrow"
         shape.operator = "rshift"
      return shape


class Edge:
   common = None
   shapeid = None
   parentid = None
   #sourceid = None
   #targetid = None
   parent = None
   #arrow = ""
   #operator = ""
   #style = ""
   node = None
   edge = None
   attributes = {}

   def __init__(self, 
                label = "", 
                style = "",
                fontname = "",
                fontsize = 0,
                arrow = "",
                operator = "",     # Internal use only.
                sourceid = None,   # Internal use only.
                targetid = None):  # Internal use only.
      self.common = Common()
      self.shapeid = randomid()

      self.attributes = {"label": label, "sourceid": sourceid, "targetid": targetid, "style": style, "arrow": arrow, "fontname": fontname, "fontsize": fontsize}

      _edges[self.shapeid] = self.attributes

      return

   def __sub__(self, shape = None):
      # edge - shape
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         if self.sourceid != None:
            _edges[self.shapeid]["sourceid"] = self.sourceid
            _edges[self.shapeid]["targetid"] = shape.shapeid
            _edges[self.shapeid]["arrow"] = self.arrow
            _edges[self.shapeid]["operator"] = self.operator
         else:
            # Minus has precedence over << and sourceid hasn't been set.
            # Set dummy value for source to prevent serialization error in dumpXML.
            _edges[self.shapeid]["sourceid"] = shape.shapeid
            _edges[self.shapeid]["targetid"] = shape.shapeid
            _edges[self.shapeid]["arrow"] = self.arrow
            _edges[self.shapeid]["operator"] = self.operator
            print("Edge.__sub__: shape << edge - shape not supported")
            sys_exit()
      else:
         print("Edge.__sub__: edge - shape not supported")
         sys_exit()

      return shape

   def __lshift__(self, shape = None):
      # edge << shape
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         _edges[self.shapeid]["sourceid"] = shape.shapeid
         _edges[self.shapeid]["targetid"] = self.sourceid
         _edges[self.shapeid]["operator"] = self.operator
         arrow = "doublearrow" if self.operator == "rshift" else "singlearrow" 
         _edges[self.shapeid]["arrow"] = arrow
      else:
         print("Edge.__lshift__: edge << shape not supported")
         sys_exit()
      return shape

   def __rshift__(self, shape = None):
      # edge >> shape
      if isinstance(shape, Cluster) or isinstance(shape, Node):
         _edges[self.shapeid]["sourceid"] = self.sourceid
         _edges[self.shapeid]["targetid"] = shape.shapeid 
         _edges[self.shapeid]["operator"] = self.operator 
         arrow = "doublearrow" if self.operator == "lshift" else "singlearrow" 
         _edges[self.shapeid]["arrow"] = arrow
      else:
         print("Edge.__rshift__: edge >> shape not supported")
         sys_exit()
      return shape
