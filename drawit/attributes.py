# @file attributes.py
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

from enum import Enum

class Attributes:
   def __init__(self):
      self.diagrams = {}
      self.clusters = {}
      self.nodes = {}
      self.edges = {}

   def reset(self):
      self.diagrams = {}
      self.clusters = {}
      self.nodes = {}
      self.edges = {}

   def getDiagrams(self):
      return self.diagrams

   def getClusters(self):
      return self.clusters

   def getNodes(self):
      return self.nodes

   def getEdges(self):
      return self.edges

   def setDiagrams(self, diagrams):
      self.diagrams = diagrams

   def setClusters(self, clusters):
      self.clusters = clusters
      #print("")
      #print(self.clusters)

   def setNodes(self, nodes):
      self.nodes = nodes

   def setEdges(self, edges):
      self.edges = edges

   def addDiagram(self, diagramid, attributes):
      self.diagrams[diagramid] = attributes

   def addCluster(self, clusterid, attributes):
      self.clusters[clusterid] = attributes

   def addNode(self, nodeid, attributes):
      self.nodes[nodeid] = attributes

   def addEdge(self, edgeid, attributes):
      self.edges[edgeid] = attributes

   def setEdgeSourceID(self, shapeid, sourceid):
      self.edges[shapeid]["sourceid"] = sourceid 

   def setEdgeTargetID(self, shapeid, targetid):
      self.edges[shapeid]["targetid"] = targetid

   def setEdgeArrow(self, shapeid, arrow):
      self.edges[shapeid]["arrow"] = arrow 

   def setEdgeOperator(self, shapeid, operator):
      self.edges[shapeid]["operator"] = operator


# Valid attribute values.

class Directions(Enum):
   LR = 'LR'
   TB = 'TB'

class Alternates(Enum):
   WHITE = 'WHITE'  # white-to-light
   LIGHT = 'LIGHT'  # light-to-white
   NONE = 'NONE'     # all transparent
   USER = 'USER'     # all user-defined

class Providers(Enum):
   ANY = 'ANY'  # logical
   IBM = 'IBM'   # prescribed-ibm

class NodeShapes(Enum):
   ACTOR = 'ACTOR'
   COMPONENT = 'COMPONENT'
   NODE = 'NODE'

class ClusterShapes(Enum):
   COMPONENT = 'COMPONENT'
   LOCATION = 'LOCATION'
   NODE = 'NODE'
   ZONE = 'ZONE'

class OutFormats(Enum):
   JPG = 'JPG'
   PDF = 'PDF'
   PNG = 'PNG'
   SVG = 'SVG'
   XML = 'XML'

class Fonts(Enum):
   IBM_PLEX_SANS = 'IBM Plex Sans'
   IBM_PLEX_SANS_ARABIC = 'IBM Plex Sans Arabic'
   IBM_PLEX_SANS_DEVANAGARI = 'IBM Plex Sans Devanagari'
   IBM_PLEX_SANS_HEBREW = 'IBM Plex Sans Hebrew'
   IBM_PLEX_SANS_JP = 'IBM Plex Sans JP'
   IBM_PLEX_SANS_KR = 'IBM Plex Sans KR'
   IBM_PLEX_SANS_THAI = 'IBM Plex Sans Thai'

class EdgeStyles(Enum):
   SOLID = 'SOLID'
   DASHED = 'DASHED'

# Allows customization of lines and arrows.
class ExtendedEdgeStyles(Enum):
   SOLID_LINE = 'dashed=0;'
   DASHED_LINE = 'dashed=1;'
   NO_ARROW = 'endArrow=none;'
   SINGLE_ARROW = 'endArrow=block;endFill=1;'
   DOUBLE_ARROW = 'endArrow=block;endFill=1;startArrow=block;startFill=1;'


