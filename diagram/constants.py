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

from enum import Enum

# Format Properties

class ShapeFormat(Enum):
   ACTOR = 'shape=mxgraph.ibm.base;ibmType=actor;'
   LOGICAL_COMPONENT = 'shape=mxgraph.ibm.base;ibmType=compl;'
   PRESCRIBED_COMPONENT = 'shape=mxgraph.ibm.base;ibmType=compp;'
   LOGICAL_LOCATION = 'shape=mxgraph.ibm.base;ibmType=groupl;'
   PRESCRIBED_LOCATION = 'shape=mxgraph.ibm.base;ibmType=groupp;'
   LOGICAL_NODE = 'shape=mxgraph.ibm.base;ibmType=nodel;'
   PRESCRIBED_NODE = 'shape=mxgraph.ibm.base;ibmType=nodep;'

# Layout Properties

class ShapeLayout(Enum):
   COLLAPSED = 'ibmLayout=collapsed;'
   EXPANDED = 'ibmLayout=expanded;'
   EXPANDED_STACK ='ibmLayout=expandedStack;'
   LOCATION = 'ibmLayout=expanded;'
   ITEM_ICON = 'ibmLayout=itemIcon;'

# Size Properties

class ShapeSize(Enum):
   COLLAPSED = {'width': '48', 'height': '48'}
   EXPANDED = {'width': '240', 'height': '48'}
   LOCATION = {'width': '240', 'height': '152'}
   ITEM = {'width': '252', 'height': '16'}

# Base Properties

class BaseStyle(Enum):
   BASIC = 'html=1;metaEdit=1;whiteSpace=wrap;image=;'
   FONT = 'fontFamily=IBM Plex Sans;fontSize=14;fontColor=#000000;'
   CONTAINER = 'container=1;collapsible=0;expand=0;recursiveResize=0;'

   COLLAPSED_LABEL = 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
   COLLAPSED_LABEL3 = 'align=center;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
   EXPANDED_LABEL = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
   EXPANDED_LABEL3 = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=16;spacingRight=16;spacingTop=0;spacingBottom=4;'
   ITEM_LABEL = 'align=left;verticalAlign=middle;labelPosition=center;verticalLabelPosition=middle;spacing=0;spacingLeft=0;spacingRight=0;spacingTop=0;spacingBottom=0;'

   EXPANDED_STACK = 'childLayout=stackLayout;horizontalStack=0;stackFill=1;stackSpacing=8;marginLeft=16;marginRight=8;marginTop=64;marginBottom=8;'

# Combined Properties

class CombinedStyle(Enum):
   ICON = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.COLLAPSED_LABEL.value
   ICON3 = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.COLLAPSED_LABEL3.value
   ICON_EXPANDED = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL.value + BaseStyle.CONTAINER.value
   ICON_EXPANDED3 = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL3.value + BaseStyle.CONTAINER.value
   ICON_EXPANDED_STACK = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL.value + BaseStyle.EXPANDED_STACK.value + BaseStyle.CONTAINER.value
   ICON_EXPANDED_STACK3 = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL3.value + BaseStyle.EXPANDED_STACK.value + BaseStyle.CONTAINER.value
   LOCATION = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL.value + BaseStyle.CONTAINER.value
   LOCATION3 = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.EXPANDED_LABEL3.value + BaseStyle.CONTAINER.value
   ITEM = BaseStyle.BASIC.value + BaseStyle.FONT.value + BaseStyle.ITEM_LABEL.value
   TEXT = 'text;html=1;resizable=0;autosize=1;align=left;verticalAlign=middle;points=[];strokeColor=none;rounded=0;'

# Shape Properties

