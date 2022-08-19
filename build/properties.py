# @file properties.py
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

# Icons Table

icons = {
    'cloud': {'logical': 'cloud', 'prescribed': 'ibm-cloud'},
    'enterpriseNetwork': {'logical': 'network--enterprise', 'prescribed': 'network--enterprise'},
    'floatingIP': {'logical': 'floating-ip', 'prescribed': 'floating-ip'},
    'instance': {'logical': 'virtual-machine', 'prescribed': 'instance--virtual'},
    'instanceBastion': {'logical': 'bastion-host', 'prescribed': 'bastion-host'},
    'internet': {'logical': 'wikis', 'prescribed': 'wikis'},
    'loadBalancer': {'logical': 'load-balancer--vpc', 'prescribed': 'load-balancer--vpc'},
    'publicGateway': {'logical': 'gateway--public', 'prescribed': 'gateway--public'},
    'publicNetwork': {'logical': 'network--public', 'prescribed': 'network--public'},
    'region': {'logical': 'location', 'prescribed': 'location'},
    'router': {'logical': 'router', 'prescribed': 'router'},
    'subnet': {'logical': 'locked', 'prescribed': 'ibm-cloud--subnets'},
    'user': {'logical': 'user', 'prescribed': 'user'},
    'vpc': {'logical': 'virtual-private-cloud', 'prescribed': 'virtual-private-cloud--alt'},
    'vpnConnection': {'logical': 'vpn--connection', 'prescribed': 'vpn--connection'},
    'vpnGateway': {'logical': 'gateway--vpn', 'prescribed': 'gateway--vpn'},
    'zone': {'logical': 'data--center', 'prescribed': 'data--center'},

    'linux': {'logical': 'linux', 'prescribed': 'linux'},
    'profileBalanced': {'logical': 'instance--bx', 'prescribed': 'instance--bx'},
    'profileCompute': {'logical': 'instance--cx', 'prescribed': 'instance--cx'},
    'profileMemory': {'logical': 'instance--mx', 'prescribed': 'instance--mx'},
    'blockStorage': {'logical': 'block-storage', 'prescribed': 'block-storage'}
}

# Format Properties

formats = {
    'actor': {'logical': 'shape=mxgraph.ibm.base;ibmType=actor;', 'prescribed': 'shape=mxgraph.ibm.base;ibmType=actor;'},
    'component': {'logical': 'shape=mxgraph.ibm.base;ibmType=compl;', 'prescribed': 'shape=mxgraph.ibm.base;ibmType=compp;'},
    'group': {'logical': 'shape=mxgraph.ibm.base;ibmType=groupl;', 'prescribed': 'shape=mxgraph.ibm.base;ibmType=groupp;'},
    'node': {'logical': 'shape=mxgraph.ibm.base;ibmType=nodel;', 'prescribed': 'shape=mxgraph.ibm.base;ibmType=nodep;'}
}

# Layout Properties

layouts = {
    'collapsed': 'ibmLayout=collapsed;',
    'expanded': 'ibmLayout=expanded;',
    'expandedStack': 'ibmLayout=expandedStack;',
    'group': 'ibmLayout=expanded;',
    'itemIcon': 'ibmLayout=itemIcon;'
}

# Size Properties

minsizes = {
    'collapsed': {'width': '48', 'height': '48'},
    'expanded': {'width': '240', 'height': '48'},
    'group': {'width': '240', 'height': '152'},
    'item': {'width': '252', 'height': '16'}
}

# Style Properties

basic = 'html=1;metaEdit=1;whiteSpace=wrap;image=;'
font = 'fontFamily=IBM Plex Sans;fontSize=14;fontColor=#000000;'
container = 'container=1;collapsible=0;expand=0;recursiveResize=0;'

