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

from enum import Enum

from .constants import ComponentColor, ShapeKind

class Icons:
   iconDictionary = { 
      'Undefined': 	        
            {'icon': 'undefined', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'UserCollaboration': 	        
            {'icon': 'collaborate', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR},
      'Credentials': 	        
            {'icon': 'credentials', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Devices': 	        
            {'icon': 'devices', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR},
      'Meeting': 	        
            {'icon': 'events', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR},
      'AuthorizationBoundary': 	        
            {'icon': 'flag', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Cloud-prescribed': 	        
            {'icon': 'ibm-cloud', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'User':  	        
            {'icon': 'user', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR}, 
      'Instance-logical': 	        
            {'icon': 'virtual-machine', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'VPC-logical':  	        
            {'icon': 'virtual-private-cloud', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION}, 
      'VPC-prescribed':  	        
            {'icon': 'virtual-private-cloud--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION}, 
      'Region': 	        
            {'icon': 'location', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'Security': 	        
            {'icon': 'security', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE},
      'FingerprintRecognition': 	        
            {'icon': 'fingerprint-recognition', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Network2':  	        
            {'icon': 'network--2', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'EdgeNode':  	        
            {'icon': 'edge-node', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'Group':  	        
            {'icon': 'group', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR}, 
      'Mobile':  	        
            {'icon': 'mobile', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR}, 
      'Policy':  	        
            {'icon': 'policy', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE}, 
      'Rule':  	        
            {'icon': 'rule', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE}, 
      'Terminal':  	        
            {'icon': 'terminal', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ObjectStorage-prescribed':  	        
            {'icon': 'object-storage', 'color': ComponentColor.STORAGE, 'kind': ShapeKind.NODE}, 
      'Laptop':  	        
            {'icon': 'laptop', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR}, 
      'Tablet':  	        
            {'icon': 'tablet', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR}, 
      'Archive':  	        
            {'icon': 'archive', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'DataCenter':  	        
            {'icon': 'data--base--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'Internet':  	        
            {'icon': 'wikis', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'Database':  	        
            {'icon': 'data--base', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'Subnet-logical':  	        
            {'icon': 'locked', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION}, 
      'application':  	        
            {'icon': 'application', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'arrows--horizontal': 	        
            {'icon': 'arrows--horizontal', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Cloud-logical': 
            {'icon': 'cloud', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'ServerlessApplication': 	        
            {'icon': 'function', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'OpenShift':  	        
            {'icon': 'logo--openshift', 'color': ComponentColor.COMPUTE, 'kind': ShapeKind.NODE}, 
      'password': 	        
            {'icon': 'password', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'script': 	        
            {'icon': 'script', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Administrator': 	        
            {'icon': 'user--admin', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR},
      'CloudFoundry': 	        
            {'icon': 'cloud-foundry--1', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'cloud-satellite':  	        
            {'icon': 'cloud-satellite', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'timer':  	        
            {'icon': 'timer', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'deploy':  	        
            {'icon': 'deploy', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'shuffle': 	        
            {'icon': 'shuffle', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'wifi--controller': 	        
            {'icon': 'wifi--controller', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'switch-layer-3': 	        
            {'icon': 'switch-layer-3', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'VPNGateway': 	        
            {'icon': 'gateway--vpn', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BareMetalServer': 	        
            {'icon': 'bare-metal-server', 'color': ComponentColor.COMPUTE, 'kind': ShapeKind.NODE},
      'switch-layer-2': 	        
            {'icon': 'switch-layer-2', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'LoadBalancer-prescribed': 	        
            {'icon': 'load-balancer--vpc', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ACLRules': 	        
            {'icon': 'subnet-acl-rules', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE},
      'VPNConnection': 	        
            {'icon': 'vpn--connection', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'EnterpriseNetwork': 	        
            {'icon': 'network--enterprise', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'direct-link': 	        
            {'icon': 'direct-link', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'SecurityServices-prescribed': 	        
            {'icon': 'ibm-security--services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ResourceGroup': 	        
            {'icon': 'group--resource', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.ZONE},
      'ServiceDeskUser': 	        
            {'icon': 'user--service-desk', 'color': ComponentColor.USER, 'kind': ShapeKind.ACTOR},
      'document--protected': 	        
            {'icon': 'document--protected', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'SecurityGroup': 	        
            {'icon': 'group--security', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.ZONE},
      'application--virtual': 	        
            {'icon': 'application--virtual', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--pool': 	        
            {'icon': 'load-balancer--pool', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'vehicle--services': 	        
            {'icon': 'vehicle--services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'security-services': 	        
            {'icon': 'security-services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'user--military': 	        
            {'icon': 'user--military', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'message-queue': 	        
            {'icon': 'message-queue', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'DataBackup': 	        
            {'icon': 'data-backup', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'GUI': 	        
            {'icon': 'gui', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'CloudMonitoring': 	        
            {'icon': 'cloud--monitoring', 'color': ComponentColor.MANAGEMENT, 'kind': ShapeKind.NODE},
      'Firewall': 	        
            {'icon': 'firewall', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE},
      'wifi--not-secure': 	        
            {'icon': 'wifi--not-secure', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'CDN': 	        
            {'icon': 'content-delivery-network', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'CloudAlerting': 	        
            {'icon': 'cloud--alerting', 'color': ComponentColor.MANAGEMENT, 'kind': ShapeKind.NODE},
      'FlowLogs-prescribed': 	        
            {'icon': 'flow-logs-vpc', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'cloud--service-management': 	        
            {'icon': 'cloud--service-management', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--network': 	        
            {'icon': 'load-balancer--network', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'PublicNetwork': 	        
            {'icon': 'network--public', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'server--dns': 	        
            {'icon': 'server--dns', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'vehicle--api': 	        
            {'icon': 'vehicle--api', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ClassicInfrastructure': 	        
            {'icon': 'infrastructure--classic', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ClassicInstance': 	        
            {'icon': 'instance--classic', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--application': 	        
            {'icon': 'load-balancer--application', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ibm-cloud--dedicated-host': 	        
            {'icon': 'ibm-cloud--dedicated-host', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'InternetServices-prescribed': 	        
            {'icon': 'ibm-cloud--internet-services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'radio--push-to-talk': 	        
            {'icon': 'radio--push-to-talk', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--global': 	        
            {'icon': 'load-balancer--global', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'firewall--classic': 	        
            {'icon': 'firewall--classic', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BlockStorage-logical': 	        
            {'icon': 'block-storage--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'AccessGroup': 	        
            {'icon': 'group--access', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.ZONE},
      'vpn--policy': 	        
            {'icon': 'vpn--policy', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'code-signing-service': 	        
            {'icon': 'code-signing-service', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'MemoryProfile': 	        
            {'icon': 'instance--mx', 'color': ComponentColor.COMPUTE, 'kind': ShapeKind.NODE},
      'hybrid-networking--alt': 	        
            {'icon': 'hybrid-networking--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'document--unprotected': 	        
            {'icon': 'document--unprotected', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'bastion-host': 	        
            {'icon': 'bastion-host', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BLOB': 	        
            {'icon': 'data-blob', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ObjectStorage-logical': 	        
            {'icon': 'object-storage--alt', 'color': ComponentColor.STORAGE, 'kind': ShapeKind.NODE},
      'server--proxy': 	        
            {'icon': 'server--proxy', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'application--mobile': 	        
            {'icon': 'application--mobile', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'mobility--services': 	        
            {'icon': 'mobility--services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'FileStorage': 	        
            {'icon': 'file-storage', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'router--wifi': 	        
            {'icon': 'router--wifi', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'intrusion-prevention': 	        
            {'icon': 'intrusion-prevention', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'edge-node--alt': 	        
            {'icon': 'edge-node--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'VLAN-prescribed': 	        
            {'icon': 'vlan--ibm', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'CloudServices': 	        
            {'icon': 'cloud-services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'BlockStorage-prescribed': 	        
            {'icon': 'block-storage', 'color': ComponentColor.STORAGE, 'kind': ShapeKind.NODE},
      'FloatingIP': 	        
            {'icon': 'floating-ip', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'vehicle--connected': 	        
            {'icon': 'vehicle--connected', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'AccountGroup': 	        
            {'icon': 'group--account', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.ZONE},
      'image-service': 	        
            {'icon': 'image-service', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BalancedProfile': 	        
            {'icon': 'instance--bx', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ObjectStorageAccessor': 	        
            {'icon': 'data-accessor', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'gateway--user-access': 	        
            {'icon': 'gateway--user-access', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'document--signed': 	        
            {'icon': 'document--signed', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'application--web': 	        
            {'icon': 'application--web', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'InstanceGroup': 	        
            {'icon': 'autoscaling', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.ZONE},
      'load-balancer--listener': 	        
            {'icon': 'load-balancer--listener', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'radio--combat': 	        
            {'icon': 'radio--combat', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'user--settings': 	        
            {'icon': 'user--settings', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'wifi-bridge--alt': 	        
            {'icon': 'wifi-bridge--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'POP': 	        
            {'icon': 'point-of-presence', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'AvailabilityZone': 	        
            {'icon': 'data--center', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'sim-card': 	        
            {'icon': 'sim-card', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'chat--operational': 	        
            {'icon': 'chat--operational', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'VPE-prescribed': 	        
            {'icon': 'ibm-cloud--vpc-endpoints', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'id-management': 	        
            {'icon': 'id-management', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Instance-prescribed': 	        
            {'icon': 'instance--virtual', 'color': ComponentColor.COMPUTE, 'kind': ShapeKind.NODE},
      'gui--management': 	        
            {'icon': 'gui--management', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'virtual-desktop': 	        
            {'icon': 'virtual-desktop', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ComputeProfile': 	        
            {'icon': 'instance--cx', 'color': ComponentColor.COMPUTE, 'kind': ShapeKind.NODE},
      'phone--settings': 	        
            {'icon': 'phone--settings', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'OverlayNetwork': 	        
            {'icon': 'network--overlay', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Gateway': 	        
            {'icon': 'gateway', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'document--security': 	        
            {'icon': 'document--security', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Router': 	        
            {'icon': 'router', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'router--voice':  	        
            {'icon': 'router--voice', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'dns-services': 	        
            {'icon': 'dns-services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'VLAN-logical': 	        
            {'icon': 'vlan', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'server--time': 	        
            {'icon': 'server--time', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'gateway--api': 	        
            {'icon': 'gateway--api', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'wifi--secure': 	        
            {'icon': 'wifi--secure', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'gateway--mail': 	        
            {'icon': 'gateway--mail', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'PublicGateway': 	        
            {'icon': 'gateway--public', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'phone--application': 	        
            {'icon': 'phone--application', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'transmission-lte': 	        
            {'icon': 'transmission-lte', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'vehicle--insights': 	        
            {'icon': 'vehicle--insights', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ActivityTracker': 	        
            {'icon': 'cloud--auditing', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'hardware-security-module': 	        
            {'icon': 'hardware-security-module', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'two-factor-authentication': 	        
            {'icon': 'two-factor-authentication', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'wifi-bridge': 	        
            {'icon': 'wifi-bridge', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--classic': 	        
            {'icon': 'load-balancer--classic', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'load-balancer--local': 	        
            {'icon': 'load-balancer--local', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'cloud--logging': 	        
            {'icon': 'cloud--logging', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Subnet-prescribed': 	        
            {'icon': 'ibm-cloud--subnets', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.LOCATION},
      'data-diode': 	        
            {'icon': 'data-diode', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'FileStorage': 	        
            {'icon': 'folder--details', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'gateway--security': 	        
            {'icon': 'gateway--security', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BareMetalServer1': 	        
            {'icon': 'bare-metal-server--01', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BareMetalServer2':  	        
            {'icon': 'bare-metal-server--02', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'boot':  	        
            {'icon': 'boot', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'box--extra-large': 	        
            {'icon': 'box--extra-large', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'box--large': 	        
            {'icon': 'box--large', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'box--medium': 	        
            {'icon': 'box--medium', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'box--small': 	        
            {'icon': 'box--small', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'cloud-satellite--config':  	        
            {'icon': 'cloud-satellite--config', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'cloud-satellite--link':  	        
            {'icon': 'cloud-satellite--link', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'cloud-satellite--services':  	        
            {'icon': 'cloud-satellite--services', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'communication--unified': 	        
            {'icon': 'communication--unified', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'DataStax': 	        
            {'icon': 'database--datastax', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ElasticDB': 	        
            {'icon': 'database--elastic', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'EnterpriseDB': 	        
            {'icon': 'database--enterprisedb', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Etcd': 	        
            {'icon': 'database--etcd', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'MongoDB': 	        
            {'icon': 'database--mongodb', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'PostgreSQL': 	        
            {'icon': 'database--postgresql', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'RabbitDB':	        
            {'icon': 'database--rabbit', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Redis': 	        
            {'icon': 'database--redis', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'directory-domain':  	        
            {'icon': 'directory-domain', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'encryption': 	        
            {'icon': 'encryption', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ibm-cloud-pak--applications':  	        
            {'icon': 'ibm-cloud-pak--applications', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--data':  	        
            {'icon': 'ibm-cloud-pak--data', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--integration':  	        
            {'icon': 'ibm-cloud-pak--integration', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--multicloud-mgmt':  	        
            {'icon': 'ibm-cloud-pak--multicloud-mgmt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--network-automation':  	        
            {'icon': 'ibm-cloud-pak--network-automation', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--security':  	        
            {'icon': 'ibm-cloud-pak--security', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--system':  	        
            {'icon': 'ibm-cloud-pak--system', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ibm-cloud-pak--watson-aiops':  	        
            {'icon': 'ibm-cloud-pak--watson-aiops', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'military-camp': 	        
            {'icon': 'military-camp', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'network--admin-control': 	        
            {'icon': 'network--admin-control', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'pcn--e-node': 	        
            {'icon': 'pcn--e-node', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'pcn--military': 	        
            {'icon': 'pcn--military', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'pcn--p-node': 	        
            {'icon': 'pcn--p-node', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'pcn--z-node': 	        
            {'icon': 'pcn--z-node', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'session-border-control': 	        
            {'icon': 'session-border-control', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'tank': 	        
            {'icon': 'tank', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'BlockStorageVolume': 	        
            {'icon': 'volume--block-storage', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'FileStorageVolume': 	        
            {'icon': 'volume--file--storage', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'ObjectStorageVolume': 	        
            {'icon': 'volume--object-storage', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'TransitGateway-prescribed': 	        
            {'icon': 'ibm-cloud--transit-gateway', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Enterprise': 	        
            {'icon': 'enterprise', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'Linux-prescribed':  	        
            {'icon': 'linux', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'Linux--logical':  	        
            {'icon': 'linux--alt', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE}, 
      'ObjectStorageSlicestor': 	        
            {'icon': 'slicestor', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'concept': 	        
            {'icon': 'concept', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--data': 	        
            {'icon': 'deployment-unit--data', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--execution': 	        
            {'icon': 'deployment-unit--execution', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--installation': 	        
            {'icon': 'deployment-unit--installation', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--presentation': 	        
            {'icon': 'deployment-unit--presentation', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--technical--data': 	        
            {'icon': 'deployment-unit--technical--data', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--technical--execution': 	        
            {'icon': 'deployment-unit--technical--execution', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--technical--installation': 	        
            {'icon': 'deployment-unit--technical--installation', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'deployment-unit--technical--presentation': 	        
            {'icon': 'deployment-unit--technical--presentation', 'color': ComponentColor.NETWORK, 'kind': ShapeKind.NODE},
      'API': 	        
            {'icon': 'api', 'color': ComponentColor.APPLICATION, 'kind': ShapeKind.NODE},
      'BuildTool':  	        
            {'icon': 'build-tool', 'color': ComponentColor.APPLICATION, 'kind': ShapeKind.NODE}, 
      'CD':  	        
            {'icon': 'continuous-deployment', 'color': ComponentColor.MANAGEMENT, 'kind': ShapeKind.NODE}, 
      'CI': 	        
            {'icon': 'continuous-integration', 'color': ComponentColor.MANAGEMENT, 'kind': ShapeKind.NODE},
      'KeyProtect--prescribed':  	        
            {'icon': 'ibm-cloud--key-protect', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE}, 
      'SecretsManager': 	        
            {'icon': 'ibm-cloud--secrets-manager', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE},
      'ArtifactRepository': 	        
            {'icon': 'repo--artifact', 'color': ComponentColor.STORAGE, 'kind': ShapeKind.NODE},
      'SourceCodeRepository': 	        
            {'icon': 'repo--source-code', 'color': ComponentColor.STORAGE, 'kind': ShapeKind.NODE},
      'ServiceID':  	        
            {'icon': 'service-id', 'color': ComponentColor.SECURITY, 'kind': ShapeKind.NODE}, 
      'TestTool': 	        
            {'icon': 'test-tool', 'color': ComponentColor.APPLICATION, 'kind': ShapeKind.NODE}
   }

   common = None

   def __init__(self, common):   
      self.common = common

   def getIconDictionary(self):
      return self.iconDictionary

   def getIcon(self, name, shapetype):
      if self.common.isAllIcons():
         iconname = name
         iconcolor = ComponentColor.NETWORK
      elif self.common.isLogicalShapes():
         if shapetype in self.iconDictionary:
            icon = self.iconDictionary[shapetype]
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-logical' in self.iconDictionary:
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
         elif shapetype + '-prescribed' in self.iconDictionary:
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

   def validIcon(self, iconname):
      for name, values in self.iconDictionary.items():
         if iconname == values['icon']:
            return True
      return False
