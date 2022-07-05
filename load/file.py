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

from common.utils import *

class File:
   def __init__(self, user):
      self.inputfile = user['inputfile']
      self.outputfolder = user['outputfolder']
      self.yamldatatypes = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']

   def loadJSON(self):
      stream = open(self.inputfile, 'r', encoding='utf-8-sig')
      data = json.loads(stream.read())
      if not 'vpcs' in data:
         printerror(invalidmessage % ("No VPCs were found", self.inputfile))
         sys.exit()
      elif not 'subnets' in data:
         printerror(invalidmessage % ("No Subnets were found", self.inputfile))
         sys.exit()

      return data

   def loadYAML(self):
      stream = open(self.inputfile, 'r')
      data = yaml.load(stream, Loader=yaml.FullLoader)
      if not 'vpcs' in data:
         printerror(invalidmessage % ("No VPCs were found", inputfile))
         sys.exit()
      elif not 'subnets' in data:
         printerror(invalidmessage % ("No Subnets were found", inputfile))
         sys.exit()
      return data

   def normalizeData(self, data):
      vpcs = pd.json_normalize(data['vpcs'] if ('vpcs' in data) else pd.json_normalize({}))
      subnets = pd.json_normalize(data['subnets'] if ('subnets' in data) else pd.json_normalize({}))
      instances = pd.json_normalize(data['instances'] if ('instances' in data) else pd.json_normalize({}))
      networkInterfaces = pd.json_normalize(data['networkInterfaces'] if ('networkInterfaces' in data) else pd.json_normalize({}))
      publicGateways = pd.json_normalize(data['publicGateways'] if ('publicGateways' in data) else pd.json_normalize({}))
      floatingIPs = pd.json_normalize(data['floatingIPs'] if ('floatingIPs' in data) else pd.json_normalize({}))
      vpnGateways = pd.json_normalize(data['vpnGateways'] if ('vpnGateways' in data) else pd.json_normalize({}))
      vpnConnections = pd.json_normalize(data['vpnConnections'] if ('vpnConnections' in data) else pd.json_normalize({}))
      loadBalancers = pd.json_normalize(data['loadBalancers'] if ('loadBalancers' in data) else pd.json_normalize({}))
      loadBalancerListeners = pd.json_normalize(data['loadBalancerListeners'] if ('loadBalancerListeners' in data) else pd.json_normalize({}))
      loadBalancerPools = pd.json_normalize(data['loadBalancerPools'] if ('loadBalancerPools' in data) else pd.json_normalize({}))
      loadBalancerMembers = pd.json_normalize(data['loadBalancerMembers'] if ('loadBalancerMembers' in data) else pd.json_normalize({}))
      volumes = pd.json_normalize(data['volumes'] if ('volumes' in data) else pd.json_normalize({}))
      networkACLs = pd.json_normalize(data['networkACLs'] if ('networkACLs' in data) else pd.json_normalize({}))
      securityGroups = pd.json_normalize(data['securityGroups'] if ('securityGroups' in data) else pd.json_normalize({}))
      keys = pd.json_normalize(data['keys'] if ('keys' in data) else pd.json_normalize({}))

      listenerdata = []
      pooldata = []
      memberdata = []

      if not loadBalancers.empty:
         lbdata = loadBalancers
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

      if not vpcs.empty:
         vpcs.rename(
            columns={'availabilityZone': 'zone.name'}, inplace=True)

      if not subnets.empty:
         subnets.rename(
            columns={'availabilityZone': 'zone.name',
                     'subnet': 'ipv4_cidr_block',
                     'publicGateway.id': 'public_gateway.id',
                     'vpcId': 'vpc.id'}, inplace=True)

         subnets['vpc.name'] = subnets['vpc.id'] 

      if not instances.empty:
         instances.rename(
            columns={'memoryGb': 'memory',
                     'bandwidthMb': 'bandwidth',
                     'cpuCount': 'vcpu.count',
                     'profile': 'profile.name',
                     'osVersion': 'image.name'}, inplace=True)

      if not networkInterfaces.empty:
         networkInterfaces.rename(
            #columns={'ip': 'primary_ipv4_address',
            columns={'ip': 'primary_ip.address',
                     'networkId': 'subnet.id',
                     'instanceId': 'instance.id'}, inplace=True)

      if not vpnGateways.empty:
         vpnGateways.rename(
            columns={'floatingIP': 'floating_ip.address'}, inplace=True)

      normalizeddata = {
         'vpcs': vpcs,
         'subnets': subnets,
         'instances': instances,
         'networkInterfaces': networkInterfaces,
         'publicGateways': publicGateways,
         'floatingIPs': floatingIPs,
         'vpnGateways': vpnGateways,
         'vpnConnections': vpnConnections,
         'loadBalancers': loadBalancers,
         'loadBalancerListeners': loadBalancerListeners,
         'loadBalancerPools': loadBalancerPools,
         'loadBalancerMembers': loadBalancerMembers,
         'volumes': volumes,
         'networkACLs': networkACLs,
         'securityGroups': securityGroups,
         'keys': keys
      }

      return normalizeddata
