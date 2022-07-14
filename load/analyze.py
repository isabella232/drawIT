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

from common.utils import *

class Analyze:
   def __init__(self, user):
      self.inputtype = user['inputtype']
      self.inputdata = user['inputdata']
      self.setupdata = user['setupdata']

   def analyzeData(self):
      instancestable = {}
      subnetstable = {}
      zonestable = {} # subnetids
      vpcstable = {} # zoneids
      regionstable = {} # vpcids

      self.inputdata = userdata['inputdata']
      self.setupdata = userdata['setupdata']

      # Add subnets to subnetstable including empty subnets.
      subnets = self.inputdata['subnets']
      for subnetindex, subnetframe in subnets.iterrows():
         subnetid = subnetframe['id']
         subnetstable[subnetid] = []

      # Add instances to instancestable, add instances to subnetstable based on subnet in each nic.
      instances = self.inputdata['instances']
      if not instances.empty:
         for instanceindex, instanceframe in instances.iterrows():
            instancename = instanceframe['name']
            instanceid = instanceframe['id']
            vpcname = instanceframe['vpcName']
            vpcid = instanceframe['vpcId']
            regionname = instanceframe['region']
            zonename = instanceframe['availabilityZone']

            nics = instanceframe['networkInterfaces']
            if nics:
               for nicframe in nics:
                  nicname = nicframe['name']
                  nicid = nicframe['id']
                  nicip = 0
                  nicsubnetid = 0
                  nicinstance = 0
             
                  nicsubnetid = 0
                  if self.inputtype == 'rias':
                     nicsubnetid = nicframe['subnet.id']
                  else: # yaml
                     nicsubnetid = nicframe['networkId']
                  subnetstable[nicsubnetid].append(instanceframe)

      # Add subnets to zonestable, zones to vpcstable, and vpcs to regionstable.
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

         # Add subnets to zonetable.
         zonekey = subnetvpcid + ':' + subnetzonename
         zonestable = self.setupdata['zones']
         if zonekey in zonestable:
            if subnetid not in zonestable[zonekey]:
               zonestable[zonekey].append(subnetid)
         else:
            zonestable[zonekey] = [subnetid]

         # Add zones to vpcstable.
         zonekey = subnetvpcid + ':' + subnetzonename
         vpcstable = self.setupdata['vpcs']
         if subnetvpcid in vpcstable:
            if zonekey not in vpcstable[subnetvpcid]:
               vpcstable[subnetvpcid].append(zonekey)
         else:
            vpcstable[subnetvpcid] = [zonekey]

         # Add vpcs to regionstable.
         regionstable = self.setupdata['regions']
         if subnetregion in regionstable:
            if subnetvpcid not in regionstable[subnetregion]:
               regionstable[subnetregion].append(subnetvpcid)
         else:
            regionstable[subnetregion] = [subnetvpcid]

      self.setupdata['instances'] = instancestable
      self.setupdata['subnets'] = subnetstable
      self.setupdata['zones'] = zonestable
      self.setupdata['vpcs'] = vpcstable
      self.setupdata['regions'] = regionstable

      return self.setupdata
