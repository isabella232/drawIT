# @file data.py
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

from load.analyze import Analyze
from load.file import File
from load.rias import RIAS
from common.options import Options
from common.utils import *

class Data:
   analyze = None
   data = None
   options = None

   def __init__(self, options):
      self.options = options
      if self.options.isInputRIAS():
         self.data = RIAS(options)
      else:
         self.data = File(options)
      self.analyze = Analyze(options)
      return

   def loadData(self):
      normalizeddata = None
      if self.options.isInputRIAS():
         self.data.loadRIAS()
      elif self.options.isInputJSON():
         self.data.loadJSON()
      else:
         self.data.loadYAML()
      self.analyze.analyzeData(self.data)
      return

   def getInstancesTable(self):
      return self.analyze.getInstancesTable()

   def getSubnetsTable(self):
      return self.analyze.getSubnetsTable()

   def getVPCsTable(self):
      return self.analyze.getVPCsTable()

   def getRegionsTable(self):
      return self.analyze.getRegionsTable()

   def getZonesTable(self):
      return self.analyze.getZonesTable()

   def getFloatingIPs(self):
      return self.data.getFloatingIPs()

   def getInstances(self):
      return self.data.getInstances()

   def getKeys(self):
      return self.data.getKeys()

   def getNetworkInterfaces(self):
      return self.data.getNetworkInterfaces()

   def getLoadBalancers(self):
      return self.data.getLoadBalancers()

   def getLoadBalancerListeners(self):
      return self.data.getLoadBalancerListeners()

   def getLoadBalancerPools(self):
      return self.data.getLoadBalancerPools()

   def getLoadBalancerMembers(self):
      return self.data.getLoadBalancerMembers()

   def getNetworkACLs(self):
      return self.data.getNetworkACLs()

   def getPublicGateways(self):
      return self.data.getPublicGateways()

   def getSecurityGroups(self):
      return self.data.getSecurityGroups()

   def getSubnets(self):
      return self.data.getSubnets()

   def getVolumes(self):
      return self.data.getVolumes()

   def getVPCs(self):
      return self.data.getVPCs()

   def getVPNGateways(self):
      return self.data.getVPNGateways()

   def getVPNConnections(self):
      return self.data.getVPNConnections()

   def getInstance(self, id):
      return findrow(self.options, self.data.getInstances(), 'id', id)

   def getSubnet(self, id):
      return findrow(self.options, self.data.getSubnets(), 'id', id)

   def getVPC(self, id):
      return findrow(self.options, self.data.getVPCs(), 'id', id)

   def getFloatingIP(self, id):
      return findrow(self.options, self.data.getFloatingIPs(), 'target.id', id)

   def getPublicGateway(self, id):
      return findrow(self.options, self.data.getPublicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.options.isInputRIAS():
         return findrow(self.options, self.data.getVPNGateways(), 'subnet.id', id)
      else:
         return findrow(self.options, self.data.getVPNGateways(), 'networkId', id)