class ShapeStyle(Enum):
   ACTOR = ShapeFormat.ACTOR.value + ShapeLayout.COLLAPSED.value + CombinedStyle.ICON.value

   LOGICAL_NODE = ShapeFormat.LOGICAL_NODE.value + ShapeLayout.COLLAPSED.value + CombinedStyle.ICON.value
   PRESCRIBED_NODE = ShapeFormat.PRESCRIBED_NODE.value + ShapeLayout.COLLAPSED.value + CombinedStyle.ICON.value

   LOGICAL_COMPONENT = ShapeFormat.LOGICAL_COMPONENT.value + ShapeLayout.COLLAPSED.value + CombinedStyle.ICON.value
   PRESCRIBED_COMPONENT = ShapeFormat.PRESCRIBED_COMPONENT.value + ShapeLayout.COLLAPSED.value + CombinedStyle.ICON.value

   LOGICAL_LOCATION = ShapeFormat.LOGICAL_LOCATION.value + ShapeLayout.LOCATION.value + CombinedStyle.LOCATION.value  
   PRESCRIBED_LOCATION = ShapeFormat.PRESCRIBED_LOCATION.value + ShapeLayout.LOCATION.value + CombinedStyle.LOCATION.value  

# Color Properties

class ColorPalette(Enum):
   BLACK = 'strokeColor=#000000;'
   BLUE = 'strokeColor=#0f62fe;'
   CYAN = 'strokeColor=#1192e8;'
   GRAY = 'strokeColor=#878d96;'
   GREEN = 'strokeColor=#198038;'
   MAGENTA = 'strokeColor=#ee5396;'
   PURPLE = 'strokeColor=#a56eff'
   RED = 'strokeColor=#fa4d56;'
   TEAL = 'strokeColor=#009d9a;'

class FillPalette(Enum):
   BLACK = 'fillColor=#f2f4f8;'
   BLUE = 'fillColor=#edf5ff;'
   CYAN = 'fillColor=#e5f6ff;'
   GRAY = 'fillColor=#f2f4f8;'
   GREEN = 'fillColor=#defbe6;'
   MAGENTA = 'fillColor=#fff0f7;'
   PURPLE = 'fillColor=#f6f2ff'
   TEAL = 'fillColor=#d9fbfb;'
   RED = 'fillColor=#fff1f1;'
   WHITE = 'fillColor=#ffffff;'
   NONE = 'fillColor=none;'

class ComponentColor(Enum): 
   APPLICATION = ColorPalette.PURPLE.value
   BACKEND = ColorPalette.GRAY.value
   COMPUTE = ColorPalette.GREEN.value
   DATA = ColorPalette.BLUE.value
   DEVOP = ColorPalette.MAGENTA.value
   MANAGEMENT = ColorPalette.TEAL.value
   NETWORK = ColorPalette.CYAN.value
   SECURITY = ColorPalette.RED.value
   STORAGE = ColorPalette.BLUE.value
   USER = ColorPalette.BLACK.value

class ComponentFill(Enum):
   APPLICATION = FillPalette.PURPLE.value
   BACKEND = FillPalette.GRAY.value
   COMPUTE = FillPalette.GREEN.value
   DATA = FillPalette.BLUE.value
   DEVOP = FillPalette.MAGENTA.value
   MANAGEMENT = FillPalette.TEAL.value
   NETWORKL = FillPalette.CYAN.value
   SECURITY = FillPalette.RED.value
   STORAGE = FillPalette.BLUE.value
   USER = FillPalette.BLACK.value

class ShapeKind(Enum):
   ACTOR = 'actor'
   NODE = 'node'
   COMPONENT = 'component'
   LOCATION = 'location'
   ZONE = 'zone'
#   LOGICAL = 'logical'
#   PRESCRIBED = 'prescribed'

# Name Constants

class ShapeName(Enum):
   INTERNET = 'Internet'
   PUBLIC_NETWORK = 'Public<br>Network'
   PUBLIC_USER = 'User'
   ENTERPRISE_NETWORK = 'Enterprise<br>Network'
   ENTERPRISE_USER = 'Enterprise User'
   NO_PARENT = '1'

# Positioning Constants

class ShapePos(Enum):
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

class ZoneCIDR(Enum):
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

   NONE = ''
