# @file options.py
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
from os import path

class CloudType(Enum):
   IBM = 'ibm'
   AWS = 'aws'

class RunMode(Enum):
   BATCH = 'batch'
   GUI = 'gui'
   WEB = 'web'
   TERRAFORM = 'terraform'

class InputType(Enum):
   RIAS = 'rias'
   JSON = 'json'
   YAML = 'yaml'

class OutputSplit(Enum):
   SINGLE = 'single'
   COMBINE = 'combine'
   REGION = 'region'
   VPC = 'vpc'

class OutputLayout(Enum):
   HORIZONTAL = 'horizontal'
   VERTICAL = 'vertical'
   HORIZONTAL_NOLINK = 'horizontalnolink'
   VERTICAL_NOLINK = 'verticalnolink'

class OutputShapes(Enum):
   LOGICAL = 'logical'
   PRESCRIBED = 'prescribed'

class Regions(Enum):
   ALL = 'all'
   GERMANY = 'eu-de'
   OSAKA = 'jp-osa'
   SAOPAULO = 'br-sao'
   SYDNEY = 'au-syd'
   TOKYO = 'jp-tok'
   TORONTO = 'ca-tor'
   UNITEDKINGDOM = 'eu-gb'
   USEAST = 'us-east'
   USSOUTH = 'us-south'

