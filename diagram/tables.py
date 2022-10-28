# @file tables.py
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

from diagram.icons import icons

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
    'Cloud': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['Cloud']},
    'EnterpriseNetwork': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['EnterpriseNetwork']},
    'PublicNetwork': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['PublicNetwork']},
    'Region': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['location'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['Region']},
    'Subnet': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group3'], 'size': minsizes['group'], 'icon': icons['Subnet']},
    'VPC': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['network'], 'style': styles['group'], 'size': minsizes['group'], 'icon': icons['VPC']},
    'Zone': {'format': formats['group'], 'layout': layouts['group'], 'color': expandedColors['location'], 'style': styles['group3'], 'size': minsizes['group'], 'icon': icons['Zone']},

    # Expanded Icons
    'InstanceExpanded': {'format': formats['node'], 'layout': layouts['expanded'], 'color': expandedColors['compute'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['InstanceVirtual']},
    'InstanceBastionExpanded': {'format': formats['node'], 'layout': layouts['expanded'], 'color': expandedColors['security'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['InstanceBastion']},
    'InstanceExpandedStack': {'format': formats['node'], 'layout': layouts['expandedStack'], 'color': expandedColors['compute'], 'style': styles['iconExpandedStack3'], 'size': minsizes['expanded'], 'icon': icons['InstanceVirtual']},
    'InstanceBastionExpandedStack': {'format': formats['node'], 'layout': layouts['expandedStack'], 'color': expandedColors['security'], 'style': styles['iconExpanded3'], 'size': minsizes['expanded'], 'icon': icons['InstanceBastion']},

    # Collapsed Icons
    'Instance': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['compute'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['InstanceVirtual']},
    'InstanceBastion': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['InstanceBastion']},
    'FloatingIP': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['FloatingIP']},
    'Internet': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['Internet']},
    'LoadBalancer': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['LoadBalancer']},
    'PublicGateway': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['PublicGateway']},
    'Router': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['Router']},
    'User': {'format': formats['actor'], 'layout': layouts['collapsed'], 'color': collapsedColors['actor'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['User']},
    'VPNConnection': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['VPNConnection']},
    'VPNGateway': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['security'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['VPNGateway']},
    'VPE': {'format': formats['node'], 'layout': layouts['collapsed'], 'color': collapsedColors['network'], 'style': styles['icon'], 'size': minsizes['collapsed'], 'icon': icons['VPE']},

    # Item Icons

    # Item Icons
    'OperatingSystem': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['Linux']},
    'ProfileBalanced': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['ProfileBalanced']},
    'ProfileCompute': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['ProfileCompute']},
    'ProfileMemory': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['ProfileMemory']},
    'BlockStorage': {'format': formats['node'], 'layout': layouts['itemIcon'], 'color': collapsedColors['item'], 'style': styles['item'], 'size': minsizes['item'], 'icon': icons['BlockStorage']},

    # Text
    'Text': {'style': styles['text']}
}

# Names Table

names = {
   'InternetName': 'Internet',
   'PublicNetworkName': 'Public<br>Network',
   'PublicUserName': 'User',
   'EnterpriseNetworkName': 'Enterprise<br>Network',
   'EnterpriseUserName': 'Enterprise User'
}

# Points Table

points = {
   'IconWidth': 48,
   'IconHeight': 48,

   'GroupWidth': 240,
   'GroupHeight': 152,

   'MinGroupWidth': 240,
   'MinGroupHeight': 48,

   'GroupSpace': 30,
   'TopSpace': 70,
   'TextGroupSpace': 10,
   'TextTopSpace': 70,
   'IconSpace': 48,

   'LeftSpace': 0,

   # Public network icon locations:
   #    First x,y is User icon.
   #    Second x,y is Internet icon.

   # Enterprse network icon locations:
   #    First x,y is User icon.

   # VPC icon locations:
   #    First x,y is Router icon.
   #    Second x,y is ALB icon.
   #    Third x,y is VPN Gateway icon.

   # Zone icon locations:
   #    First x,y is Public Gateway icon.
   #    Second x,y is NLB icon.

   'FirstIconX': 0,
   'FirstIconY': 0,

   'SecondIconX': 0,
   'SecondIconY': 0,

   'ThirdIconX': 0,
   'ThirdIconY': 0,

   'FourthIconX': 0,
   'FourthIconY': 0,

   'PublicIconCount': 2,
   'PublicNetworkWidth': 0,
   'PublicNetworkHeight': 0,

   'EnterpriseIconCount': 1,
   'EnterpriseNetworkWidth': 0,
   'EnterpriseNetworkHeight': 0
}

points['LeftSpace'] = points['IconSpace'] * 3

points['FirstIconX'] = points['IconSpace']
points['FirstIconY'] = points['TopSpace']

points['SecondIconX'] = points['IconSpace']
points['SecondIconY'] = points['FirstIconY'] + points['IconHeight'] + points['IconSpace']

points['ThirdIconX'] = points['IconSpace']
points['ThirdIconY'] = points['SecondIconY'] + points['IconHeight'] + points['IconSpace']

points['FourthIconX'] = points['IconSpace']
points['FourthIconY'] = points['ThirdIconY'] + points['IconHeight'] + points['IconSpace']

points['PublicNetworkWidth'] = points['IconSpace'] * 3
points['PublicNetworkHeight'] = points['TopSpace'] + (points['IconSpace'] * points['PublicIconCount']) + (points['IconHeight'] * points['PublicIconCount'])

points['EnterpriseNetworkWidth'] = points['IconSpace'] * 3
points['EnterpriseNetworkHeight'] = points['TopSpace'] + (points['IconSpace'] * points['EnterpriseIconCount']) + (points['IconHeight'] * points['EnterpriseIconCount'])

# Zone CIDR Table

zoneCIDRs = {
   'au-syd-1': '10.245.0.0/18',
   'au-syd-2': '10.245.64.0/18',
   'au-syd-3': '10.245.128.0/18',

   'br-sao-1': '10.250.0.0/18',
   'br-sao-2': '10.250.64.0/18',
   'br-sao-3': '10.250.128.0/18',

   'ca-tor-1': '10.249.0.0/18',
   'ca-tor-2': '10.249.64.0/18',
   'ca-tor-3': '10.249.128.0/18',

   'eu-de-1': '10.243.0.0/18',
   'eu-de-2': '10.243.64.0/18',
   'eu-de-3': '10.243.128.0/18',

   'eu-gb-1': '10.242.0.0/18',
   'eu-gb-2': '10.242.64.0/18',
   'eu-gb-3': '10.242.128.0/18',

   'jp-osa-1': '10.248.0.0/18',
   'jp-osa-2': '10.248.64.0/18',
   'jp-osa-3': '10.248.128.0/18',

   'jp-tok-1': '10.244.0.0/18',
   'jp-tok-2': '10.244.64.0/18',
   'jp-tok-3': '10.244.128.0/18',

   'us-east-1': '10.241.0.0/18',
   'us-east-2': '10.241.64.0/18',
   'us-east-3': '10.241.128.0/18',

   'us-south-1': '10.240.0.0/18',
   'us-south-2': '10.240.64.0/18',
   'us-south-3': '10.240.128.0/18'
}
