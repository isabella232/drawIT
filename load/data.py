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

from load.file import File
from load.rias import RIAS
from common.options import Options
from common.utils import *

class Data:
   instancesTable = {} # Table of instances ordered by subnet that shows instances within each subnet.
   nicsTable = {}      # Table of nics ordered by subnet+instance that shows nics for same instance in different subnets.
   vpcsTable = {}      # Table of zones ordered by vpc that shows zones with each vpc.
   regionsTable = {}   # Table of vpcs ordered by region that shows vpcs within each region.
   zonesTable = {}     # Table of subnets ordered by vpc+zone that shows subnets within each zone.

   data = None
   options = None

   def __init__(self, options):
      self.options = options
      if self.options.isInputRIAS():
         self.data = RIAS(options)
      else:
         self.data = File(options)
      return

   def loadData(self):
      normalizeddata = None
      if self.options.isInputRIAS():
         self.data.loadRIAS()
      elif self.options.isInputJSON():
         self.data.loadJSON()
      else:
         self.data.loadYAML()
      self.analyzeData()
      return

   def analyzeData(self):
      # Create empty instancesTable.
      subnets = self.data.getSubnets()
      if not subnets.empty:
         for subnetindex, subnetframe in subnets.iterrows():
            subnetid = subnetframe['id']
            self.instancesTable[subnetid] = []

      # Add instances to instancesTable ordered by subnetid, nics to nicsTable ordered by subnetid+instanceid..
      instances = self.data.getInstances()
      if not instances.empty:
         for instanceindex, instanceframe in instances.iterrows():
            instanceid = instanceframe['id']
            #instancename = instanceframe['name']
            #vpcname = instanceframe['vpc.name'] if self.options.isInputRIAS() else instanceframe['vpcName']
            #vpcid = instanceframe['vpc.id'] if self.options.isInputRIAS() else instanceframe['vpcId']
            #zonename = instanceframe['zone.name'] if self.options.isInputRIAS() else instanceframe['availabilityZone']
            #regionname = zonename[:len(zonename) - 2] if self.options.isInputRIAS() else instanceframe['availabilityZone']

            addedInstance = False
            nics = instanceframe['network_interfaces'] if self.options.isInputRIAS() else instanceframe['networkInterfaces']
            if nics:
               for nicframe in nics:
                  #nicname = nicframe['name']
                  #nicid = nicframe['id']
                  nicsubnetid = nicframe['subnet']['id'] if self.options.isInputRIAS() else nicframe['networkId']

                  if nicsubnetid in self.instancesTable:
                     if addedInstance == False:
                        self.instancesTable[nicsubnetid].append(instanceframe)
                        addedInstance = True
                  else:
                     printerror(invalidsubnetreferencemessage % nicsubnetid)
                     continue

                  dualid = nicsubnetid + ':' + instanceid
                  if dualid in self.nicsTable:
                     self.nicsTable[dualid].append(nicframe)
                  else:
                     self.nicsTable[dualid] = [nicframe]

      # Add subnets to zonesTable, zones to vpcsTable, and vpcs to regionsTable.
      for subnetindex, subnetframe in subnets.iterrows():
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         if subnetzonename == None:
            printerror(invalidzonereferencemessage % subnetname)
            continue

         lastindex = subnetzonename.rfind('-')
         subnetregion = subnetzonename[0:lastindex]
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']

         # Add subnets to zonesTable ordered by vpcid+zonename.
         zonekey = subnetvpcid + ':' + subnetzonename
         if zonekey in self.zonesTable:
            if subnetid not in self.zonesTable[zonekey]:
               self.zonesTable[zonekey].append(subnetid)
         else:
            self.zonesTable[zonekey] = [subnetid]

         # Add zones to vpcsTable ordered by vpcid.
         #zonekey = subnetvpcid +  subnetzonename
         if subnetvpcid in self.vpcsTable:
            if zonekey not in self.vpcsTable[subnetvpcid]:
               self.vpcsTable[subnetvpcid].append(zonekey)
         else:
            self.vpcsTable[subnetvpcid] = [zonekey]

         # Add vpcs to regionsTable ordered by region.
         if subnetregion in self.regionsTable:
            if subnetvpcid not in self.regionsTable[subnetregion]:
               self.regionsTable[subnetregion].append(subnetvpcid)
         else:
            self.regionsTable[subnetregion] = [subnetvpcid]

      return

   def findRow(self, user, dictionarylist, columnname, columnvalue):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
            if dictionary[columnname] == columnvalue:
               return dictionary
      return {}

   def getInstancesTable(self, subnetid):
      return self.instancesTable[subnetid]

   def getNICsTable(self, subnetid, instanceid):
       return self.nicsTable[subnetid + ':' + instanceid]

   def getVPCsTable(self):
      return self.vpcsTable

   def getRegionsTable(self):
      return self.regionsTable

   def getZonesTable(self):
      return self.zonesTable

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
      return self.findRow(self.options, self.data.getInstances(), 'id', id)

   def getSubnet(self, id):
      return self.findRow(self.options, self.data.getSubnets(), 'id', id)

   def getVPC(self, id):
      return self.findRow(self.options, self.data.getVPCs(), 'id', id)

   def getFloatingIP(self, id):
      return self.findRow(self.options, self.data.getFloatingIPs(), 'target.id', id)

   def getPublicGateway(self, id):
      return self.findRow(self.options, self.data.getPublicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.options.isInputRIAS():
         return self.findRow(self.options, self.data.getVPNGateways(), 'subnet.id', id)
      else:
         return self.findRow(self.options, self.data.getVPNGateways(), 'networkId', id)
