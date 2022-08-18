# @file constants.py
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

class Constants:
   toolName = 'drawIT'
   toolVersion = '0.5.9'
   toolCopyright = toolName + ' ' + toolVersion + ' - Copyright 2022 IBM Corporation'

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

   iconWidth = 48
   iconHeight = 48

   groupWidth = 240
   groupHeight = 152

   minGroupWidth = 240
   minGroupHeight = 48

   groupSpace = 30
   topSpace = 70
   textGroupSpace = 10
   textTopSpace = 70
   iconSpace = 48
   leftSpace = iconSpace * 3

   firstIconX = 0
   firstIconY = 0

   secondIconX = 0
   secondIconY = 0

   publicIconCount = 0
   publicNetworkWidth = 0
   publicNetworkHeight = 0

   enterpriseIconCount = 0
   enterpriseNetworkWidth = 0
   enterpriseNetworkHeight = 0

   internetName = 'Internet'
   publicNetworkName = 'Public<br>Network'
   publicUserName = 'User'
   enterpriseNetworkName = 'Enterprise<br>Network'
   enterpriseUserName = 'Enterprise User'

   def __init__(self):
      self.firstIconX = self.iconSpace
      self.firstIconY = self.topSpace

      self.secondIconX = self.iconSpace
      self.secondIconY = self.firstIconY + self.iconHeight + self.iconSpace

      self.publicIconCount = 2
      self.publicNetworkWidth = self.iconSpace * 3
      self.publicNetworkHeight = self.topSpace + (self.iconSpace * self.publicIconCount) + (self.iconHeight * self.publicIconCount)

      self.enterpriseIconCount = 1
      self.enterpriseNetworkWidth = self.iconSpace * 3
      self.enterpriseNetworkHeight = self.topSpace + (self.iconSpace * self.enterpriseIconCount) + (self.iconHeight * self.enterpriseIconCount)

      return

   def getToolName(self):
      return self.toolName

   def getToolVersion(self):
      return self.toolVersion

   def getToolCopyright(self):
      return self.toolCopyright

   def getZoneCIDRs(self):
      return self.zoneCIDRs

   def getZoneCIDR(self, zone):
      return self.zoneCIDRs[zone]

   def getIconWidth(self):
      return self.iconWidth

   def getIconHeight(self):
      return self.iconHeight

   def getGroupWidth(self):
      return self.groupWidth

   def getGroupHeight(self):
      return self.groupHeight

   def getMinGroupWidth(self):
      return self.minGroupWidth

   def getMinGroupHeight(self):
      return self.minGroupHeight

   def getGroupSpace(self):
      return self.groupSpace

   def getTopSpace(self):
      return self.topSpace

   def getTextGroupSpace(self):
      return self.textGroupSpace

   def getTextTopSpace(self):
      return self.textTopSpace

   def getIconSpace(self):
      return self.iconSpace

   def getLeftSpace(self):
      return self.leftSpace

   def getFirstIconX(self):
      return self.firstIconX

   def getFirstIconY(self):
      return self.firstIconY

   def getSecondIconX(self):
      return self.secondIconX

   def getSecondIconY(self):
      return self.secondIconY

   def getPublicIconCount(self):
      return self.publicIconCount

   def getPublicNetworkWidth(self):
      return self.publicNetworkWidth

   def getPublicNetworkHeight(self):
      return self.publicNetworkHeight

   def getEnterpriseIconCount(self):
      return self.enterpiseIconCount

   def getEnterpriseNetworkWidth(self):
      return self.enterpriseNetworkWidth

   def getEnterpriseNetworkHeight(self):
      return self.enterpriseNetworkHeight

   def getInternetName(self):
      return self.internetName

   def getPublicNetworkName(self):
      return self.publicNetworkName

   def getPublicUserName(self):
      return self.publicUserName

   def getEnterpriseNetworkName(self):
      return self.enterpriseNetworkName

   def getEnterpriseUserName(self):
      return self.enterpriseUserName