labels = {
        'collapsedLabel': 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;',
        'collapsedLabel3': 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;',
        'expandedLabel': 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;',
        'expandedLabel3': 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;',
        'itemLabel': 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=0;spacingRight=0;spacingTop=0;spacingBottom=0;'}

stack = {
        'expandedStack': 'childLayout=stackLayout;horizontalStack=0;stackFill=1;stackSpacing=8;marginLeft=16;marginRight=8;marginTop=64;marginBottom=8;'}

styles = {
    'icon': basic + font +  labels['collapsedLabel'],
    'icon3': basic + font +  labels['collapsedLabel3'],
    'iconExpanded': basic + font +  labels['expandedLabel'] + container,
    'iconExpanded3': basic + font +  labels['expandedLabel3'] + container,
    'iconExpandedStack': basic + font +  labels['expandedLabel'] + stack['expandedStack'] + container,
    'iconExpandedStack3': basic + font +  labels['expandedLabel3'] + stack['expandedStack'] + container,
    'group': basic + font +  labels['expandedLabel'] + container,
    'group3': basic + font +  labels['expandedLabel3'] + container,
    'item': basic + font +  labels['itemLabel'],
    'text': 'text;html=1;resizable=0;autosize=1;align=left;verticalAlign=middle;points=[];strokeColor=none;rounded=0;'}


# Color Properties

expandedColors = {
    'compute': 'strokeColor=#198038;fillColor=#defbe6;',
    'group': 'strokeColor=#009d9a;fillColor=#ffffff;',
    'location': 'strokeColor=#878d96;fillColor=#f2f4f8;',
    'network': 'strokeColor=#1192e8;fillColor=#ffffff;',
    'security': 'strokeColor=#fa4d56;fillColor=#fff1f1;'}

collapsedColors = {
    'actor': 'strokeColor=#000000;fillColor=none;',
    'compute': 'strokeColor=#198038;fillColor=none;',
    'group': 'strokeColor=#009d9a;fillColor=none;',
    'location': 'strokeColor=#878d96;fillColor=none;',
    'network': 'strokeColor=#1192e8;fillColor=none;',
    'security': 'strokeColor=#fa4d56;fillColor=none;',
    'item': 'strokeColor=#198038;fillColor=none;'}

# Shape Table

ibmshapes = {
    # Groups
    'cloud': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['cloud']},
    'enterpriseNetwork': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['enterpriseNetwork']},
    'publicNetwork': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['publicNetwork']},
    'region': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['location'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['region']},
    'subnet': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group3'], 'size': minsizes['group'], 'icon': icons['subnet']},
    'vpc': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['vpc']},
    'zone': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['location'], 'style': styles['group3'], 'size': minsizes['group'], 'icon': icons['zone']},

    # Expanded Icons
    'instanceExpanded': {'format': formats['node'], 'layout': layouts['expanded'], 'color': expandedColors['compute'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['instance']},
    'instanceBastionExpanded': {'format': formats['node'], 'layout': layouts['expanded'], 'color': expandedColors['security'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['instanceBastion']},
    'instanceExpandedStack': {'format': formats['node'], 'layout': layouts['expandedStack'], 'color': expandedColors['compute'], 'style': styles['iconExpandedStack3'], 'size': minsizes['expanded'], 'icon': icons['instance']},
    'instanceBastionExpandedStack': {'format': formats['node'], 'layout': layouts['expandedStack'], 'color': expandedColors['security'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['instanceBastion']},

    # Collapsed Icons
    'instance': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['compute'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['instance']},
    'instanceBastion': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['instanceBastion']},
    'floatingIP': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['floatingIP']},
    'internet': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['internet']},
    'loadBalancer': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['loadBalancer']},
    'publicGateway': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['publicGateway']},
    'router': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['router']},
    'user': {'format': formats['actor'], 'layout': layouts['collapsed'], 'color': collapsedColors['actor'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['user']},
    'vpnConnection': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['vpnConnection']},
    'vpnGateway': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['vpnGateway']},

    # Item Icons
    'operatingSystem': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['linux']},
    'profileBalanced': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['profileBalanced']},
    'profileCompute': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['profileCompute']},
    'profileMemory': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['profileMemory']},
    'blockStorage': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['blockStorage']},

    # Text
    'text': {'style': styles['text']}
}

