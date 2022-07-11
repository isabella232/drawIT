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
      nicstable = {}
      regionstable = {}
      vpcstable = {}
      zonestable = {}

      self.inputdata = userdata['inputdata']
      self.setupdata = userdata['setupdata']

      # For each NIC add nicstable[subnetid] = nicframe.
      nics = self.inputdata['networkInterfaces']
      if not nics.empty:
         for nicindex, nicframe in nics.iterrows():
            nicname = nicframe['name']
            nicid = nicframe['id']
            nicip = nicframe['primary_ip.address']
            nicsubnetid = nicframe['subnet.id']
            nicinstance = nicframe['instance.id']
            # TODO: Region not in nicframe
            # nicregion = nicframe['region']

            # Create nicstable[subnetid] = nicframe
            if nicsubnetid in nicstable:
               nicstable[nicsubnetid].append(nicframe)
            else:
               nicstable[nicsubnetid] = [nicframe]

      # Include empty subnets.
      subnetdf = self.inputdata['subnets']
      for subnetindex, subnetframe in subnetdf.iterrows():
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

         # Create nicstable[subnetid] = empty nicframe
         nicframe = pd.DataFrame()
         if not subnetid in nicstable:
            nicstable[subnetid] = [nicframe]
         #if subnetid in nicstable:
         #   nicstable[subnetid].append(nicframe)
         #else:
         #   nicstable[subnetid] = [nicframe]

      # For each nic in nicstable, 
      # get subnetframe, get zone.name from subnet, get regionname from zone.name, 
      # add zonestable[vpcid:zonename] = subnetid
      # add vpcstable[vpcid:zonename] = zonekey
      # add regionstable[regionname] = vpcid

      for subnetid in nicstable:
         subnetframe = findrow(userdata, self.inputdata['subnets'], 'id', subnetid)
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

         # Add zones to vpctable.
         zonekey = subnetvpcid + ':' + subnetzonename
         vpcstable = self.setupdata['vpcs']
         if subnetvpcid in vpcstable:
            if zonekey not in vpcstable[subnetvpcid]:
               vpcstable[subnetvpcid].append(zonekey)
         else:
            vpcstable[subnetvpcid] = [zonekey]

         # Add vpcs to regiontable.
         regionstable = self.setupdata['regions']
         if subnetregion in regionstable:
            if subnetvpcid not in regionstable[subnetregion]:
               regionstable[subnetregion].append(subnetvpcid)
         else:
            regionstable[subnetregion] = [subnetvpcid]

      self.setupdata['nics'] = nicstable
      self.setupdata['regions'] = regionstable
      self.setupdata['vpcs'] = vpcstable
      self.setupdata['zones'] = zonestable

      return self.setupdata
