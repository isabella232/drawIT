# @file common.py
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

from common.options import Options
from common.messages import Messages
from common.utils import *

class Common:
   options = None
   messages = None

   def __init__(self):
      self.options = Options()
      self.messages = Messages(self.options)
      return

   # Options

   def getAccountID(self):
      return self.options.getAccountID()

   def setAccountID(self, value):
      self.options.setAccountID(value)

   def getAPIKey(self):
      return self.options.getAPIKey()

   def setAPIKey(self, value):
      self.options.setAPIKey(value)

   def getRegion(self):
      return self.options.getRegion()

   def setRegion(self, value):
      self.options.setRegion(value)

   def getInputFile(self):
      return self.options.getInputFile()

   def setInputFile(self, value):
      self.options.setInputFile(value)

   def getOutputFile(self):
      return self.options.getOutputFile()

   def setOutputFile(self, value):
      self.options.setOutputFile(value)

   def getOutputFolder(self):
      return self.options.getOutputFolder()

   def setOutputFolder(self, value):
      self.options.setOutputFolder(value)

   def isBatchMode(self):
      return self.options.isBatchMode()

   def isGUIMode(self):
      return self.options.isGUIMode()

   def isWebMode(self):
      return self.options.isWebMode()

   def getRunMode(self):
      return self.options.getRunMode()

   def setRunMode(self, value):
      self.options.setRunMode(value)

   def isInputRIAS(self):
      return self.options.isInputRIAS()

   def isInputJSON(self):
      return self.options.isInputJSON()

   def isInputYAML(self):
      return self.options.isInputYAML()

   def setInputRIAS(self):
      return self.options.setInputRIAS()

   def setInputJSON(self):
      return self.options.setInputJSON()

   def setInputYAML(self):
      return self.options.setInputYAML()

   #def getInputType(self):
   #   return self.options.getInputType()

   #def setInputType(self, value):
   #   self.options.setInputType(value)

   def isSingleSplit(self):
      return self.options.isSingleSplit()

   def isRegionSplit(self):
      return self.options.isRegionSplit()

   def isVPCSplit(self):
      return self.options.isVPCSplit()

   def getOutputSplit(self):
      return self.options.getOutputSplit()

   def setOutputSplit(self, value):
      self.options.setOutputSplit(value)

   def isLowDetail(self):
      return self.options.isLowDetail()

   def isMediumDetail(self):
      return self.options.isMediumDetail()

   def isHighDetail(self):
      return self.options.isHighDetail()

   def getOutputDetail(self):
      return self.options.getOutputDetail()

   def setOutputDetail(self, value):
      self.options.setOutputDetail(value)

   def isLogicalShapes(self):
      return self.options.isLogicalShapes()

   def isPrescribedShapes(self):
      return self.options.isPrescribedtShapes()

   def getOutputShapes(self):
      return self.options.getOutputShapes()

   def setOutputShapes(self, value):
      self.options.setOutputShapes(value)

   # Messages

   def printStartFile(self, filename):
      self.messages.printStartFile(filename)

   def printStartRIASwithKey(self, apikey, region):
      self.messages.printStartRIASwithKey(apikey, region)

   def printStartRIASwithAccount(self, apikey, accountid, region):
      self.messages.printStartRIASwithAccount(apikey, accountid, region)

   def printDone(self, outputfolder):
      self.messages.printDone(outputfolder)

   def printMissingVPCs(self, *args):
      self.messages.printMissingVPCs(*args)

   def printMissingSubnets(self, *args):
      self.messages.printMissingSubnets(*args)

   def getOptions(self):
      return self.options
