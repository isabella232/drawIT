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
   def __init__(self, user):
      self.user = user
      self.types = Types(user)

   # Groups

   def buildPublicNetwork(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('publicNetwork', compress(name), '1', name, subname, '', x, y, width, height) 
      return node

   def buildEnterpriseNetwork(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('enterpriseNetwork', compress(name), '1', name, subname, '', x, y, width, height) 
      return node

   def buildCloud(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('cloud', compress(name), '1', name, subname, '', x, y, width, height)
      return node

   def buildRegion(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('region', compress(id), compress(parentid), name, '', '', x, y, width, height) 
      return node

   def buildVPC(self, id, parentid, name, subname, x, y, width, height):
    node = self.types.buildNode('vpc', compress(id), compress(parentid), name, '', '', x, y, width, height)
    return node

   def buildZone(self, id, parentid, name, subname, x, y, width, height):
      zonename = name.split(':')[1]
      shapename = 'Availability Zone ' + zonename[-1]
      node = self.types.buildNode('zone', compress(id), compress(parentid), zonename, subname, '', x, y, width, height)
      return node

   def buildSubnet(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('subnet', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   # Expanded Icons

   def buildInstanceExpanded(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceExpandedStack', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceExpandedStack(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceExpandedStack', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastionExpanded(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceBastionExpanded', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastionExpandedStack(self, id, parentid, name, subname, x, y, width, height):
       node = self.types.buildNode('instanceBastionExpandedStack', compress(id), compress(parentid), name, subname, '', x, y, width, height)
       return node

    # Icons

   def buildInstance(self, id, parentd, name, subname, x, y, width, height):
      node = self.types.buildNode('instance', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildInstanceBastion(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('instanceBastion', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildFloatingIP(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('floatingIP', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildInternet(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('internet', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildLoadBalancer(self, id, parentid, name, subname, x, y, width, height):
      shapename = 'Load Balancer'
      node = self.types.buildNode('loadBalancer', compress(id), compress(parentid), shapename, name + '<br>' + subname, '', x, y, width, height) 
      return node

   def buildPublicGateway(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('publicGateway', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildRouter(self, id, parentid, name, subname, x, y, width, height):
      shapename = 'VPC Router'
      node = self.types.buildNode('router', compress(id), compress(parentid), shapename, name + '<br>' + subname, '', x, y, width, height) 
      return node

   def buildUser(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('user', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildVPNConnection(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('vpnConnection', compress(id), compress(parentid), name, subname, '', x, y, width, height)
      return node

   def buildVPNGateway(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('vpnGateway', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemOS(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('operatingSystem', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileBalanced(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileBalanced', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileCompute(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileCompute', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemProfileMemory(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('profileMemory', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildItemBlockStorage(self, id, parentid, name, subname, x, y, width, height):
      node = self.types.buildNode('blockStorage', compress(id), compress(parentid), name, subname, '', x, y, width, height) 
      return node

   def buildText(self, id, parentid, name, subname, text, x, y, width, height):
      text = truncateText(text, 35, '&lt;br&gt;');
      value = self.types.buildValue(compress(id), compress(parentid), name, parent, subname, text, x, y, width, height) 
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
