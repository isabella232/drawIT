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

from os import makedirs, path
from pandas import isna

from build.common.options import Options
from build.common.messages import Messages

class Common:
   toolName = 'buildIT'
   toolVersion = '0.5.18'
   toolCopyright = toolName + ' ' + toolVersion + ' - Copyright IBM Corporation'
   toolHeader = '# Generated by buildIT'

   options = None
   messages = None

   def __init__(self):
       self.options = Options(self.toolName)
       self.messages = Messages(self.options)

   # Utilities

   def printLine(self, tfname, line):
      outputdirectory = self.options.getOutputDirectory()

      pathname = path.join(outputdirectory, tfname)
      filepath, filename = path.split(pathname)

      # Check for existing module directory.
      if not path.exists(filepath):
         # Create new module directory.
         makedirs(filepath)

      if not path.exists(pathname):
         tf = open(pathname, 'w')
         tf.write(self.toolHeader)
         tf.write('\n')
         tf.close()

      tf = open(pathname, 'a')
      tf.write(line)
      tf.write('\n')
      tf.close()

      return

   # isna returns True for NA values such as None or numpy.NaN.
   # isna returns False for empty strings or numpy.inf unless
   # set pandas.options.mode.use_inf_as_na = True
   # Note:
   # Empty spreadsheet values start out as NaN but if a value is
   # added and later deleted then the value can be an empty string.
   # Checking pd.isna here doesn't work as value is 'nan'.
   def noValue(self, value):
      empty = isna(value)
      if empty:
         return True
      if type(value) == str:
         value = value.replace(' ', '')
         if value == '':
            return True
      if isinstance(value, str):
         value = value.replace(' ', '')
         if value == '':
            return True
         else:
            return False
      else:
         return False

   # Options

   def getInputDirectory(self):
      return self.options.getInputDirectory()

   def setInputDirectory(self, value):
      self.options.setInputDirectory(value)

   def getOutputDirectory(self):
      return self.options.getOutputDirectory()

   def setOutputDirectory(self, value):
      self.options.setOutputDirectory(value)

   def getInputType(self):
      return self.options.getInputType()

   def setInputType(self, value):
      self.options.setInputType(value)

   def getExtension(self):
      return self.options.getExtension()

   def setExtension(self, value):
      self.options.setExtension(value)

   def getFile(self):
      return self.options.getFile()

   def setFile(self, value):
      self.options.setFile(value)

   def getName(self):
      return self.options.getName()

   def setName(self, value):
      self.options.setName(value)

   # Messages

   def printToolHeader(self):
      self.messages.printToolHeader()

   def printStart(self, inputFolder):
      self.messages.printStart()

   def printDone(self, outputFolder):
      self.messages.printDone()

   def printSheet(self, sheet):
      self.messages.printSheet(sheet)

   def printProvider(self):
      self.messages.printProvider()

   def printVersion(self):
      self.messages.printVersion()

   def printDoneTerraform(self, inputFolder, outputFolder):
      self.messages.printDoneTerraform(inputFolder, outputFolder)

   def printBackupDirectory(self, folder1, folder2):
      self.messages.printBackupDirectory(folder1, folder2)

   def printInvalidInput(self, inputFolder):
      self.messages.printInvalidInput(inputFolder)

   def printInvalidFile(self, inputFile):
      self.messages.printInvalidFile(inputFile)

   def printInvalidProtocol(self, protocol):
      self.messages.printInvalidProtocol(protocol)

   def printInvalidGateway(self, gateway):
      self.messages.printInvalidGateway(gateway)

   def printInvalidNIC(self, nic):
      self.messages.printInvalidNic(nic)

   def printInvalidSecondaryNIC(self, nic):
      self.messages.printInvalidSecondaryNIC(nic)

   def printMissingInput(self, inputFolder):
      self.messages.printMissingInput(inputFolder)

   def printMissingImage(self, image):
      self.messages.printMissingImage(image)

   def printMissingZone(self, zone):
      self.messages.printMissingZone(zone)

   def printMissingSubnet(self, subnet):
      self.messages.printMissingSubnet(subnet)

   def printMissingImageProfile(self, profile):
      self.messages.printMissingImageProfile(profile)

   def printMissingVolumeProfile(self, profile):
      self.messages.printVolumeProfile(profile)

   def printMissingValue(self, column, row):
      self.messages.printMissingValue(column, row)
