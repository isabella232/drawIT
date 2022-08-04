# @file analyze.py
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

from common.options import Options
from common.utils import *

class Analyze:
   instancesTable = {}
   subnetsTable = {}
   vpcsTable = {} # vpcids
   regionsTable = {} # vpcids
   zonesTable = {} # subnetids
   options = None

   def __init__(self, options):
      self.options = options
      return

   def analyzeData(self, data):
      # Add subnets to subnetsTable including empty subnets.
      subnets = data.getSubnets()
      for subnetindex, subnetframe in subnets.iterrows():
         subnetid = subnetframe['id']
         self.subnetsTable[subnetid] = []

      # Add instances to subnetsTable in each nic.
      instances = data.getInstances()
      if not instances.empty:
         for instanceindex, instanceframe in instances.iterrows():
            instancename = instanceframe['name']
            instanceid = instanceframe['id']
            #vpcname = instanceframe['vpcName']
            #vpcid = instanceframe['vpcId']
            vpcname = instanceframe['vpc.name'] if self.options.isInputRIAS() else instanceframe['vpcName']
            vpcid = instanceframe['vpc.id'] if self.options.isInputRIAS() else instanceframe['vpcId']
            #regionname = instanceframe['region']
            #zonename = instanceframe['availabilityZone']
            zonename = instanceframe['zone.name'] if self.options.isInputRIAS() else instanceframe['availabilityZone']
            regionname = zonename[:len(zonename) - 2] if self.options.isInputRIAS() else instanceframe['availabilityZone']

            #nics = instanceframe['networkInterfaces']
            nics = instanceframe['network_interfaces'] if self.options.isInputRIAS() else instanceframe['networkInterfaces']
            if nics:
               for nicframe in nics:
                  nicname = nicframe['name']
                  nicid = nicframe['id']
             
                  nicsubnetid = nicframe['subnet']['id'] if self.options.isInputRIAS() else nicframe['networkId']
                  if nicsubnetid in self.subnetsTable:
                     self.subnetsTable[nicsubnetid].append(instanceframe)
                  else:
                     printerror(invalidsubnetreferencemessage % nicsubnetid)
                     continue

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

         # Add subnets to zones.
         zonekey = subnetvpcid + ':' + subnetzonename
         if zonekey in self.zonesTable:
            if subnetid not in self.zonesTable[zonekey]:
               self.zonesTable[zonekey].append(subnetid)
         else:
            self.zonesTable[zonekey] = [subnetid]

         # Add zones to vpcsTable.
         zonekey = subnetvpcid + ':' + subnetzonename
         if subnetvpcid in self.vpcsTable:
            if zonekey not in self.vpcsTable[subnetvpcid]:
               self.vpcsTable[subnetvpcid].append(zonekey)
         else:
            self.vpcsTable[subnetvpcid] = [zonekey]

         # Add vpcs to regionsTable.
         if subnetregion in self.regionsTable:
            if subnetvpcid not in self.regionsTable[subnetregion]:
               self.regionsTable[subnetregion].append(subnetvpcid)
         else:
            self.regionsTable[subnetregion] = [subnetvpcid]

      return

   def getInstancesTable(self):
      return self.instancesTable

   def getSubnetsTable(self):
      return self.subnetsTable

   def getVPCsTable(self):
      return self.vpcsTable

   def getRegionsTable(self):
      return self.regionsTable

   def getZonesTable(self):
      return self.zonesTable
