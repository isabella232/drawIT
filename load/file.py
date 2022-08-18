# @file file.py
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

from json import loads as json_load
from yaml import load as yaml_load
from pandas import json_normalize

from common.common import Common

class File:
   floatingIPs = {}
   instances = {}
   keys = {}
   networkInterfaces = {}
   loadBalancers = {}
   loadBalancerListeners = {}
   loadBalancerPools = {}
   loadBalancerMembers = {}
   networkACLs = {}
   publicGateways = {}
   securityGroups = {}
   subnets = {}
   volumes = {}
   vpcs = {}
   vpnGateways = {}
   vpnConnections = {}
   data = {}
   types = []
   common = None

   def __init__(self, common):
      #self.types = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.types = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips']
      self.common = common
      return

   def loadJSON(self):
      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      self.data = json_load(stream.read())
      if not 'vpcs' in self.data:
         self.common.printMissingVPCs(self.common.getInputFile())
         sys.exit()
      elif not 'subnets' in self.data:
         self.common.printMissingSubnets(self.common.getInputFile())
         sys.exit()

      if self.data != None:
         self.normalizeData()

      return

   def loadYAML(self):
      stream = open(self.common.getInputFile(), 'r')
      self.data = yaml_load(stream, Loader=yaml.FullLoader)
      if not 'vpcs' in self.data:
         self.common.printMissingVPCs(self.common.getInputFile())
         sys.exit()
      elif not 'subnets' in self.data:
         self.common.printMissingSubnets(self.common.getInputFile())
         sys.exit()

      if self.data != None:
         self.normalizeData()

      return

   def normalizeData(self):
      self.vpcs = json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else json_normalize({}))
      self.subnets = json_normalize(self.data['subnets'] if ('subnets' in self.data) else json_normalize({}))
      self.instances = json_normalize(self.data['instances'] if ('instances' in self.data) else json_normalize({}))
      #self.networkInterfaces = json_normalize(self.data['networkInterfaces'] if ('networkInterfaces' in self.data) else json_normalize({}))
      self.publicGateways = json_normalize(self.data['publicGateways'] if ('publicGateways' in self.data) else json_normalize({}))
      self.floatingIPs = json_normalize(self.data['floatingIPs'] if ('floatingIPs' in self.data) else json_normalize({}))
      self.vpnGateways = json_normalize(self.data['vpnGateways'] if ('vpnGateways' in self.data) else json_normalize({}))
      self.vpnConnections = json_normalize(self.data['vpnConnections'] if ('vpnConnections' in self.data) else json_normalize({}))
      self.loadBalancers = json_normalize(self.data['loadBalancers'] if ('loadBalancers' in self.data) else json_normalize({}))
      self.loadBalancerListeners = json_normalize(self.data['loadBalancerListeners'] if ('loadBalancerListeners' in self.data) else json_normalize({}))
      self.loadBalancerPools = json_normalize(self.data['loadBalancerPools'] if ('loadBalancerPools' in self.data) else json_normalize({}))
      self.loadBalancerMembers = json_normalize(self.data['loadBalancerMembers'] if ('loadBalancerMembers' in self.data) else json_normalize({}))
      self.volumes = json_normalize(self.data['volumes'] if ('volumes' in self.data) else json_normalize({}))
      self.networkACLs = json_normalize(self.data['networkACLs'] if ('networkACLs' in self.data) else json_normalize({}))
      self.securityGroups = json_normalize(self.data['securityGroups'] if ('securityGroups' in self.data) else json_normalize({}))
      self.keys = json_normalize(self.data['keys'] if ('keys' in self.data) else json_normalize({}))

      listenerdata = []
      pooldata = []
      memberdata = []

      if not self.loadBalancers.empty:
         lbdata = self.loadBalancers
         for lbindex, lb in lbdata.iterrows():
            lbid = lb['id']
            lbname = lb['name']
            lblisteners = lb['listeners']
            lbpools = lb['pools']

            if lbpools:
               for lbpool in lbpools:
                  lbpoolid = lbpool['id']
                  lbpoolname = lbpool['name']

                  extended = lbpool
                  extended['lbid'] = lbid
                  pooldata.append(extended)

                  lbpoolid = extended['lbid']

                  poolmemberdata = []

                  lbmembers = lbpool['members']
                  if lbmembers:
                     for lbmember in lbmembers:
                        if lbmember:
                           if lbmember['health'] == 'ok':
                              #print(lbmember)
                              #extended = {'id': lbid, "members": [ lbmember ]}
                              poolmemberdata.append(lbmember)
  
                              #for lbmember in lbmemberarray:

                              # vpcs.rename(
                              # columns={'is_public': 'isPublic'}, inplace=True)
  
                              #lbmemberid = lbmember['id']
 
                              #print(lbmemberarray)
                              #extended = lbmember
                              #extended['id'] = lbid
                              #extended['lbpoolid'] = lbpoolid
                              #memberdata.append(extended)

                  if poolmemberdata:
                     extended = {'id': lbid, "members": [ poolmemberdata ] }
                     memberdata.append(extended)

                  #if len(lbmembers) > 0 and lbmembers[0] != None:
                  #   # TODO: Remove 0
                  #   lbmembers = [ lbmembers[0] ]
                  #   #print(lbmembers)
                  #   #print(lbmembers)
                  #   extended['id'] = lbid
                  #   #extended['poolid'] = lbpoolid
                  #   memberdata.append(extended)

                  #   #for lbmemberarray in lbmembers:
                  #   #   if lbmemberarray:
                  #   #      for lbmember in lbmemberarray:
                  #   #         normalizedmember = json_normalize(lbmember)

                  #   #         vpcs.rename(
                  #   #            columns={'is_public': 'isPublic'}, inplace=True)

                  #   #         lbmemberid = normalizedmember['id']

                  #   #         extended = normalizedmember
                  #   #         extended['lbid'] = lbid
                  #   #         extended['lbpoolid'] = lbpoolid
                  #   #         memberdata.append(extended)

            if lblisteners:
               for lblistener in lblisteners:
                  lblistenerid = lblistener['id']

                  extended = lblistener
                  extended['lbid'] = lbid
                  listenerdata.append(extended)

      loadBalancerListeners =  json_normalize(listenerdata)
      loadBalancerPools =  json_normalize(pooldata)
      loadBalancerMembers =  json_normalize(memberdata)

      if not self.vpcs.empty:
         self.vpcs.rename(
            columns={'availabilityZone': 'zone.name'}, inplace=True)

      if not self.subnets.empty:
         self.subnets.rename(
            columns={'availabilityZone': 'zone.name',
                     'subnet': 'ipv4_cidr_block',
                     'publicGateway.id': 'public_gateway.id',
                     'vpcId': 'vpc.id'}, inplace=True)

         self.subnets['vpc.name'] = self.subnets['vpc.id'] 

      if not self.instances.empty:
         self.instances.rename(
            columns={'memoryGb': 'memory',
                     'bandwidthMb': 'bandwidth',
                     'cpuCount': 'vcpu.count',
                     'profile': 'profile.name',
                     'osVersion': 'image.name'}, inplace=True)


      #networkInterfaces = instances['networkInterfaces']
      #nicframe = pd.DataFrame.from_dict(networkInterfaces)
      #if not nicframe.empty:
      #   nicframe.rename(
      #      columns={'ip': 'primary_ip.address',
      #               'networkId': 'subnet.id',
      #               'instanceId': 'instance.id'}, inplace=True)
      #instances['networkInterfaces'] = nicframe

      #if not networkInterfaces.empty:
      #   networkInterfaces.rename(
      #      #columns={'ip': 'primary_ipv4_address',
      #      columns={'ip': 'primary_ip.address',
      #               'networkId': 'subnet.id',
      #               'instanceId': 'instance.id'}, inplace=True)

      if not self.vpnGateways.empty:
         self.vpnGateways.rename(
            columns={'floatingIP': 'floating_ip.address'}, inplace=True)

      return

   def getFloatingIPs(self):
      return self.floatingIPs

   def getInstances(self):
      return self.instances

   def getKeys(self):
      return self.keys

   def getNetworkInterfaces(self):
      return self.networkInterfaces

   def getLoadBalancers(self):
      return self.loadBalancers

   def getLoadBalancerListeners(self):
      return self.loadBalancerListeners

   def getLoadBalancerPools(self):
      return self.loadBalancerPools

   def getLoadBalancerMembers(self):
      return self.loadBalancerMembers

   def getNetworkACLs(self):
      return self.networkACLs

   def getPublicGateways(self):
      return self.publicGateways

   def getSecurityGroups(self):
      return self.securityGroups

   def getSubnets(self):
      return self.subnets

   def getVolumes(self):
      return self.volumes

   def getVPCs(self):
      return self.vpcs

   def getVPNGateways(self):
      return self.vpnGateways

   def getVPNConnections(self):
      return self.vpnConnections

   def getInstance(self, id):
      return findrow(self.common, self.inputInstances, 'id', id)

   def getSubnet(self, id):
      return findrow(self.common, self.inputSubnets, 'id', id)

   def getVPC(self, id):
      return findrow(self.common, self.inputVPCs, 'id', id)

   def getFloatingIP(self, id):
      return findrow(self.common, self.inputFloatingIPs, 'target.id', id)

   def getPublicGateway(self, id):
      return findrow(self.common, self.InputPublicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.user.isInputRIAS() == 'rias':
         return findrow(self.common, self.inputVPNGateways, 'subnet.id', id)
      else:
         return findrow(self.common, self.inputVPNGateways, 'networkId', id)
