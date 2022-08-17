# @file shapes.py
#
# Copyright IBM Corporation 2022
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

from build.types import Types
from common.utils import *

class Shapes:
   common = None
   types = None

   def __init__(self, common):
      self.common = common
      self.types = Types(common)

   # Groups

   def buildPublicNetwork(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('publicNetwork', self.common.compress(name), '1', name, subname, '', x, y, width, height) 
      return node

   def buildEnterpriseNetwork(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('enterpriseNetwork', self.common.compress(name), '1', name, subname, '', x, y, width, height) 
      return node

   def buildCloud(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('cloud', self.common.compress(name), '1', name, subname, '', x, y, width, height)
      return node

   def buildRegion(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('region', self.common.compress(id), self.common.compress(parentid), name, '', '', x, y, width, height) 
      return node

   def buildVPC(self, id, parentid, name, subname, x, y, width, height):
    node = self.types.buildNode('vpc', self.common.compress(id), self.common.compress(parentid), name, '', '', x, y, width, height)
    return node

   def buildZone(self, id, parentid, name, subname, x, y, width, height):
      zonename = name.split(':')[1]
      shapename = 'Availability Zone ' + zonename[-1]
      node = self.types.buildNode('zone', self.common.compress(id), self.common.compress(parentid), zonename, subname, '', x, y, width, height)
      return node

   def buildSubnet(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('subnet', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   # Expanded Icons

   def buildInstanceExpanded(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceExpandedStack(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastionExpanded(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceBastionExpanded', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastionExpandedStack(self, id, parentid, name, subname, x, y, width, height):
       node = self.types.buildNode('instanceBastionExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
       return node

    # Icons

   def buildInstance(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instance', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastion(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceBastion', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildFloatingIP(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('floatingIP', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildInternet(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('internet', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildLoadBalancer(self, id, parentid, name, subname, x, y, width, height):
      shapename = 'Load Balancer'
      node = self.types.buildNode('loadBalancer', self.common.compress(id), self.common.compress(parentid), shapename, name + '<br>' + subname, '', x, y, width, height) 
      return node

   def buildPublicGateway(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('publicGateway', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildRouter(self, id, parentid, name, subname, x, y, width, height):
      shapename = 'VPC Router'
      node = self.types.buildNode('router', self.common.compress(id), self.common.compress(parentid), shapename, name + '<br>' + subname, '', x, y, width, height) 
      return node

   def buildUser(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('user', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildVPNConnection(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('vpnConnection', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildVPNGateway(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('vpnGateway', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemOS(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('operatingSystem', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileBalanced(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileBalanced', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileCompute(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileCompute', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileMemory(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileMemory', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemBlockStorage(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('blockStorage', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildText(self, id, parentid, name, subname, text, x, y, width, height):
      text = self.common.truncateText(text, 35, '&lt;br&gt;');
      value = self.types.buildValue(self.common.compress(id), self.common.compress(parentid), name, parent, subname, text, x, y, width, height) 
      return value

   def buildLink(self, label, source, target):
       return self.types.buildLink(label, source, target)

   def buildDoubleArrow(self, label, source, target):
       return self.types.buildSolidLinkDoubleArrow(label, source, target)

   def buildSingleArrow(self, label, source, target):
       return self.types.buildSolidLinkSingleArrow(label, source, target)

   def buildXML(self, vpcdata, pagename):
      self.types.buildXML(vpcdata, self.types.buildPage(pagename))

   def dumpXML(self, file, folder):
      self.types.dumpXML(file, folder)

   def resetXML(self):
      self.types.resetXML()
