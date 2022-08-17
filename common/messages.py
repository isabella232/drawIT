# @file messages.py
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
from common.utils import *

class Messages:
   startFileMessage = 'Starting with input from %s'
   startRIASKeyMessage = 'Starting with input from RIAS for API Key %s in %s'
   startRIASAccountMessage = 'Starting with input from RIAS for API Key %s and Account ID %s in %s'
   doneToolMessage = 'Completed with output to %s'
   startProviderMessage = 'Generating Resource for provider'
   backupDirectoryMessage = 'Backed up existing output directory %s to %s'
   warningMessage = '(Warning) %s'
   errorMessage = '(Error) %s'
   invalidMessage = '(Error) %s: %s'
   invalidModeMessage = '(Error) Invalid run mode: %s'
   invalidInputDirectoryMessage = '(Error) Invalid input directory: %s'
   invalidInputFileMessage = '(Error) Invalid input file: %s'
   invalidOutputTypeMessage = '(Error) Invalid output type: %s'
   invalidProtocolMessage = '(Error) Invalid protocol: %s'
   invalidGatewaySpecMessage = '(Error) Invalid gateway specification: %s'
   invalidPublicGatewaymessage = '(Error) Invalid public gateway: %s'
   invalidNICMessage = '(Error) Invalid nic: %s'
   invalidSecondaryNICMessage = '(Error) Invalid secondary nic: %s'
   invalidFIPReferenceMessage = '(Error) Invalid FIP reference: %s'
   invalidInstanceReferenceMessage = '(Error) Invalid Instance reference: %s'
   invalidSubnetReferenceMessage = '(Error) Invalid Subnet reference: %s'
   invalidZonereferenceMessage = '(Error) Invalid Zone reference for Subnet: %s'
   invalidVPCreferenceMessage = '(Error) Invalid VPC reference: %s'
   invalidLBReferenceMessage = '(Error) Invalid LB reference: %s'
   invalidLPPrivateMessage = '(Warning) Private LB not implemented: %s'
   missingInputMessage = '(Error) No input files found: %s'
   missingImageMessage = '(Error) Image %s not found'
   missingRegionMessage = '(Error) Region %s not found'
   missingZoneMessage = '(Error) Zone %s not found'
   missingSubnetMessage = '(Error) Subnet for %s not found'
   missingImageProfileMessage = '(Error) Image profile %s not found'
   missingVolumeProfileMessage = '(Error) Volume profile %s not found'
   missingValueMessage = '(Error) Required value missing on column %s, row %s'
   processingSheetMessage = 'Processing %s'

   missingVPCs = 'No VPCs were found'
   missingSubnets = 'No Subnets were found'

   options = None

   def __init__(self, options):
      self.options = options
      return

   def printLine(self, name, line):
      genpath = self.options['outputfolder']

      pathname = os.path.join(genpath, name)
      filepath, filename = os.path.split(pathname)

      # Check for existing module directory.
      if not os.path.exists(filepath):
         # Create new module directory.
         os.makedirs(filepath)

      if not os.path.exists(pathname):
         tf = open(pathname, 'wb')
         #tf.write(toolheader)
         #tf.write('\n')
         tf.close()

      tf = open(pathname, 'ab')
      tf.write(line)
      tf.write('\n')
      tf.close()

      return

   def printError(self, *args):
      print(*args, file=sys.stderr)

   def printMessage(self, *args):
      print(*args, file=sys.stderr)

   def printXML(self, *args):
      sys.stdout.write(*args)


   def printStartFile(self, filename):
      self.printError(self.startFileMessage % filename)

   def printStartRIASwithKey(self, apikey, region):
      self.printError(self.startRIASKeyMessage % (apikey, region))

   def printStartRIASwithAccount(self, apikey, accountid, region):
      self.printError(self.startRIASAccountMessage % (apikey, accountid, region))

   def printDone(self, outputfolder):
      self.printError(self.doneToolMessage % outputfolder)

   def printMissingVPCs(self, *args):
      self.printError(self.invalidMessage % (self.missingVPCs, *args))

   def printMissingSubnets(self, *args):
      self.printError(self.invalidMessage % (self.missingSubnets, *args))

   def printDetailsRIAS(self, arg):
      self.printError(self.invalidMessage % arg)
