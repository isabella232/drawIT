# @file constants.py
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

# Format Properties

ACTOR_FORMAT = 'shape=mxgraph.ibm.base;ibmType=actor;'
LOGICAL_COMPONENT_FORMAT = 'shape=mxgraph.ibm.base;ibmType=compl;'
PRESCRIBED_COMPONENT_FORMAT = 'shape=mxgraph.ibm.base;ibmType=compp;'
LOGICAL_LOCATION_FORMAT = 'shape=mxgraph.ibm.base;ibmType=groupl;'
PRESCRIBED_LOCATION_FORMAT = 'shape=mxgraph.ibm.base;ibmType=groupp;'
LOGICAL_NODE_FORMAT = 'shape=mxgraph.ibm.base;ibmType=nodel;'
PRESCRIBED_NODE_FORMAT = 'shape=mxgraph.ibm.base;ibmType=nodep;'

# Layout Properties

COLLAPSED_LAYOUT = 'ibmLayout=collapsed;'
EXPANDED_LAYOUT = 'ibmLayout=expanded;'
EXPANDED_STACK_LAYOUT ='ibmLayout=expandedStack;'
LOCATION_LAYOUT = 'ibmLayout=expanded;'
ITEM_ICON_LAYOUT = 'ibmLayout=itemIcon;'

# Size Properties

COLLAPSED_SIZE = {'width': '48', 'height': '48'}
EXPANDED_SIZE = {'width': '240', 'height': '48'}
LOCATION_SIZE = {'width': '240', 'height': '152'}
ITEM_SIZE = {'width': '252', 'height': '16'}

# Style Properties

BASIC_STYLE = 'html=1;metaEdit=1;whiteSpace=wrap;image=;'
FONT_STYLE = 'fontFamily=IBM Plex Sans;fontSize=14;fontColor=#000000;'
CONTAINER_STYLE = 'container=1;collapsible=0;expand=0;recursiveResize=0;'

COLLAPSED_LABEL_STYLE = 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
COLLAPSED_LABEL3_STYLE = 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
EXPANDED_LABEL_STYLE = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
EXPANDED_LABEL3_STYLE = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
ITEM_LABEL_STYLE = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=0;spacingRight=0;spacingTop=0;spacingBottom=0;'

EXPANDED_STACK_STYLE = 'childLayout=stackLayout;horizontalStack=0;stackFill=1;stackSpacing=8;marginLeft=16;marginRight=8;marginTop=64;marginBottom=8;'

ICON_STYLE = BASIC_STYLE + FONT_STYLE + COLLAPSED_LABEL_STYLE
ICON3_STYLE = BASIC_STYLE + FONT_STYLE + COLLAPSED_LABEL3_STYLE
ICON_EXPANDED_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL_STYLE + CONTAINER_STYLE
ICON_EXPANDED3_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL3_STYLE + CONTAINER_STYLE
ICON_EXPANDED_STACK_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL_STYLE + EXPANDED_STACK_STYLE + CONTAINER_STYLE
ICON_EXPANDED_STACK3_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL3_STYLE + EXPANDED_STACK_STYLE + CONTAINER_STYLE
LOCATION_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL_STYLE + CONTAINER_STYLE
LOCATION3_STYLE = BASIC_STYLE + FONT_STYLE + EXPANDED_LABEL3_STYLE + CONTAINER_STYLE
ITEM_STYLE = BASIC_STYLE + FONT_STYLE + ITEM_LABEL_STYLE
TEXT_STYLE = 'text;html=1;resizable=0;autosize=1;align=left;verticalAlign=middle;points=[];strokeColor=none;rounded=0;'

# Shape Properties

ACTOR_STYLE = ACTOR_FORMAT + COLLAPSED_LAYOUT + ICON_STYLE

LOGICAL_NODE_STYLE = LOGICAL_NODE_FORMAT + COLLAPSED_LAYOUT + ICON_STYLE
PRESCRIBED_NODE_STYLE = PRESCRIBED_NODE_FORMAT + COLLAPSED_LAYOUT + ICON_STYLE

LOGICAL_COMPONENT_STYLE = LOGICAL_COMPONENT_FORMAT + COLLAPSED_LAYOUT + ICON_STYLE
PRESCRIBED_COMPONENT_STYLE = PRESCRIBED_COMPONENT_FORMAT + COLLAPSED_LAYOUT + ICON_STYLE

LOGICAL_LOCATION_STYLE = LOGICAL_LOCATION_FORMAT + LOCATION_LAYOUT + LOCATION_STYLE  
PRESCRIBED_LOCATION_STYLE = PRESCRIBED_LOCATION_FORMAT + LOCATION_LAYOUT + LOCATION_STYLE  

# Color Properties

BLACK_COLOR = 'strokeColor=#000000;'
BLUE_COLOR = 'strokeColor=#0f62fe;'
CYAN_COLOR = 'strokeColor=#1192e8;'
GRAY_COLOR = 'strokeColor=#878d96;'
GREEN_COLOR = 'strokeColor=#198038;'
MAGENTA_COLOR = 'strokeColor=#ee5396;'
PURPLE_COLOR = 'strokeColor=#a56eff'
RED_COLOR = 'strokeColor=#fa4d56;'
TEAL_COLOR = 'strokeColor=#009d9a;'

