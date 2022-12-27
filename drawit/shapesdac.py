# @file shapesdac.py
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

from .typesdac import Types

class Shapes:
   common = None
   types = None

   def __init__(self, common):
      self.common = common
      self.types = Types(common)

   def buildShape(self, id, attributes, x, y, width, height, meta):
      node = self.types.buildNode(id, attributes, x, y, width, height, meta)
      return node

   def buildLink(self, label, source, target, meta):
       return self.types.buildLink(label, source, target, meta)

   def buildDoubleArrow(self, label, source, target, meta):
       return self.types.buildSolidLinkDoubleArrow(label, source, target, meta)

   def buildSingleArrow(self, label, source, target, meta):
       return self.types.buildSolidLinkSingleArrow(label, source, target, meta)

   def buildXML(self, vpcdata, pagename):
      self.types.buildXML(vpcdata, self.types.buildPage(pagename))

   def dumpXML(self, file, folder):
      self.types.dumpXML(file, folder)

   def resetXML(self):
      self.types.resetXML()
