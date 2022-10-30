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

Icons = { 
    'undefined':
        {'logical': 'undefined', 'prescribed': 'undefined', 'color': NETWORK_COLOR},  
    'collaborate':
        {'logical': 'collaborate', 'prescribed': 'collaborate', 'color': NETWORK_COLOR},  
    'credentials':
        {'logical': 'credentials', 'prescribed': 'credentials', 'color': NETWORK_COLOR},  
    'devices':
        {'logical': 'devices', 'prescribed': 'devices', 'color': NETWORK_COLOR},  
    'events':
        {'logical': 'events', 'prescribed': 'events', 'color': NETWORK_COLOR},  
    'flag':
        {'logical': 'flag', 'prescribed': 'flag', 'color': NETWORK_COLOR},  
    'Cloud':
        {'logical': 'cloud', 'prescribed': 'ibm-cloud', 'color': NETWORK_COLOR},  
    'User':
        {'logical': 'user', 'prescribed': 'user', 'color': USER_COLOR},  
    'Instance':
        {'logical': 'virtual-machine', 'prescribed': 'instance--virtual', 'color': COMPUTE_COLOR},  
    'VPC':
        {'logical': 'virtual-private-cloud', 'prescribed': 'virtual-private-cloud--alt', 'color': NETWORK_COLOR},  
    'Region':
        {'logical': 'location', 'prescribed': 'location', 'color': BACKEND_COLOR},  
    'Security':
        {'logical': 'security', 'prescribed': 'security', 'color': SECURITY_COLOR},  
    'fingerprint-recognition':
        {'logical': 'fingerprint-recognition', 'prescribed': 'fingerprint-recognition', 'color': NETWORK_COLOR},  
    'network--2':
        {'logical': 'network--2', 'prescribed': 'network--2', 'color': NETWORK_COLOR},  
    'VPN':
        {'logical': 'VPN', 'prescribed': 'VPN', 'color': SECURITY_COLOR},  
    'edge-node':
        {'logical': 'edge-node', 'prescribed': 'edge-node', 'color': NETWORK_COLOR},  
    'group':
        {'logical': 'group', 'prescribed': 'group', 'color': NETWORK_COLOR},  
    'mobile':
        {'logical': 'mobile', 'prescribed': 'mobile', 'color': NETWORK_COLOR},  
    'policy':
        {'logical': 'policy', 'prescribed': 'policy', 'color': NETWORK_COLOR},  
    'rule':
        {'logical': 'rule', 'prescribed': 'rule', 'color': NETWORK_COLOR},  
    'terminal':
        {'logical': 'terminal', 'prescribed': 'terminal', 'color': NETWORK_COLOR},  
    'ObjectStorage':
        {'logical': 'object-storage', 'prescribed': 'object-storage', 'color': STORAGE_COLOR},  
    'laptop':
        {'logical': 'laptop', 'prescribed': 'laptop', 'color': NETWORK_COLOR},  
    'tablet':
        {'logical': 'tablet', 'prescribed': 'tablet', 'color': NETWORK_COLOR},  
    'archive':
        {'logical': 'archive', 'prescribed': 'archive', 'color': NETWORK_COLOR},  
    'data--base--alt':
        {'logical': 'data--base--alt', 'prescribed': 'data--base--alt', 'color': DATA_COLOR},  
    'Internet':
        {'logical': 'wikis', 'prescribed': 'wikis', 'color': NETWORK_COLOR},  
    'data--base':
        {'logical': 'data--base', 'prescribed': 'data--base', 'color': DATA_COLOR},  
    'Subnet':
        {'logical': 'locked', 'prescribed': 'ibm-cloud--subnets', 'color': NETWORK_COLOR},  
    'application':
        {'logical': 'application', 'prescribed': 'application', 'color': NETWORK_COLOR},  
    'arrows--horizontal':
        {'logical': 'arrows--horizontal', 'prescribed': 'arrows--horizontal', 'color': NETWORK_COLOR},  
    'function':
        {'logical': 'function', 'prescribed': 'function', 'color': NETWORK_COLOR},  
    'logo--openshift':
        {'logical': 'logo--openshift', 'prescribed': 'logo--openshift', 'color': COMPUTE_COLOR},  
    'password':
        {'logical': 'password', 'prescribed': 'password', 'color': NETWORK_COLOR},  
    'script':
        {'logical': 'script', 'prescribed': 'script', 'color': NETWORK_COLOR},  
    'user--admin':
        {'logical': 'user--admin', 'prescribed': 'user--admin', 'color': NETWORK_COLOR},  
    'cloud-foundry--1':
        {'logical': 'cloud-foundry--1', 'prescribed': 'cloud-foundry--1', 'color': NETWORK_COLOR},  
    'cloud-satellite':
        {'logical': 'cloud-satellite', 'prescribed': 'cloud-satellite', 'color': NETWORK_COLOR},  
    'timer':
        {'logical': 'timer', 'prescribed': 'timer', 'color': NETWORK_COLOR},  
    'deploy':
        {'logical': 'deploy', 'prescribed': 'deploy', 'color': NETWORK_COLOR},  
    'shuffle':
        {'logical': 'shuffle', 'prescribed': 'shuffle', 'color': NETWORK_COLOR},  
    'wifi--controller':
        {'logical': 'wifi--controller', 'prescribed': 'wifi--controller', 'color': NETWORK_COLOR},  
    'switch-layer-3':
        {'logical': 'switch-layer-3', 'prescribed': 'switch-layer-3', 'color': NETWORK_COLOR},  
    'VPNGateway':
        {'logical': 'gateway--vpn', 'prescribed': 'gateway--vpn', 'color': SECURITY_COLOR},  
    'bare-metal-server':
        {'logical': 'bare-metal-server', 'prescribed': 'bare-metal-server', 'color': COMPUTE_COLOR},  
    'switch-layer-2':
        {'logical': 'switch-layer-2', 'prescribed': 'switch-layer-2', 'color': NETWORK_COLOR},  
    'LoadBalancer':
        {'logical': 'load-balancer--vpc', 'prescribed': 'load-balancer--vpc', 'color': NETWORK_COLOR},  
    'subnet-acl-rules':
        {'logical': 'subnet-acl-rules', 'prescribed': 'subnet-acl-rules', 'color': SECURITY_COLOR},  
    'VPNConnection':
        {'logical': 'vpn--connection', 'prescribed': 'vpn--connection', 'color': SECURITY_COLOR},  
    'EnterpriseNetwork':
        {'logical': 'network--enterprise', 'prescribed': 'network--enterprise', 'color': NETWORK_COLOR},  
    'direct-link':
        {'logical': 'direct-link', 'prescribed': 'direct-link', 'color': NETWORK_COLOR},  
    'ibm-security--services':
        {'logical': 'ibm-security--services', 'prescribed': 'ibm-security--services', 'color': SECURITY_COLOR},  
    'group--resource':
        {'logical': 'group--resource', 'prescribed': 'group--resource', 'color': NETWORK_COLOR},  
    'user--service-desk':
        {'logical': 'user--service-desk', 'prescribed': 'user--service-desk', 'color': NETWORK_COLOR},  
    'document--protected':
        {'logical': 'document--protected', 'prescribed': 'document--protected', 'color': NETWORK_COLOR},  
    'group--security':
        {'logical': 'group--security', 'prescribed': 'group--security', 'color': SECURITY_COLOR},  
    'application--virtual':
        {'logical': 'application--virtual', 'prescribed': 'application--virtual', 'color': COMPUTE_COLOR},  
    'load-balancer--pool':
        {'logical': 'load-balancer--pool', 'prescribed': 'load-balancer--pool', 'color': NETWORK_COLOR},  
    'vehicle--services':
        {'logical': 'vehicle--services', 'prescribed': 'vehicle--services', 'color': NETWORK_COLOR},  
    'security-services':
        {'logical': 'security-services', 'prescribed': 'security-services', 'color': SECURITY_COLOR},  
    'user--military':
        {'logical': 'user--military', 'prescribed': 'user--military', 'color': NETWORK_COLOR},  
    'message-queue':
        {'logical': 'message-queue', 'prescribed': 'message-queue', 'color': NETWORK_COLOR},  
    'data-backup':
        {'logical': 'data-backup', 'prescribed': 'data-backup', 'color': DATA_COLOR},  
    'gui':
        {'logical': 'gui', 'prescribed': 'gui', 'color': COMPUTE_COLOR},  
    'cloud--monitoring':
        {'logical': 'cloud--monitoring', 'prescribed': 'cloud--monitoring', 'color': MANAGEMENT_COLOR},  
    'firewall':
        {'logical': 'firewall', 'prescribed': 'firewall', 'color': SECURITY_COLOR},  
    'wifi--not-secure':
        {'logical': 'wifi--not-secure', 'prescribed': 'wifi--not-secure', 'color': NETWORK_COLOR},  
    'content-delivery-network':
        {'logical': 'content-delivery-network', 'prescribed': 'content-delivery-network', 'color': NETWORK_COLOR},  
    'cloud--alerting':
        {'logical': 'cloud--alerting', 'prescribed': 'cloud--alerting', 'color': MANAGEMENT_COLOR},  
    'FlowLogs':
        {'logical': 'flow-logs-vpc', 'prescribed': 'flow-logs-vpc', 'color': MANAGEMENT_COLOR},  
    'cloud--service-management':
        {'logical': 'cloud--service-management', 'prescribed': 'cloud--service-management', 'color': MANAGEMENT_COLOR},  
    'load-balancer--network':
        {'logical': 'load-balancer--network', 'prescribed': 'load-balancer--network', 'color': NETWORK_COLOR},  
    'PublicNetwork':
        {'logical': 'network--public', 'prescribed': 'network--public', 'color': NETWORK_COLOR},  
    'server--dns':
        {'logical': 'server--dns', 'prescribed': 'server--dns', 'color': NETWORK_COLOR},  
    'vehicle--api':
        {'logical': 'vehicle--api', 'prescribed': 'vehicle--api', 'color': NETWORK_COLOR},  
    'infrastructure--classic':
        {'logical': 'infrastructure--classic', 'prescribed': 'infrastructure--classic', 'color': NETWORK_COLOR},  
    'instance--classic':
        {'logical': 'instance--classic', 'prescribed': 'instance--classic', 'color': COMPUTE_COLOR},  
    'load-balancer--application':
        {'logical': 'load-balancer--application', 'prescribed': 'load-balancer--application', 'color': NETWORK_COLOR},  
    'ibm-cloud--dedicated-host':
        {'logical': 'ibm-cloud--dedicated-host', 'prescribed': 'ibm-cloud--dedicated-host', 'color': NETWORK_COLOR},  
    'ibm-cloud--internet-services':
        {'logical': 'ibm-cloud--internet-services', 'prescribed': 'ibm-cloud--internet-services', 'color': NETWORK_COLOR},  
    'radio--push-to-talk':
        {'logical': 'radio--push-to-talk', 'prescribed': 'radio--push-to-talk', 'color': NETWORK_COLOR},  
    'load-balancer--global':
        {'logical': 'load-balancer--global', 'prescribed': 'load-balancer--global', 'color': NETWORK_COLOR},  
    'firewall--classic':
        {'logical': 'firewall--classic', 'prescribed': 'firewall--classic', 'color': SECURITY_COLOR},  
    'block-storage--alt':
        {'logical': 'block-storage--alt', 'prescribed': 'block-storage--alt', 'color': STORAGE_COLOR},  
    'group--access':
        {'logical': 'group--access', 'prescribed': 'group--access', 'color': SECURITY_COLOR},  
    'vpn--policy':
        {'logical': 'vpn--policy', 'prescribed': 'vpn--policy', 'color': SECURITY_COLOR},  
    'code-signing-service':
        {'logical': 'code-signing-service', 'prescribed': 'code-signing-service', 'color': SECURITY_COLOR},  
    'ProfileMemory':
        {'logical': 'instance--mx', 'prescribed': 'instance--mx', 'color': COMPUTE_COLOR},  
    'hybrid-networking--alt':
        {'logical': 'hybrid-networking--alt', 'prescribed': 'hybrid-networking--alt', 'color': NETWORK_COLOR},  
    'document--unprotected':
        {'logical': 'document--unprotected', 'prescribed': 'document--unprotected', 'color': NETWORK_COLOR},  
    'InstanceBastion':
        {'logical': 'bastion-host', 'prescribed': 'bastion-host', 'color': COMPUTE_COLOR},  
    'data-blob':
        {'logical': 'data-blob', 'prescribed': 'data-blob', 'color': DATA_COLOR},  
    'object-storage--alt':
        {'logical': 'object-storage--alt', 'prescribed': 'object-storage--alt', 'color': STORAGE_COLOR},  
    'server--proxy':
        {'logical': 'server--proxy', 'prescribed': 'server--proxy', 'color': COMPUTE_COLOR},  
    'application--mobile':
        {'logical': 'application--mobile', 'prescribed': 'application--mobile', 'color': APPLICATION_COLOR},  
    'mobility--services':
        {'logical': 'mobility--services', 'prescribed': 'mobility--services', 'color': APPLICATION_COLOR},  
    'file-storage':
        {'logical': 'file-storage', 'prescribed': 'file-storage', 'color': STORAGE_COLOR},  
    'router--wifi':
        {'logical': 'router--wifi', 'prescribed': 'router--wifi', 'color': NETWORK_COLOR},  
    'intrusion-prevention':
        {'logical': 'intrusion-prevention', 'prescribed': 'intrusion-prevention', 'color': SECURITY_COLOR},  
    'edge-node--alt':
        {'logical': 'edge-node--alt', 'prescribed': 'edge-node--alt', 'color': SECURITY_COLOR},  
    'vlan--ibm':
        {'logical': 'vlan--ibm', 'prescribed': 'vlan--ibm', 'color': NETWORK_COLOR},  
    'cloud-services':
        {'logical': 'cloud-services', 'prescribed': 'cloud-services', 'color': NETWORK_COLOR},  
    'BlockStorage':
        {'logical': 'block-storage', 'prescribed': 'block-storage', 'color': STORAGE_COLOR},  
    'FloatingIP':
        {'logical': 'floating-ip', 'prescribed': 'floating-ip', 'color': NETWORK_COLOR},  
    'vehicle--connected':
        {'logical': 'vehicle--connected', 'prescribed': 'vehicle--connected', 'color': NETWORK_COLOR},  
    'group--account':
        {'logical': 'group--account', 'prescribed': 'group--account', 'color': NETWORK_COLOR},  
    'image-service':
        {'logical': 'image-service', 'prescribed': 'image-service', 'color': NETWORK_COLOR},  
    'ProfileBalanced':
        {'logical': 'instance--bx', 'prescribed': 'instance--bx', 'color': COMPUTE_COLOR},  
    'data-accessor':
        {'logical': 'data-accessor', 'prescribed': 'data-accessor', 'color': DATA_COLOR},  
    'gateway--user-access':
        {'logical': 'gateway--user-access', 'prescribed': 'gateway--user-access', 'color': SECURITY_COLOR},  
    'document--signed':
        {'logical': 'document--signed', 'prescribed': 'document--signed', 'color': DATA_COLOR},  
    'application--web':
        {'logical': 'application--web', 'prescribed': 'application--web', 'color': APPLICATION_COLOR},  
    'autoscaling':
        {'logical': 'autoscaling', 'prescribed': 'autoscaling', 'color': NETWORK_COLOR},  
    'load-balancer--listener':
        {'logical': 'load-balancer--listener', 'prescribed': 'load-balancer--listener', 'color': NETWORK_COLOR},  
    'radio--combat':
        {'logical': 'radio--combat', 'prescribed': 'radio--combat', 'color': NETWORK_COLOR},  
    'user--settings':
        {'logical': 'user--settings', 'prescribed': 'user--settings', 'color': USER_COLOR},  
    'wifi-bridge--alt':
        {'logical': 'wifi-bridge--alt', 'prescribed': 'wifi-bridge--alt', 'color': NETWORK_COLOR},  
    'point-of-presence':
        {'logical': 'point-of-presence', 'prescribed': 'point-of-presence', 'color': NETWORK_COLOR},  
    'AvailabilityZone':
        {'logical': 'data--center', 'prescribed': 'data--center', 'color': BACKEND_COLOR},  
    'sim-card':
        {'logical': 'sim-card', 'prescribed': 'sim-card', 'color': NETWORK_COLOR},  
    'chat--operational':
        {'logical': 'chat--operational', 'prescribed': 'chat--operational', 'color': NETWORK_COLOR},  
    'VPE':
        {'logical': 'ibm-cloud--vpc-endpoints', 'prescribed': 'ibm-cloud--vpc-endpoints', 'color': NETWORK_COLOR},  
    'id-management':
        {'logical': 'id-management', 'prescribed': 'id-management', 'color': MANAGEMENT_COLOR},  
    'gui--management':
        {'logical': 'gui--management', 'prescribed': 'gui--management', 'color': MANAGEMENT_COLOR},  
    'virtual-desktop':
        {'logical': 'virtual-desktop', 'prescribed': 'virtual-desktop', 'color': NETWORK_COLOR},  
    'ProfileCompute':
        {'logical': 'instance--cx', 'prescribed': 'instance--cx', 'color': COMPUTE_COLOR},  
    'phone--settings':
        {'logical': 'phone--settings', 'prescribed': 'phone--settings', 'color': NETWORK_COLOR},  
    'network--overlay':
        {'logical': 'network--overlay', 'prescribed': 'network--overlay', 'color': NETWORK_COLOR},  
    'Gateway':
        {'logical': 'gateway', 'prescribed': 'gateway', 'color': SECURITY_COLOR},  
    'document--security':
        {'logical': 'document--security', 'prescribed': 'document--security', 'color': SECURITY_COLOR},  
    'Router':
        {'logical': 'router', 'prescribed': 'router', 'color': NETWORK_COLOR},  
    'router--voice':
        {'logical': 'router--voice', 'prescribed': 'router--voice', 'color': NETWORK_COLOR},  
    'dns-services':
        {'logical': 'dns-services', 'prescribed': 'dns-services', 'color': DATA_COLOR},  
    'vlan':
        {'logical': 'vlan', 'prescribed': 'vlan', 'color': NETWORK_COLOR},  
    'server--time':
        {'logical': 'server--time', 'prescribed': 'server--time', 'color': NETWORK_COLOR},  
    'gateway--api':
        {'logical': 'gateway--api', 'prescribed': 'gateway--api', 'color': NETWORK_COLOR},  
    'wifi--secure':
        {'logical': 'wifi--secure', 'prescribed': 'wifi--secure', 'color': NETWORK_COLOR},  
    'gateway--mail':
        {'logical': 'gateway--mail', 'prescribed': 'gateway--mail', 'color': NETWORK_COLOR},  
    'PublicGateway':
        {'logical': 'gateway--public', 'prescribed': 'gateway--public', 'color': SECURITY_COLOR},  
    'phone--application':
        {'logical': 'phone--application', 'prescribed': 'phone--application', 'color': APPLICATION_COLOR},  
    'transmission-lte':
        {'logical': 'transmission-lte', 'prescribed': 'transmission-lte', 'color': NETWORK_COLOR},  
    'vehicle--insights':
        {'logical': 'vehicle--insights', 'prescribed': 'vehicle--insights', 'color': NETWORK_COLOR},  
    'ActivityTracker':
        {'logical': 'cloud--auditing', 'prescribed': 'cloud--auditing', 'color': MANAGEMENT_COLOR},  
    'hardware-security-module':
        {'logical': 'hardware-security-module', 'prescribed': 'hardware-security-module', 'color': NETWORK_COLOR},  
    'two-factor-authentication':
        {'logical': 'two-factor-authentication', 'prescribed': 'two-factor-authentication', 'color': SECURITY_COLOR},  
    'wifi-bridge':
        {'logical': 'wifi-bridge', 'prescribed': 'wifi-bridge', 'color': NETWORK_COLOR},  
    'load-balancer--classic':
        {'logical': 'load-balancer--classic', 'prescribed': 'load-balancer--classic', 'color': NETWORK_COLOR},  
    'load-balancer--local':
        {'logical': 'load-balancer--local', 'prescribed': 'load-balancer--local', 'color': NETWORK_COLOR},  
    'cloud--logging':
        {'logical': 'cloud--logging', 'prescribed': 'cloud--logging', 'color': MANAGEMENT_COLOR},  
    'data-diode':
        {'logical': 'data-diode', 'prescribed': 'data-diode', 'color': NETWORK_COLOR},  
    'folder--details':
        {'logical': 'folder--details', 'prescribed': 'folder--details', 'color': NETWORK_COLOR},  
    'gateway--security':
        {'logical': 'gateway--security', 'prescribed': 'gateway--security', 'color': SECURITY_COLOR},  
    'bare-metal-server--01':
        {'logical': 'bare-metal-server--01', 'prescribed': 'bare-metal-server--01', 'color': COMPUTE_COLOR},  
    'bare-metal-server--02':
        {'logical': 'bare-metal-server--02', 'prescribed': 'bare-metal-server--02', 'color': COMPUTE_COLOR},  
    'boot':
        {'logical': 'boot', 'prescribed': 'boot', 'color': STORAGE_COLOR},  
    'box--extra-large':
        {'logical': 'box--extra-large', 'prescribed': 'box--extra-large', 'color': NETWORK_COLOR},  
    'box--large':
        {'logical': 'box--large', 'prescribed': 'box--large', 'color': NETWORK_COLOR},  
    'box--medium':
        {'logical': 'box--medium', 'prescribed': 'box--medium', 'color': NETWORK_COLOR},  
    'box--small':
        {'logical': 'box--small', 'prescribed': 'box--small', 'color': NETWORK_COLOR},  
    'cloud-satellite--config':
        {'logical': 'cloud-satellite--config', 'prescribed': 'cloud-satellite--config', 'color': NETWORK_COLOR},  
    'cloud-satellite--link':
        {'logical': 'cloud-satellite--link', 'prescribed': 'cloud-satellite--link', 'color': NETWORK_COLOR},  
    'cloud-satellite--services':
        {'logical': 'cloud-satellite--services', 'prescribed': 'cloud-satellite--services', 'color': NETWORK_COLOR},  
    'communication--unified':
        {'logical': 'communication--unified', 'prescribed': 'communication--unified', 'color': NETWORK_COLOR},  
    'database--datastax':
        {'logical': 'database--datastax', 'prescribed': 'database--datastax', 'color': DATA_COLOR},  
    'database--elastic':
        {'logical': 'database--elastic', 'prescribed': 'database--elastic', 'color': DATA_COLOR},  
    'database--enterprisedb':
        {'logical': 'database--enterprisedb', 'prescribed': 'database--enterprisedb', 'color': DATA_COLOR},  
    'database--etcd':
        {'logical': 'database--etcd', 'prescribed': 'database--etcd', 'color': DATA_COLOR},  
    'database--mongodb':
        {'logical': 'database--mongodb', 'prescribed': 'database--mongodb', 'color': DATA_COLOR},  
    'database--postgresql':
        {'logical': 'database--postgresql', 'prescribed': 'database--postgresql', 'color': DATA_COLOR},  
    'database--rabbit':
        {'logical': 'database--rabbit', 'prescribed': 'database--rabbit', 'color': DATA_COLOR},  
    'database--redis':
        {'logical': 'database--redis', 'prescribed': 'database--redis', 'color': DATA_COLOR},  
    'directory-domain':
        {'logical': 'directory-domain', 'prescribed': 'directory-domain', 'color': NETWORK_COLOR},  
    'encryption':
        {'logical': 'encryption', 'prescribed': 'encryption', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--applications':
        {'logical': 'ibm-cloud-pak--applications', 'prescribed': 'ibm-cloud-pak--applications', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--data':
        {'logical': 'ibm-cloud-pak--data', 'prescribed': 'ibm-cloud-pak--data', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--integration':
        {'logical': 'ibm-cloud-pak--integration', 'prescribed': 'ibm-cloud-pak--integration', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--multicloud-mgmt':
        {'logical': 'ibm-cloud-pak--multicloud-mgmt', 'prescribed': 'ibm-cloud-pak--multicloud-mgmt', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--security':
        {'logical': 'ibm-cloud-pak--security', 'prescribed': 'ibm-cloud-pak--security', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--system':
        {'logical': 'ibm-cloud-pak--system', 'prescribed': 'ibm-cloud-pak--system', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--network-automation':
        {'logical': 'ibm-cloud-pak--network-automation', 'prescribed': 'ibm-cloud-pak--network-automation', 'color': NETWORK_COLOR},  
    'ibm-cloud-pak--watson-aiops':
        {'logical': 'ibm-cloud-pak--watson-aiops', 'prescribed': 'ibm-cloud-pak--watson-aiops', 'color': NETWORK_COLOR},  
    'military-camp':
        {'logical': 'military-camp', 'prescribed': 'military-camp', 'color': NETWORK_COLOR},  
    'network--admin-control':
        {'logical': 'network--admin-control', 'prescribed': 'network--admin-control', 'color': NETWORK_COLOR},  
    'pcn--e-node':
        {'logical': 'pcn--e-node', 'prescribed': 'pcn--e-node', 'color': NETWORK_COLOR},  
    'pcn--military':
        {'logical': 'pcn--military', 'prescribed': 'pcn--military', 'color': NETWORK_COLOR},  
    'pcn--p-node':
        {'logical': 'pcn--p-node', 'prescribed': 'pcn--p-node', 'color': NETWORK_COLOR},  
    'pcn--z-node':
        {'logical': 'pcn--z-node', 'prescribed': 'pcn--z-node', 'color': NETWORK_COLOR},  
    'session-border-control':
        {'logical': 'session-border-control', 'prescribed': 'session-border-control', 'color': NETWORK_COLOR},  
    'tank':
        {'logical': 'tank', 'prescribed': 'tank', 'color': NETWORK_COLOR},  
    'volume--block-storage':
        {'logical': 'volume--block-storage', 'prescribed': 'volume--block-storage', 'color': STORAGE_COLOR},  
    'volume--file-storage':
        {'logical': 'volume--file-storage', 'prescribed': 'volume--file-storage', 'color': STORAGE_COLOR},  
    'volume--object-storage':
        {'logical': 'volume--object-storage', 'prescribed': 'volume--object-storage', 'color': STORAGE_COLOR},  
    'ibm-cloud--transit-gateway':
        {'logical': 'ibm-cloud--transit-gateway', 'prescribed': 'ibm-cloud--transit-gateway', 'color': NETWORK_COLOR},  
    'enterprise':
        {'logical': 'enterprise', 'prescribed': 'enterprise', 'color': NETWORK_COLOR},  
    'Linux':
        {'logical': 'linux--alt', 'prescribed': 'linux', 'color': COMPUTE_COLOR},  
    'slicestor':
        {'logical': 'slicestor', 'prescribed': 'slicestor', 'color': STORAGE_COLOR},  
    'concept':
        {'logical': 'concept', 'prescribed': 'concept', 'color': NETWORK_COLOR},  
    'deployment-unit--data':
        {'logical': 'deployment-unit--data', 'prescribed': 'deployment-unit--data', 'color': NETWORK_COLOR},  
    'deployment-unit--execution':
        {'logical': 'deployment-unit--execution', 'prescribed': 'deployment-unit--execution', 'color': NETWORK_COLOR},  
    'deployment-unit--installation':
        {'logical': 'deployment-unit--installation', 'prescribed': 'deployment-unit--installation', 'color': NETWORK_COLOR},  
    'deployment-unit--presentation':
        {'logical': 'deployment-unit--presentation', 'prescribed': 'deployment-unit--presentation', 'color': NETWORK_COLOR},  
    'deployment-unit--technical--data':
        {'logical': 'deployment-unit--technical--data', 'prescribed': 'deployment-unit--technical--data', 'color': NETWORK_COLOR},  
    'deployment-unit--technical--execution':
        {'logical': 'deployment-unit--technical--execution', 'prescribed': 'deployment-unit--technical--execution', 'color': NETWORK_COLOR},  
    'deployment-unit--technical--installation':
        {'logical': 'deployment-unit--technical--installation', 'prescribed': 'deployment-unit--technical--installation', 'color': NETWORK_COLOR},  
    'deployment-unit--technical--presentation':
        {'logical': 'deployment-unit--technical--presentation', 'prescribed': 'deployment-unit--technical--presentation', 'color': NETWORK_COLOR}, 
    'API':
        {'logical': 'api', 'prescribed': 'api', 'color': NETWORK_COLOR},  
    'BuildTool':
        {'logical': 'build-tool', 'prescribed': 'build-tool', 'color': NETWORK_COLOR},  
    'ContinuousDeployment':
        {'logical': 'continuous-deployment', 'prescribed': 'continuous-deployment', 'color': NETWORK_COLOR},  
    'ContinuousIntegration':
        {'logical': 'continuous-integration', 'prescribed': 'continuous-integration', 'color': NETWORK_COLOR},  
    'KeyProtect':
        {'logical': 'ibm-cloud--key-protect', 'prescribed': 'ibm-cloud--key-protect', 'color': SECURITY_COLOR},  
    'SecretsManager':
        {'logical': 'ibm-cloud--secrets-manager', 'prescribed': 'ibm-cloud--secrets-manager', 'color': NETWORK_COLOR},  
    'ArtifactRepository':
        {'logical': 'repo--artifact', 'prescribed': 'repo--artifact', 'color': NETWORK_COLOR},  
    'SourceCodeRepository':
        {'logical': 'repo--source-code', 'prescribed': 'repo--source-code', 'color': NETWORK_COLOR},  
    'ServiceID':
        {'logical': 'service-id', 'prescribed': 'service-id', 'color': NETWORK_COLOR},  
    'TestTool':
        {'logical': 'test-tool', 'prescribed': 'test-tool', 'color': NETWORK_COLOR}  
  }