BLACK_FILL = 'fillColor=#f2f4f8;'
BLUE_FILL = 'fillColor=#edf5ff;'
CYAN_FILL = 'fillColor=#e5f6ff;'
GRAY_FILL = 'fillColor=#f2f4f8;'
GREEN_FILL = 'fillColor=#defbe6;'
MAGENTA_FILL = 'fillColor=#fff0f7;'
PURPLE_FILL = 'fillColor=#f6f2ff'
TEAL_FILL = 'fillColor=#d9fbfb;'
RED_FILL = 'fillColor=#fff1f1;'
WHITE_FILL = 'fillColor=#ffffff;'
NO_FILL = 'fillColor=none;'

APPLICATION_COLOR = PURPLE_COLOR
BACKEND_COLOR = GRAY_COLOR
COMPUTE_COLOR = GREEN_COLOR
DATA_COLOR = BLUE_COLOR
DEVOP_COLOR = MAGENTA_COLOR
MANAGEMENT_COLOR = TEAL_COLOR
NETWORK_COLOR = CYAN_COLOR
SECURITY_COLOR = RED_COLOR
STORAGE_COLOR = BLUE_COLOR
USER_COLOR = BLACK_COLOR

APPLICATION_FILL = PURPLE_FILL
BACKEND_FILL = GRAY_FILL
COMPUTE_FILL = GREEN_FILL
DATA_FILL = BLUE_FILL
DEVOP_FILL = MAGENTA_FILL
MANAGEMENT_FILL = TEAL_FILL
NETWORK_FILL = CYAN_FILL
SECURITY_FILL = RED_FILL
STORAGE_FILL = BLUE_FILL
USER_FILL = BLACK_FILL

# Name Constants

INTERNET_NAME = 'Internet'
PUBLIC_NETWORK_NAME = 'Public<br>Network'
PUBLIC_USER_NAME = 'User'
ENTERPRISE_NETWORK_NAME = 'Enterprise<br>Network'
ENTERPRISE_USER_NAME = 'Enterprise User'

ACTOR_KIND = 'actor'
LOCATION_KIND = 'location'
NODE_KIND = 'node'
LOGICAL_KIND = 'logical'
PRESCRIBED_KIND = 'prescribed'

# Positioning Constants

NO_PARENT = '1'

ICON_WIDTH = 48
ICON_HEIGHT = 48

GROUP_WIDTH = 240
GROUP_HEIGHT = 152

MIN_GROUP_WIDTH = 240
MIN_GROUP_HEIGHT = 48

GROUP_SPACE = 30
TOP_SPACE = 70
TEXT_GROUP_SPACE = 10
TEXT_TOP_SPACE = 70
ICON_SPACE = 48

LEFT_SPACE = ICON_SPACE * 3

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

FIRST_ICON_X = ICON_SPACE
FIRST_ICON_Y = TOP_SPACE

SECOND_ICON_X = ICON_SPACE
SECOND_ICON_Y = FIRST_ICON_Y + ICON_HEIGHT + ICON_SPACE

THIRD_ICON_X = ICON_SPACE
THIRD_ICON_Y = SECOND_ICON_Y + ICON_HEIGHT + ICON_SPACE

FOURTH_ICON_X = ICON_SPACE
FOURTH_ICON_Y = THIRD_ICON_Y + ICON_HEIGHT + ICON_SPACE

PUBLIC_ICON_COUNT = 2
PUBLIC_NETWORK_WIDTH = ICON_SPACE * 3
PUBLIC_NETWORK_HEIGHT = TOP_SPACE + (ICON_SPACE * PUBLIC_ICON_COUNT) + (ICON_HEIGHT * PUBLIC_ICON_COUNT)

ENTERPRISE_ICON_COUNT = 1
ENTERPRISE_NETWORK_WIDTH = ICON_SPACE * 3
ENTERPRISE_NETWORK_HEIGHT = TOP_SPACE + (ICON_SPACE * ENTERPRISE_ICON_COUNT) + (ICON_HEIGHT * ENTERPRISE_ICON_COUNT)

# Zone CIDRs

AU_SYD_1 = '10.245.0.0/18'
AU_SYD_2 = '10.245.64.0/18'
AU_SYD_3 = '10.245.128.0/18'

BR_SAO_1 = '10.250.0.0/18'
BR_SAO_2 = '10.250.64.0/18'
BR_SAO_3 = '10.250.128.0/18'

CA_TOR_1 = '10.249.0.0/18'
CA_TOR_2 = '10.249.64.0/18'
CA_TOR_3 = '10.249.128.0/18'

EU_DE_1 = '10.243.0.0/18'
EU_DE_2 = '10.243.64.0/18'
EU_DE_3 = '10.243.128.0/18'

EU_GB_1 = '10.242.0.0/18'
EU_GB_2 = '10.242.64.0/18'
EU_GB_3 = '10.242.128.0/18'

JP_OSA_1 = '10.248.0.0/18'
JP_OSA_2 = '10.248.64.0/18'
JP_OSA_3 = '10.248.128.0/18'

JP_TOK_1 = '10.244.0.0/18'
JP_TOK_2 = '10.244.64.0/18'
JP_TOK_3 = '10.244.128.0/18'

US_EAST_1 = '10.241.0.0/18'
US_EAST_2 = '10.241.64.0/18'
US_EAST_3 = '10.241.128.0/18'

US_SOUTH_1 = '10.240.0.0/18'
US_SOUTH_2 = '10.240.64.0/18'
US_SOUTH_3 = '10.240.128.0/18'
