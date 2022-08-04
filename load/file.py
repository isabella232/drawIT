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

import os
import sys
import json
import yaml
import requests
import urllib3
#import logging
from zipfile import ZipFile

from common.options import Options
from common.utils import *

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
   options = None

   def __init__(self, options):
      self.types = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.options = options
      return

   def loadJSON(self):
      stream = open(self.options.getInputFile(), 'r', encoding='utf-8-sig')
      self.data = json.loads(stream.read())
      if not 'vpcs' in self.data:
         printerror(invalidmessage % ("No VPCs were found", self.options.getInputFile()))
         sys.exit()
      elif not 'subnets' in self.data:
         printerror(invalidmessage % ("No Subnets were found", self.options.getInputFile()))
         sys.exit()

      if self.data != None:
         self.normalizeData()

      return

   def loadYAML(self):
      stream = open(self.options.getInputFile(), 'r')
      self.data = yaml.load(stream, Loader=yaml.FullLoader)
      if not 'vpcs' in self.data:
         printerror(invalidmessage % ("No VPCs were found", self.options.getInputFile()))
         sys.exit()
      elif not 'subnets' in self.data:
         printerror(invalidmessage % ("No Subnets were found", self.options.getInputFile()))
         sys.exit()

      if self.data != None:
         self.normalizeData()

      return

   def normalizeData(self):
      self.vpcs = pd.json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else pd.json_normalize({}))
      self.subnets = pd.json_normalize(self.data['subnets'] if ('subnets' in self.data) else pd.json_normalize({}))
      self.instances = pd.json_normalize(self.data['instances'] if ('instances' in self.data) else pd.json_normalize({}))
      #self.networkInterfaces = pd.json_normalize(self.data['networkInterfaces'] if ('networkInterfaces' in self.data) else pd.json_normalize({}))
      self.publicGateways = pd.json_normalize(self.data['publicGateways'] if ('publicGateways' in self.data) else pd.json_normalize({}))
      self.floatingIPs = pd.json_normalize(self.data['floatingIPs'] if ('floatingIPs' in self.data) else pd.json_normalize({}))
      self.vpnGateways = pd.json_normalize(self.data['vpnGateways'] if ('vpnGateways' in self.data) else pd.json_normalize({}))
      self.vpnConnections = pd.json_normalize(self.data['vpnConnections'] if ('vpnConnections' in self.data) else pd.json_normalize({}))
      self.loadBalancers = pd.json_normalize(self.data['loadBalancers'] if ('loadBalancers' in self.data) else pd.json_normalize({}))
      self.loadBalancerListeners = pd.json_normalize(self.data['loadBalancerListeners'] if ('loadBalancerListeners' in self.data) else pd.json_normalize({}))
      self.loadBalancerPools = pd.json_normalize(self.data['loadBalancerPools'] if ('loadBalancerPools' in self.data) else pd.json_normalize({}))
      self.loadBalancerMembers = pd.json_normalize(self.data['loadBalancerMembers'] if ('loadBalancerMembers' in self.data) else pd.json_normalize({}))
      self.volumes = pd.json_normalize(self.data['volumes'] if ('volumes' in self.data) else pd.json_normalize({}))
      self.networkACLs = pd.json_normalize(self.data['networkACLs'] if ('networkACLs' in self.data) else pd.json_normalize({}))
      self.securityGroups = pd.json_normalize(self.data['securityGroups'] if ('securityGroups' in self.data) else pd.json_normalize({}))
      self.keys = pd.json_normalize(self.data['keys'] if ('keys' in self.data) else pd.json_normalize({}))

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
                  #   #         normalizedmember = pd.json_normalize(lbmember)

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

      loadBalancerListeners =  pd.json_normalize(listenerdata)
      loadBalancerPools =  pd.json_normalize(pooldata)
      loadBalancerMembers =  pd.json_normalize(memberdata)

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
      return findrow(self.options, self.inputInstances, 'id', id)

   def getSubnet(self, id):
      return findrow(self.options, self.inputSubnets, 'id', id)

   def getVPC(self, id):
      return findrow(self.options, self.inputVPCs, 'id', id)

   def getFloatingIP(self, id):
      return findrow(self.options, self.inputFloatingIPs, 'target.id', id)

   def getPublicGateway(self, id):
      return findrow(self.options, self.InputPublicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.user.isInputRIAS() == 'rias':
         return findrow(self.options, self.inputVPNGateways, 'subnet.id', id)
      else:
         return findrow(self.options, self.inputVPNGateways, 'networkId', id)