class Options:
   cloudType = None
   runMode = None
   inputType = None
   accountID = ''
   apiKey = ''
   inputFile = ''
   region = None
   outputFile = ''
   outputFolder = ''
   tablesFolder = ''
   outputSplit = None
   outputShapes = None
   outputLayout = None
   vpcName = None

   def __init__(self, toolName):
      self.cloudType = CloudType.IBM
      self.runMode = RunMode.BATCH
      self.inputType = InputType.JSON
      self.region = Regions.ALL
      self.outputFile = 'output'
      self.outputFolder = path.join(path.expanduser('~'), 'Documents', toolName)
      self.tablesFolder ='tables'
      self.outputSplit = OutputSplit.SINGLE
      self.outputShapes = OutputShapes.PRESCRIBED
      self.outputLayout = OutputLayout.VERTICAL
      self.vpcName = '*'
      return

   def getAccountID(self):
      return self.accountID

   def setAccountID(self, value):
      self.accountID = value

   def getAPIKey(self):
      return self.apiKey

   def setAPIKey(self, value):
      self.apiKey = value

   def getInputFile(self):
      return self.inputFile

   def setInputFile(self, value):
      self.inputFile = value

   def getOutputFile(self):
      return self.outputFile

   def setOutputFile(self, value):
      self.outputFile = value

   def getOutputFolder(self):
      return self.outputFolder

   def setOutputFolder(self, value):
      self.outputFolder = value

   def getTablesFolder(self):
      return self.tablesFolder

   def setTablesFolder(self, value):
      self.tablesFolder = value

   def isIBMCloud(self):
      return self.cloudType == CloudType.IBM

   def isAWSCloud(self):
      return self.cloudType == CloudType.AWS

   def isIBMCloud(self, value):
      return value == CloudType.IBM.value

   def isAWSCloud(self, value):
      return value == CloudType.AWS.value

   def getCloudType(self):
      return self.cloudType

   def setCloudType(self, value):
      self.cloudType = value

   def isBatchMode(self):
      return self.runMode == RunMode.BATCH

   def isGUIMode(self):
      return self.runMode == RunMode.GUI

   def isWebMode(self):
      return self.runMode == RunMode.WEB

   def isTerraformMode(self):
      return self.runMode == RunMode.TERRAFORM

   def isBatchMode(self, value):
      return value == RunMode.BATCH.value

   def isGUIMode(self, value):
      return value == RunMode.GUI.value

   def isWebMode(self, value):
      return value == RunMode.WEB.value

   def isTerraformMode(self, value):
      return value == RunMode.TERRAFORM.value

   def getRunMode(self):
      return self.runMode

   def setRunMode(self, value):
      self.runMode = value

   def isInputRIAS(self):
      return self.inputType == InputType.RIAS

   def isInputJSON(self):
      return self.inputType == InputType.JSON

   def isInputYAML(self):
      return self.inputType == InputType.YAML

   def setInputRIAS(self):
      self.inputType = InputType.RIAS

   def setInputJSON(self):
      self.inputType = InputType.JSON

   def setInputYAML(self):
      self.inputType = InputType.YAML

   #def getInputType(self):
   #   return self.inputType

   #def setInputType(self, value):
   #   self.inputType = value

   def getVPCName(self):
      return self.vpcName

   def setVPCName(self, name):
      self.vpcName = name

   def isDesignatedVPC(self, name):
      return self.vpcName == '*' or self.vpcName == name

   def setSingleSplit(self):
      self.outputSplit = OutputSplit.SINGLE

   def setCombineSplit(self):
      self.outputSplit = OutputSplit.COMBINE

   def setRegionSplit(self):
      self.outputSplit = OutputSplit.REGION

   def setVPCSplit(self):
      self.outputSplit = OutputSplit.VPC

   def isSingleSplit(self):
      return self.outputSplit == OutputSplit.SINGLE

   def isCombineSplit(self):
      return self.outputSplit == OutputSplit.COMBINE

   def isRegionSplit(self):
      return self.outputSplit == OutputSplit.REGION or self.outputSplit == OutputSplit.COMBINE

   def isVPCSplit(self):
      return self.outputSplit == OutputSplit.VPC

   def getOutputSplit(self):
      return self.outputSplit

   def setOutputSplit(self, value):
      self.outputSplit = value

   def setLogicalShapes(self):
      self.outputShapes = OutputShapes.LOGICAL

   def setPrescribedShapes(self):
      self.outputShapes = OutputShapes.PRESCRIBED

   def isLogicalShapes(self):
      return self.outputShapes == OutputShapes.LOGICAL

   def isPrescribedShapes(self):
      return self.outputShapes == OutputShapes.PRESCRIBED

   def getOutputShapes(self):
      return self.outputShapes

   def setOutputShapes(self, value):
      self.outputShapes = value

   def setHorizontalLayout(self):
      self.outputLayout = OutputLayout.HORIZONTAL

   def setVerticalLayout(self):
      self.outputLayout = OutputLayout.VERTICAL

   def setHorizontalNoLinkLayout(self):
      self.outputLayout = OutputLayout.HORIZONTAL_NOLINK

   def setVerticalNoLinkLayout(self):
      self.outputLayout = OutputLayout.VERTICAL_NOLINK

   def isHorizontalLayout(self):
      return self.outputLayout == OutputLayout.HORIZONTAL or self.outputLayout == OutputLayout.HORIZONTAL_NOLINK

   def isVerticalLayout(self):
      return self.outputLayout == OutputLayout.VERTICAL or self.outputLayout == OutputLayout.VERTICAL_NOLINK

   def isLinkLayout(self):
      return self.outputLayout != OutputLayout.HORIZONTAL_NOLINK and self.outputLayout != OutputLayout.VERTICAL_NOLINK

   def getOutputLayout(self):
      return self.outputLayout

   def setOutputLayout(self, value):
      self.outputLayout = value

   def setAllRegion(self):
      self.region = Regions.ALL

   def setGermanyRegion(self):
      self.region = Regions.GERMANY

   def setOsakaRegion(self):
      self.region = Regions.OSAKA

   def setSaoPauloRegion(self):
      self.region = Regions.SAOPAULO

   def setSydneyRegion(self):
      self.region = Regions.SYDNEY

   def setTokyoRegion(self):
      self.region = Regions.TOKYO

   def setTorontoRegion(self):
      self.region = Regions.TORONTO

   def setUnitedKingdomRegion(self):
      self.region = Regions.UNITEDKINGDOM

   def setUSEastRegion(self):
      self.region = Regions.USEAST

   def setUSSouthRegion(self):
      self.region = Regions.USSOUTH

   def getRegion(self):
      return self.region

   def setRegion(self, value):
      self.region = value
