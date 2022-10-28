# @file shapes.py
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

from diagram.types import Types

class Shapes:
   common = None
   types = None

   def __init__(self, common):
      self.common = common
      self.types = Types(common)

   # Groups

   def buildPublicNetwork(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('PublicNetwork', self.common.compress(name), '1', name, subname, '', x, y, width, height, meta) 
      return node

   def buildEnterpriseNetwork(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('EnterpriseNetwork', self.common.compress(name), '1', name, subname, '', x, y, width, height, meta) 
      return node

   def buildCloud(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Cloud', self.common.compress(name), '1', name, subname, '', x, y, width, height, meta)
      return node

   def buildRegion(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Region', self.common.compress(id), self.common.compress(parentid), name, '', '', x, y, width, height, meta) 
      return node

   def buildVPC(self, id, parentid, name, subname, x, y, width, height, meta):
    node = self.types.buildNode('VPC', self.common.compress(id), self.common.compress(parentid), name, '', '', x, y, width, height, meta)
    return node

   def buildZone(self, id, parentid, name, subname, x, y, width, height, meta):
      zonename = name.split(':')[1]
      shapename = 'Availability Zone ' + zonename[-1]
      node = self.types.buildNode('Zone', self.common.compress(id), self.common.compress(parentid), zonename, subname, '', x, y, width, height, meta)
      return node

   def buildSubnet(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Subnet', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildLocation(self, id, parentid, name, subname, type, x, y, width, height, meta):
      node = self.types.buildNode(type, self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   # Expanded Icons

   def buildInstanceExpanded(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('InstanceExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildInstanceExpandedStack(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('InstanceExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildInstanceBastionExpanded(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('InstanceBastionExpanded', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildInstanceBastionExpandedStack(self, id, parentid, name, subname, x, y, width, height, meta):
       node = self.types.buildNode('InstanceBastionExpandedStack', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
       return node

    # Icons

   def buildInstance(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Instance', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildInstanceBastion(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('InstanceBastion', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildIcon(self, id, parentid, name, subname, type, x, y, width, height, meta):
      node = self.types.buildNode(type, self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildFloatingIP(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('FloatingIP', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildInternet(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Internet', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildLoadBalancer(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('LoadBalancer', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildPublicGateway(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('PublicGateway', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildRouter(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('Router', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildUser(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('User', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildVPNConnection(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('VPNConnection', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta)
      return node

   def buildVPNGateway(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('VPNGateway', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildVPCEndpoint(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('VPE', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildItemOS(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('OperatingSystem', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildItemProfileBalanced(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('ProfileBalanced', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildItemProfileCompute(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('ProfileCompute', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildItemProfileMemory(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('ProfileMemory', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildItemBlockStorage(self, id, parentid, name, subname, x, y, width, height, meta):
      node = self.types.buildNode('BlockStorage', self.common.compress(id), self.common.compress(parentid), name, subname, '', x, y, width, height, meta) 
      return node

   def buildText(self, id, parentid, name, subname, text, x, y, width, height, meta):
      text = self.common.truncateText(text, 35, '&lt;br&gt;');
      value = self.types.buildValue(self.common.compress(id), self.common.compress(parentid), name, parent, subname, text, x, y, width, height, meta) 
      return value

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
