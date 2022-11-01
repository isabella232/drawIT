# @file icons.py
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

from diagram.constants import *

class Icons:
   iconDictionary = { 
      'Undefined': 	        
            {'icon': 'undefined', 'color': NETWORK_COLOR},
      'Collaborate': 	        
            {'icon': 'collaborate', 'color': NETWORK_COLOR},
      'Credentials': 	        
            {'icon': 'credentials', 'color': NETWORK_COLOR},
      'Devices': 	        
            {'icon': 'devices', 'color': NETWORK_COLOR},
      'Events': 	        
            {'icon': 'events', 'color': NETWORK_COLOR},
      'AuthorizationBoundary': 	        
            {'icon': 'flag', 'color': NETWORK_COLOR},
      'Cloud-prescribed': 	        
            {'icon': 'ibm-cloud', 'color': NETWORK_COLOR},
      'User':  	        
            {'icon': 'user', 'color': USER_COLOR}, 
      'Instance-logical': 	        
            {'icon': 'virtual-machine', 'color': NETWORK_COLOR},
      'VPC-logical':  	        
            {'icon': 'virtual-private-cloud', 'color': NETWORK_COLOR}, 
      'VPC-prescribed':  	        
            {'icon': 'virtual-private-cloud--alt', 'color': NETWORK_COLOR}, 
      'Region': 	        
            {'icon': 'location', 'color': NETWORK_COLOR},
      'Security': 	        
            {'icon': 'security', 'color': SECURITY_COLOR},
      'FingerprintRecognition': 	        
            {'icon': 'fingerprint-recognition', 'color': NETWORK_COLOR},
      'Network2':  	        
            {'icon': 'network--2', 'color': NETWORK_COLOR}, 
      'VPN': 	        
            {'icon': 'VPN', 'color': NETWORK_COLOR},
      'EdgeNode':  	        
            {'icon': 'edge-node', 'color': NETWORK_COLOR}, 
      'Group':  	        
            {'icon': 'group', 'color': NETWORK_COLOR}, 
      'Mobile':  	        
            {'icon': 'mobile', 'color': NETWORK_COLOR}, 
      'Policy':  	        
            {'icon': 'policy', 'color': SECURITY_COLOR}, 
      'Rule':  	        
            {'icon': 'rule', 'color': SECURITY_COLOR}, 
      'Terminal':  	        
            {'icon': 'terminal', 'color': NETWORK_COLOR}, 
      'ObjectStorage-prescribed':  	        
            {'icon': 'object-storage', 'color': STORAGE_COLOR}, 
      'Laptop':  	        
            {'icon': 'laptop', 'color': NETWORK_COLOR}, 
      'Tablet':  	        
            {'icon': 'tablet', 'color': NETWORK_COLOR}, 
      'Archive':  	        
            {'icon': 'archive', 'color': NETWORK_COLOR}, 
      'data--base--alt':  	        
            {'icon': 'data--base--alt', 'color': NETWORK_COLOR}, 
      'Internet':  	        
            {'icon': 'wikis', 'color': NETWORK_COLOR}, 
      'data--base':  	        
            {'icon': 'data--base', 'color': NETWORK_COLOR}, 
      'Subnet-logical':  	        
            {'icon': 'locked', 'color': NETWORK_COLOR}, 
      'application':  	        
            {'icon': 'application', 'color': NETWORK_COLOR}, 
      'arrows--horizontal': 	        
            {'icon': 'arrows--horizontal', 'color': NETWORK_COLOR},
      'Cloud-logical': 
            {'icon': 'cloud', 'color': NETWORK_COLOR},
      'function': 	        
            {'icon': 'function', 'color': NETWORK_COLOR},
      'OpenShift-prescribed':  	        
            {'icon': 'logo--openshift', 'color': NETWORK_COLOR}, 
      'password': 	        
            {'icon': 'password', 'color': NETWORK_COLOR},
      'script': 	        
            {'icon': 'script', 'color': NETWORK_COLOR},
      'user--admin': 	        
            {'icon': 'user--admin', 'color': NETWORK_COLOR},
      'cloud-foundry--1': 	        
            {'icon': 'cloud-foundry--1', 'color': NETWORK_COLOR},
      'cloud-satellite':  	        
            {'icon': 'cloud-satellite', 'color': NETWORK_COLOR}, 
      'timer':  	        
            {'icon': 'timer', 'color': NETWORK_COLOR}, 
      'deploy':  	        
            {'icon': 'deploy', 'color': NETWORK_COLOR}, 
      'shuffle': 	        
            {'icon': 'shuffle', 'color': NETWORK_COLOR},
      'wifi--controller': 	        
            {'icon': 'wifi--controller', 'color': NETWORK_COLOR},
      'switch-layer-3': 	        
            {'icon': 'switch-layer-3', 'color': NETWORK_COLOR},
      'VPNGateway': 	        
            {'icon': 'gateway--vpn', 'color': NETWORK_COLOR},
      'BareMetalServer': 	        
            {'icon': 'bare-metal-server', 'color': COMPUTE_COLOR},
      'switch-layer-2': 	        
            {'icon': 'switch-layer-2', 'color': NETWORK_COLOR},
      'LoadBalancer-prescribed': 	        
            {'icon': 'load-balancer--vpc', 'color': NETWORK_COLOR},
      'ACLRules': 	        
            {'icon': 'subnet-acl-rules', 'color': SECURITY_COLOR},
      'VPNConnection': 	        
            {'icon': 'vpn--connection', 'color': NETWORK_COLOR},
      'EnterpriseNetwork': 	        
            {'icon': 'network--enterprise', 'color': NETWORK_COLOR},
      'direct-link': 	        
            {'icon': 'direct-link', 'color': NETWORK_COLOR},
      'SecurityServices-prescribed': 	        
            {'icon': 'ibm-security--services', 'color': NETWORK_COLOR},
      'group--resource': 	        
            {'icon': 'group--resource', 'color': NETWORK_COLOR},
      'user--service-desk': 	        
            {'icon': 'user--service-desk', 'color': NETWORK_COLOR},
      'document--protected': 	        
            {'icon': 'document--protected', 'color': NETWORK_COLOR},
      'group--security': 	        
            {'icon': 'group--security', 'color': NETWORK_COLOR},
      'application--virtual': 	        
            {'icon': 'application--virtual', 'color': NETWORK_COLOR},
      'load-balancer--pool': 	        
            {'icon': 'load-balancer--pool', 'color': NETWORK_COLOR},
      'vehicle--services': 	        
            {'icon': 'vehicle--services', 'color': NETWORK_COLOR},
      'security-services': 	        
            {'icon': 'security-services', 'color': NETWORK_COLOR},
      'user--military': 	        
            {'icon': 'user--military', 'color': NETWORK_COLOR},
      'message-queue': 	        
            {'icon': 'message-queue', 'color': NETWORK_COLOR},
      'data-backup': 	        
            {'icon': 'data-backup', 'color': NETWORK_COLOR},
      'gui': 	        
            {'icon': 'gui', 'color': NETWORK_COLOR},
      'CloudMonitoring': 	        
            {'icon': 'cloud--monitoring', 'color': MANAGEMENT_COLOR},
      'Firewall': 	        
            {'icon': 'firewall', 'color': SECURITY_COLOR},
      'wifi--not-secure': 	        
            {'icon': 'wifi--not-secure', 'color': NETWORK_COLOR},
      'CDN': 	        
            {'icon': 'content-delivery-network', 'color': NETWORK_COLOR},
      'CloudAlerting': 	        
            {'icon': 'cloud--alerting', 'color': MANAGEMENT_COLOR},
      'FlowLogs-prescribed': 	        
            {'icon': 'flow-logs-vpc', 'color': NETWORK_COLOR},
      'cloud--service-management': 	        
            {'icon': 'cloud--service-management', 'color': NETWORK_COLOR},
      'load-balancer--network': 	        
            {'icon': 'load-balancer--network', 'color': NETWORK_COLOR},
      'PublicNetwork': 	        
            {'icon': 'network--public', 'color': NETWORK_COLOR},
      'server--dns': 	        
            {'icon': 'server--dns', 'color': NETWORK_COLOR},
      'vehicle--api': 	        
            {'icon': 'vehicle--api', 'color': NETWORK_COLOR},
      'infrastructure--classic': 	        
            {'icon': 'infrastructure--classic', 'color': NETWORK_COLOR},
      'instance--classic': 	        
            {'icon': 'instance--classic', 'color': NETWORK_COLOR},
      'load-balancer--application': 	        
            {'icon': 'load-balancer--application', 'color': NETWORK_COLOR},
      'ibm-cloud--dedicated-host': 	        
            {'icon': 'ibm-cloud--dedicated-host', 'color': NETWORK_COLOR},
      'ibm-cloud--internet-services': 	        
            {'icon': 'ibm-cloud--internet-services', 'color': NETWORK_COLOR},
      'radio--push-to-talk': 	        
            {'icon': 'radio--push-to-talk', 'color': NETWORK_COLOR},
      'load-balancer--global': 	        
            {'icon': 'load-balancer--global', 'color': NETWORK_COLOR},
      'firewall--classic': 	        
            {'icon': 'firewall--classic', 'color': NETWORK_COLOR},
      'block-storage--alt': 	        
            {'icon': 'block-storage--alt', 'color': NETWORK_COLOR},
      'group--access': 	        
            {'icon': 'group--access', 'color': NETWORK_COLOR},
      'vpn--policy': 	        
            {'icon': 'vpn--policy', 'color': NETWORK_COLOR},
      'code-signing-service': 	        
            {'icon': 'code-signing-service', 'color': NETWORK_COLOR},
      'MemoryProfile': 	        
            {'icon': 'instance--mx', 'color': COMPUTE_COLOR},
      'hybrid-networking--alt': 	        
            {'icon': 'hybrid-networking--alt', 'color': NETWORK_COLOR},
      'document--unprotected': 	        
            {'icon': 'document--unprotected', 'color': NETWORK_COLOR},
      'bastion-host': 	        
            {'icon': 'bastion-host', 'color': NETWORK_COLOR},
      'data-blob': 	        
            {'icon': 'data-blob', 'color': NETWORK_COLOR},
      'ObjectStorage-logical': 	        
            {'icon': 'object-storage--alt', 'color': STORAGE_COLOR},
      'server--proxy': 	        
            {'icon': 'server--proxy', 'color': NETWORK_COLOR},
      'application--mobile': 	        
            {'icon': 'application--mobile', 'color': NETWORK_COLOR},
      'mobility--services': 	        
            {'icon': 'mobility--services', 'color': NETWORK_COLOR},
      'file-storage': 	        
            {'icon': 'file-storage', 'color': NETWORK_COLOR},
      'router--wifi': 	        
            {'icon': 'router--wifi', 'color': NETWORK_COLOR},
      'intrusion-prevention': 	        
            {'icon': 'intrusion-prevention', 'color': NETWORK_COLOR},
      'edge-node--alt': 	        
            {'icon': 'edge-node--alt', 'color': NETWORK_COLOR},
      'vlan--ibm': 	        
            {'icon': 'vlan--ibm', 'color': NETWORK_COLOR},
      'CloudServices': 	        
            {'icon': 'cloud-services', 'color': NETWORK_COLOR},
      'BlockStorage': 	        
            {'icon': 'block-storage', 'color': STORAGE_COLOR},
      'FloatingIP': 	        
            {'icon': 'floating-ip', 'color': NETWORK_COLOR},
      'vehicle--connected': 	        
            {'icon': 'vehicle--connected', 'color': NETWORK_COLOR},
      'group--account': 	        
            {'icon': 'group--account', 'color': NETWORK_COLOR},
      'image-service': 	        
            {'icon': 'image-service', 'color': NETWORK_COLOR},
      'BalancedProfile': 	        
            {'icon': 'instance--bx', 'color': NETWORK_COLOR},
      'data-accessor': 	        
            {'icon': 'data-accessor', 'color': NETWORK_COLOR},
      'gateway--user-access': 	        
            {'icon': 'gateway--user-access', 'color': NETWORK_COLOR},
      'document--signed': 	        
            {'icon': 'document--signed', 'color': NETWORK_COLOR},
      'application--web': 	        
            {'icon': 'application--web', 'color': NETWORK_COLOR},
      'autoscaling': 	        
            {'icon': 'autoscaling', 'color': NETWORK_COLOR},
      'load-balancer--listener': 	        
            {'icon': 'load-balancer--listener', 'color': NETWORK_COLOR},
      'radio--combat': 	        
            {'icon': 'radio--combat', 'color': NETWORK_COLOR},
      'user--settings': 	        
            {'icon': 'user--settings', 'color': NETWORK_COLOR},
      'wifi-bridge--alt': 	        
            {'icon': 'wifi-bridge--alt', 'color': NETWORK_COLOR},
      'point-of-presence': 	        
            {'icon': 'point-of-presence', 'color': NETWORK_COLOR},
      'AvailabilityZone': 	        
            {'icon': 'data--center', 'color': NETWORK_COLOR},
      'sim-card': 	        
            {'icon': 'sim-card', 'color': NETWORK_COLOR},
      'chat--operational': 	        
            {'icon': 'chat--operational', 'color': NETWORK_COLOR},
      'VPE-prescribed': 	        
            {'icon': 'ibm-cloud--vpc-endpoints', 'color': NETWORK_COLOR},
      'id-management': 	        
            {'icon': 'id-management', 'color': NETWORK_COLOR},
      'Instance-prescribed': 	        
            {'icon': 'instance--virtual', 'color': COMPUTE_COLOR},
      'gui--management': 	        
            {'icon': 'gui--management', 'color': NETWORK_COLOR},
      'virtual-desktop': 	        
            {'icon': 'virtual-desktop', 'color': NETWORK_COLOR},
      'ComputeProfile': 	        
            {'icon': 'instance--cx', 'color': COMPUTE_COLOR},
      'phone--settings': 	        
            {'icon': 'phone--settings', 'color': NETWORK_COLOR},
      'network--overlay': 	        
            {'icon': 'network--overlay', 'color': NETWORK_COLOR},
      'Gateway': 	        
            {'icon': 'gateway', 'color': NETWORK_COLOR},
      'document--security': 	        
            {'icon': 'document--security', 'color': NETWORK_COLOR},
      'Router': 	        
            {'icon': 'router', 'color': NETWORK_COLOR},
      'router--voice':  	        
            {'icon': 'router--voice', 'color': NETWORK_COLOR}, 
      'dns-services': 	        
            {'icon': 'dns-services', 'color': NETWORK_COLOR},
      'vlan': 	        
            {'icon': 'vlan', 'color': NETWORK_COLOR},
      'server--time': 	        
            {'icon': 'server--time', 'color': NETWORK_COLOR},
      'gateway--api': 	        
            {'icon': 'gateway--api', 'color': NETWORK_COLOR},
      'wifi--secure': 	        
            {'icon': 'wifi--secure', 'color': NETWORK_COLOR},
      'gateway--mail': 	        
            {'icon': 'gateway--mail', 'color': NETWORK_COLOR},
      'PublicGateway': 	        
            {'icon': 'gateway--public', 'color': NETWORK_COLOR},
      'phone--application': 	        
            {'icon': 'phone--application', 'color': NETWORK_COLOR},
      'transmission-lte': 	        
            {'icon': 'transmission-lte', 'color': NETWORK_COLOR},
      'vehicle--insights': 	        
            {'icon': 'vehicle--insights', 'color': NETWORK_COLOR},
      'ActivityTracker': 	        
            {'icon': 'cloud--auditing', 'color': NETWORK_COLOR},
      'hardware-security-module': 	        
            {'icon': 'hardware-security-module', 'color': NETWORK_COLOR},
      'two-factor-authentication': 	        
            {'icon': 'two-factor-authentication', 'color': NETWORK_COLOR},
      'wifi-bridge': 	        
            {'icon': 'wifi-bridge', 'color': NETWORK_COLOR},
      'load-balancer--classic': 	        
            {'icon': 'load-balancer--classic', 'color': NETWORK_COLOR},
      'load-balancer--local': 	        
            {'icon': 'load-balancer--local', 'color': NETWORK_COLOR},
      'cloud--logging': 	        
            {'icon': 'cloud--logging', 'color': NETWORK_COLOR},
      'Subnet-prescribed': 	        
            {'icon': 'ibm-cloud--subnets', 'color': NETWORK_COLOR},
      'data-diode': 	        
            {'icon': 'data-diode', 'color': NETWORK_COLOR},
      'folder--details': 	        
            {'icon': 'folder--details', 'color': NETWORK_COLOR},
      'gateway--security': 	        
            {'icon': 'gateway--security', 'color': NETWORK_COLOR},
      'bare-metal-server--01': 	        
            {'icon': 'bare-metal-server--01', 'color': NETWORK_COLOR},
      'bare-metal-server--02':  	        
            {'icon': 'bare-metal-server--02', 'color': NETWORK_COLOR}, 
      'boot':  	        
            {'icon': 'boot', 'color': NETWORK_COLOR}, 
      'box--extra-large': 	        
            {'icon': 'box--extra-large', 'color': NETWORK_COLOR},
      'box--large': 	        
            {'icon': 'box--large', 'color': NETWORK_COLOR},
      'box--medium': 	        
            {'icon': 'box--medium', 'color': NETWORK_COLOR},
      'box--small': 	        
            {'icon': 'box--small', 'color': NETWORK_COLOR},
      'cloud-satellite--config':  	        
            {'icon': 'cloud-satellite--config', 'color': NETWORK_COLOR}, 
      'cloud-satellite--link':  	        
            {'icon': 'cloud-satellite--link', 'color': NETWORK_COLOR}, 
      'cloud-satellite--services':  	        
            {'icon': 'cloud-satellite--services', 'color': NETWORK_COLOR}, 
      'communication--unified': 	        
            {'icon': 'communication--unified', 'color': NETWORK_COLOR},
      'database--datastax': 	        
            {'icon': 'database--datastax', 'color': NETWORK_COLOR},
      'database--elastic': 	        
            {'icon': 'database--elastic', 'color': NETWORK_COLOR},
      'database--enterprisedb': 	        
            {'icon': 'database--enterprisedb', 'color': NETWORK_COLOR},
      'database--etcd': 	        
            {'icon': 'database--etcd', 'color': NETWORK_COLOR},
      'database--mongodb': 	        
            {'icon': 'database--mongodb', 'color': NETWORK_COLOR},
      'database--postgresql': 	        
            {'icon': 'database--postgresql', 'color': NETWORK_COLOR},
      'database--rabbit': 	        
            {'icon': 'database--rabbit', 'color': NETWORK_COLOR},
      'database--redis': 	        
            {'icon': 'database--redis', 'color': NETWORK_COLOR},
      'directory-domain':  	        
            {'icon': 'directory-domain', 'color': NETWORK_COLOR}, 
      'encryption': 	        
            {'icon': 'encryption', 'color': NETWORK_COLOR},
      'ibm-cloud-pak--applications':  	        
            {'icon': 'ibm-cloud-pak--applications', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--data':  	        
            {'icon': 'ibm-cloud-pak--data', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--integration':  	        
            {'icon': 'ibm-cloud-pak--integration', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--multicloud-mgmt':  	        
            {'icon': 'ibm-cloud-pak--multicloud-mgmt', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--security':  	        
            {'icon': 'ibm-cloud-pak--security', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--system':  	        
            {'icon': 'ibm-cloud-pak--system', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--network-automation':  	        
            {'icon': 'ibm-cloud-pak--network-automation', 'color': NETWORK_COLOR}, 
      'ibm-cloud-pak--watson-aiops':  	        
            {'icon': 'ibm-cloud-pak--watson-aiops', 'color': NETWORK_COLOR}, 
      'military-camp': 	        
            {'icon': 'military-camp', 'color': NETWORK_COLOR},
      'network--admin-control': 	        
            {'icon': 'network--admin-control', 'color': NETWORK_COLOR},
      'pcn--e-node': 	        
            {'icon': 'pcn--e-node', 'color': NETWORK_COLOR},
      'pcn--military': 	        
            {'icon': 'pcn--military', 'color': NETWORK_COLOR},
      'pcn--p-node': 	        
            {'icon': 'pcn--p-node', 'color': NETWORK_COLOR},
      'pcn--z-node': 	        
            {'icon': 'pcn--z-node', 'color': NETWORK_COLOR},
      'session-border-control': 	        
            {'icon': 'session-border-control', 'color': NETWORK_COLOR},
      'tank': 	        
            {'icon': 'tank', 'color': NETWORK_COLOR},
      'volume--block-storage': 	        
            {'icon': 'volume--block-storage', 'color': NETWORK_COLOR},
      'volume--file-storage': 	        
            {'icon': 'volume--file-storage', 'color': NETWORK_COLOR},
      'volume--object-storage': 	        
            {'icon': 'volume--object-storage', 'color': NETWORK_COLOR},
      'ibm-cloud--transit-gateway': 	        
            {'icon': 'ibm-cloud--transit-gateway', 'color': NETWORK_COLOR},
      'enterprise': 	        
            {'icon': 'enterprise', 'color': NETWORK_COLOR},
      'linux':  	        
            {'icon': 'linux', 'color': NETWORK_COLOR}, 
      'linux--alt':  	        
            {'icon': 'linux--alt', 'color': NETWORK_COLOR}, 
      'slicestor': 	        
            {'icon': 'slicestor', 'color': NETWORK_COLOR},
      'concept': 	        
            {'icon': 'concept', 'color': NETWORK_COLOR},
      'deployment-unit--data': 	        
            {'icon': 'deployment-unit--data', 'color': NETWORK_COLOR},
      'deployment-unit--execution': 	        
            {'icon': 'deployment-unit--execution', 'color': NETWORK_COLOR},
      'deployment-unit--installation': 	        
            {'icon': 'deployment-unit--installation', 'color': NETWORK_COLOR},
      'deployment-unit--presentation': 	        
            {'icon': 'deployment-unit--presentation', 'color': NETWORK_COLOR},
      'deployment-unit--technical--data': 	        
            {'icon': 'deployment-unit--technical--data', 'color': NETWORK_COLOR},
      'deployment-unit--technical--execution': 	        
            {'icon': 'deployment-unit--technical--execution', 'color': NETWORK_COLOR},
      'deployment-unit--technical--installation': 	        
            {'icon': 'deployment-unit--technical--installation', 'color': NETWORK_COLOR},
      'deployment-unit--technical--presentation': 	        
            {'icon': 'deployment-unit--technical--presentation', 'color': NETWORK_COLOR},
      'API': 	        
            {'icon': 'api', 'color': APPLICATION_COLOR},
      'BuildTool':  	        
            {'icon': 'build-tool', 'color': APPLICATION_COLOR}, 
      'CD':  	        
            {'icon': 'continuous-deployment', 'color': MANAGEMENT_COLOR}, 
      'CI': 	        
            {'icon': 'continuous-integration', 'color': MANAGEMENT_COLOR},
      'KeyProtect--prescribed':  	        
            {'icon': 'ibm-cloud--key-protect', 'color': SECURITY_COLOR}, 
      'SecretsManager': 	        
            {'icon': 'ibm-cloud--secrets-manager', 'color': SECURITY_COLOR},
      'ArtifactRepository': 	        
            {'icon': 'repo--artifact', 'color': STORAGE_COLOR},
      'SourceCodeRepository': 	        
            {'icon': 'repo--source-code', 'color': STORAGE_COLOR},
      'ServiceID':  	        
            {'icon': 'service-id', 'color': SECURITY_COLOR}, 
      'TestTool': 	        
            {'icon': 'test-tool', 'color': APPLICATION_COLOR}
   }

   common = None

   def __init__(self, common):   
      self.common = common

   def getIcon(self, shapetype):
      if self.common.isLogicalShapes():
         if shapetype in self.iconDictionary:
            icon = self.iconDictionary[shapetype]
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-logical'  in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-logical']
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-prescribed' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-prescribed']
            iconname = icon['icon']
            iconcolor = icon['color']
         else:
            icon = self.iconDictionary['Undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
      else: # check prescribed
         if shapetype in self.iconDictionary:
            icon = self.iconDictionary[shapetype]
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-prescribed'  in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-prescribed']
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-logical' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-logical']
            iconname = icon['icon']
            iconcolor = icon['color']
         else:
            icon = self.iconDictionary['Undefined']
            iconname = icon['icon']
            iconcolor = icon['color']

      return iconname, iconcolor    
