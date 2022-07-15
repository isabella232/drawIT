# @file rias.py
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

class RIAS:
   def __init__(self, user):
      #self.riasdatatypes = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.riasdatatypes = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways']
      self.outputfolder = user['outputfolder']
      self.region = user['region']
      self.apikey = user['apikey']
      self.accountid = user['accountid']

   def gettoken(self, accountID, apiKey):
      endpoint = 'https://iam.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
         }
      data = {
         'grant_type': 'urn:ibm:params:oauth:grant-type:apikey', 
         'apikey': apiKey
      }
      urllib3.disable_warnings()
      response = requests.post(url=endpoint + "/identity/token", headers=headers, data=data, verify=False)
      token_dict = json.loads(response.text)
      if 'errorCode' in token_dict:
         printerror(invalidmessage % (token_dict['errorCode'], token_dict['errorMessage'])) 
         sys.exit()
      token = token_dict["token_type"] + " " + token_dict["access_token"]
      return token

   def getriasdata(self, token, accountID, group):
      #version = '2022-03-15'
      version = '2022-07-05'
      endpoint = 'https://' + self.region + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         if group == 'vpn_gateways' or group == 'load_balancers':
            # Exit for now as causing error with other accounts:
            #    not_authorized: The request is not authorized. href=https://us-south.iaas.cloud.ibm.com/v1/vpn_gateways
            return {}
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': '2'
      }
      request = endpoint + "/v1/" + group
      response = requests.get(url=request, headers=headers, params=params, verify=False)
      rawdata = json.loads(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         printerror(invalidmessage % (error['code'], error['message'] + ' href=' + request)) 
         sys.exit()
      elif group == "vpcs" and rawdata['total_count'] == 0:
         printerror(invalidmessage % ("No VPCs were found", 'href=' + request)) 
         sys.exit()
      elif group == "subnets" and rawdata['total_count'] == 0:
         printerror(invalidmessage % ("No Subnets were found", 'href=' + request)) 
         sys.exit()
      data = rawdata[group]
      #if group == "vpcs":
      #   for vpc in data:
      #      print(vpc["name"])
      return data

   def getriassubdata(self, token, accountID, id, group, subgroup):
      #version = '2022-05-31'
      version = '2022-07-05'
      endpoint = 'https://' + self.region + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': 2
      }
      request = endpoint + "/v1/" + group + '/' + id + '/' + subgroup
      response = requests.get(url=request, headers=headers, params=params, verify=False)
      rawdata = json.loads(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         printerror(invalidmessage % (error['code'], error['message'] + ' href=' + request)) 
         sys.exit()
      data = rawdata[group]
      return data
      #return rawdata

   def getriassubdata2(self, token, accountID, id, group, subgroup, id2, subgroup2):
      #version = '2022-05-31'
      version = '2022-07-05'
      endpoint = 'https://' + self.region + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': '2'
      }
      request = endpoint + "/v1/" + group + '/' + id + '/' + subgroup + '/' + id2 + '/' + subgroup2
      response = requests.get(url=request, headers=headers, params=params, verify=False)
      rawdata = json.loads(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         printerror(invalidmessage % (error['code'], error['message'] + ' href=' + request)) 
         sys.exit()
      data = rawdata[group]
      return data
      #return rawdata

   def loadRIAS(self):
      data = {}
      listenerdata = []
      pooldata = []
      memberdata = []
      #nicdata = []
      vpndata = []
      token = self.gettoken(self.accountid, self.apikey)
      #rawdata = getriasdata(userdata, token, accountid, 'vpcs')
      #data[datatype] = rawdata
      #return data
 
      for datatype in self.riasdatatypes:
         rawdata = self.getriasdata(token, self.accountid, datatype)
         data[datatype] = rawdata
         #if datatype == 'instances':
         #   instancedata = rawdata
         #   for instance in instancedata:
         #      id = instance['id']
         #      rawdata = self.getriassubdata(token, self.accountid, id, datatype, 'network_interfaces')
         #      nics = rawdata['network_interfaces']
         #      extended = {}
         #      for nic in nics:
         #         extended = nic
         #         extended['instance.id'] = id
         #         nicdata.append(extended)

         if datatype == 'load_balancers':
            lbdata = rawdata
            for lb in lbdata:
               id = lb['id']
               rawdata = self.getriassubdata(token, self.accountid, id, datatype, 'listeners')
               listeners = rawdata['listeners']
               listenerdict = {} 
               lblistenerdata = []
               extended = {}
               for listener in listeners:
                  listenerid = listener['id']

                  extended = listener
                  extended['lbid'] = id
                  lblistenerdata.append(extended)

               listenerdict = {'id': id, 'listeners': lblistenerdata}
               listenerdata.append(listenerdict)

               rawdata = self.getriassubdata(token, self.accountid, id, datatype, 'pools')
               pools = rawdata['pools']
               pooldict = {} 
               memberdict = {} 
               lbpooldata = []
               lbmemberdata = []
               extended = {}
               for pool in pools:
                  poolid = pool['id']

                  extended = pool
                  extended['lbid'] = id
                  pooldata.append(extended)

                  rawdata = self.getriassubdata2(token, self.accountid, id, datatype, 'pools', poolid, 'members')
                  members = rawdata['members']
                  lbmemberdata.append(members)

               memberdict = {'id': id, 'members': lbmemberdata}
               memberdata.append(memberdict)

         #elif datatype == 'vpn_gateways':
         #   vpngatewaydata = rawdata
         #   for gateway in vpngatewaydata:
         #      id = gateway['id']
         #      rawdata = getriassubdata(token, accountid, id, datatype, 'connections')
         #      connections = rawdata['connections']
         #      extended = {}
         #      for connection in connections:
         #         extended = connection
         #         #extended['subnetId'] = id
         #         vpndata.append(extended)
         
      #data['network_interfaces'] = nicdata
      data['load_balancer_listeners'] = listenerdata
      data['load_balancer_pools'] = pooldata
      data['load_balancer_members'] = memberdata

      #data['vpnConnections'] = vpndata
  
      return data

   def normalizeData(self, data):
      vpcs = pd.json_normalize(data['vpcs'] if ('vpcs' in data) else pd.json_normalize({}))
      subnets = pd.json_normalize(data['subnets'] if ('subnets' in data) else pd.json_normalize({}))
      instances = pd.json_normalize(data['instances'] if ('instances' in data) else pd.json_normalize({}))
      #networkInterfaces = pd.json_normalize(data['network_interfaces'] if ('network_interfaces' in data) else pd.json_normalize({}))
      publicGateways = pd.json_normalize(data['public_gateways'] if ('public_gateways' in data) else pd.json_normalize({}))
      floatingIPs = pd.json_normalize(data['floating_ips'] if ('floating_ips' in data) else pd.json_normalize({}))
      vpnGateways = pd.json_normalize(data['vpn_gateways'] if ('vpn_gateways' in data) else pd.json_normalize({}))
      vpnConnections = pd.json_normalize({})
      loadBalancers = pd.json_normalize(data['load_balancers'] if ('load_balancers' in data) else pd.json_normalize({}))
      loadBalancerListeners = pd.json_normalize(data['load_balancer_listeners'] if ('load_balancer_listeners' in data) else pd.json_normalize({}))
      loadBalancerPools = pd.json_normalize(data['load_balancer_pools'] if ('load_balancer_pools' in data) else pd.json_normalize({}))
      loadBalancerMembers = pd.json_normalize(data['load_balancer_members'] if ('load_balancer_members' in data) else pd.json_normalize({}))
      volumes = pd.json_normalize({})
      networkACLs = pd.json_normalize({})
      securityGroups = pd.json_normalize({})
      keys = pd.json_normalize({})

      normalizeddata = {
         'vpcs': vpcs,
         'subnets': subnets,
         'instances': instances,
         #'networkInterfaces': networkInterfaces,
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
