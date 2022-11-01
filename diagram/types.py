# @file types.py
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

import random
import time

from common.common import Common

from diagram.constants import *
from diagram.elements import Elements
from diagram.icons import Icons

class Types:
   common = None
   data = None
   elements = None
   icons = None

   def __init__(self, common):
      self.common = common
      self.data = {'header': {'type': 'device',
                              'compressed': 'false'}}
      self.elements = Elements(self.data)
      self.icons = Icons(common)
      random.seed(time.time())

   def buildLink(self, label, source, target, meta):
      data = {'header': {'id': self.common.compress(str(random.random())),
                         'label': ''},
              'cell':   {'style': 'endArrow=none;dashed=1;',
                         'edge': '1',
                         'parent': '1',
                         'source': self.common.compress(source),
                         'target': self.common.compress(target)},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLink(self, label, source, target, meta):
      data = {'header': {'id': self.common.compress(str(random.random())),
                         'label': label},
              'cell':   {'style': 'endArrow=none;dashed=0;',
                         'edge': '1',
                         'parent': '1',
                         'source': self.common.compress(source),
                         'target': iself.common.compress(target)},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLinkSingleArrow(self, label, source, target, meta):
         data = {'header': {'id': self.common.compress(str(random.random())),
                            'label': label},
                 'cell':   {'style': 'endArrow=block;endFill=1;dashed=0;',
                            'edge': '1',
                            'parent': '1',
                            'source': self.common.compress(source),
                            'target': self.common.compress(target)},
                  'geo':   {'relative': '1',
                            'as': 'geometry'}}
         return data

   def buildSolidLinkDoubleArrow(self, label, source, target, meta):
      data = {'header': {'id': self.common.compress(str(random.random())),
                         'label': label},
              'cell':   {'style': 'endArrow=block;endFill=1;startArrow=block;startFill=1;dashed=0;',
                         'edge': '1',
                         'parent': '1',
                         'source': self.common.compress(source),
                         'target': self.common.compress(target)},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildNode(self, shapetype, shapekind, shapefill, id, parentid, name, subname, badgetext, x, y, width, height, meta):
      iconname, iconcolor = self.icons.getIcon(shapetype)

      if self.common.isLogicalShapes():
         if shapekind == ACTOR_KIND:
            style = ACTOR_STYLE
         elif shapekind == NODE_KIND:
            style = LOGICAL_NODE_STYLE
         else:
            style = LOGICAL_LOCATION_STYLE
      else: # check prescribed
         if shapekind == ACTOR_KIND:
            style = ACTOR_STYLE
         elif shapekind == NODE_KIND:
            style = PRESCRIBED_NODE_STYLE
         else:
            style = PRESCRIBED_LOCATION_STYLE

      style += iconcolor + shapefill

      shapelabel = "<b style='font-weight:600'>%Primary-Label%</b><br>%Secondary-Text%"
      labelsize = 30

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      header = {'id': id,
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {'Badge-Text': badgetext,
               'Icon-Name': iconname,
               'Primary-Label': name,
               'Secondary-Text': subname}

      if meta != None:
         props.update(meta)

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildValue(self, id, parentid, name, parent, subname, text, x, y, width, height):
      shape = ibmshapes['text']
      style = shape['style']  
      data = {'cell': {'id': id,
                       'value': text,
                       'style': style,
                       'parent': parentid,
                       'vertex': '1'},
              'geo':  {'x': str(x),
                       'y': str(y),
                       'width': str(width),
                       'height': str(height),
                       'as': 'geometry'}}
      return data

   def buildPage(self, name):
      data = {'header': {'id': self.common.compress(name),
                         'name': name},
              'graph':  {'dx': '1326',
                         'dy': '846',
                         'grid': '1',
                         'gridSize': '10',
                         'guides': '1',
                         'tooltips': '1',
                         'connect': '1',
                         'arrows': '1',
                         'fold': '1',
                         'page': '1',
                         'pageScale': '1',
                         'pageWidth': '850',
                         'pageHeight': '1100',
                         'math': '0',
                         'shadow': '0'},
              'cell0':  {'id': '0'},
              'cell1':  {'id': '1',
                         'parent': '0'}}
      return data

   def buildXML(self, vpcdata, pagedata):
      self.elements.buildXML(vpcdata, pagedata)

   def dumpXML(self, file, folder):
      self.elements.dumpXML(file, folder)

   def resetXML(self):
      self.data = {'header': {'type': 'device',
                         'compressed': 'false'}}
      self.elements.resetXML(self.data)
