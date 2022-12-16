# @file messages.py
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

from sys import stderr

from common.options import Options

class Messages:
   startFileMessage = 'Starting with input from %s for %s Cloud'
   startRIASKeyMessage = 'Starting with input from RIAS for API Key %s in %s'
   startRIASAccountMessage = 'Starting with input from RIAS for API Key %s and Account ID %s in %s'
   doneMessage = 'Completed with output to %s for %s Cloud'
   exitMessage = 'Completed with no output'
   startProviderMessage = 'Generating Resource for provider'
   backupDirectoryMessage = 'Backed up existing output directory %s to %s'
   warningMessage = '(Warning) %s'
   errorMessage = '(Error) %s'
   invalidMessage = '(Error) %s: %s'
   invalidRequestMessage = '(Error) %s: %s, href=%s'
   invalidResponseMessage = '(Error) %s: %s'
   invalidModeMessage = '(Error) Invalid run mode: %s'
   invalidCloudMessage = '(Error) Cloud type not supported: %s'
   invalidInputDirectoryMessage = '(Error) Invalid input directory: %s'
   invalidInputMessage = '(Error) Invalid input: No RIAS, JSON, or YAML'
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
   invalidVPCReferenceMessage = '(Error) Invalid VPC reference: %s'
   invalidVPEReferenceMessage = '(Error) Invalid VPE reference: %s'
   invalidLBReferenceMessage = '(Error) Invalid Load Balancer reference: %s'
   invalidLBPrivateMessage = '(Warning) Private Load Balancer not implemented: %s'
   invalidInstanceMemberMessage = '(Error) Invalid member for Load Balancer: %s, Pool: %s, Instance: %s'
   missingInputMessage = '(Error) No input files found: %s'
   missingImageMessage = '(Error) Image %s not found'
   missingRegionMessage = '(Error) Region %s not found'
   missingZoneMessage = '(Error) Zone %s not found'
   missingZoneReferenceMessage = '(Error) Invalid Zone reference for Subnet: %s'
   missingSubnetMessage = '(Error) Subnet for %s not found'
   missingImageProfileMessage = '(Error) Image profile %s not found'
   missingVolumeProfileMessage = '(Error) Volume profile %s not found'
   missingValueMessage = '(Error) Required value missing on column %s, row %s'
   warningMissingPoolMessage = '(Warning) No pool defined for Load Balancer: %s'
   warningMissingMemberMessage = '(Warning) No member defined for Load Balancer: %s, Pool: %s'
   processingSheetMessage = 'Processing %s'

   missingVPCsMessage = '(Error) No VPCs were found'
   missingSubnetsMessage = '(Error) No Subnets were found'

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
      print(*args, file=stderr)

   def printMessage(self, *args):
      print(*args, file=stderr)

   def printXML(self, *args):
      sys.stdout.write(*args)


   def printStartFile(self, filename, cloud):
      self.printError(self.startFileMessage % (filename, cloud))

   def printStartRIASwithKey(self, apikey, region):
      self.printError(self.startRIASKeyMessage % (apikey, region))

   def printStartRIASwithAccount(self, apikey, accountid, region):
      self.printError(self.startRIASAccountMessage % (apikey, accountid, region))

   def printDone(self, filename, cloud):
      self.printError(self.doneMessage % (filename, cloud))

   def printExit(self):
      self.printError(self.exitMessage)

   def printMissingVPCs(self):
      self.printError(self.missingVPCsMessage)

   def printMissingSubnets(self):
      self.printError(self.missingSubnetsMessage)

   def printInvalidMode(self, mode):
      self.printError(self.invalidModeMessage % mode)

   def printInvalidCloud(self, cloud):
      self.printError(self.invalidCloudMessage % cloud)

   def printInvalidInput(self):
      self.printError(self.invalidInputMessage)

   def printInvalidFile(self, filename):
      self.printError(self.invalidInputFileMessage % filename)

   def printInvalidInstance(self, instanceid):
      self.printError(self.invalidInstanceReferenceMessage % instanceid)

   def printInvalidLoadBalancer(self, lbname):
      self.printError(self.invalidLBReferenceMessage % lbname)

   def printInvalidPrivateLoadBalancer(self, lbname):
      self.printError(self.invalidLBPrivateMessage % lbname)

   def printInvalidPublicGateway(self, pubgateid):
      self.printError(self.invalidPublicGatewayMessage % pubgateid)

   def printInvalidSubnet(self, subnetid):
      self.printError(self.invalidSubnetReferenceMessage % subnetid)

   def printInvalidVPC(self, vpcid):
      self.printError(self.invalidVPCReferenceMessage % vpcid)

   def printInvalidVPE(self, vpeid):
      self.printError(self.invalidVPEReferenceMessage % vpeid)

   def printMissingZone(self, subnetname):
      self.printError(self.missingZoneReferenceMessage % subnetname)

   def printMissingPool(self, lbname):
      self.printError(self.warningMissingPoolMessage % lbname)

   def printMissingMember(self, lbname, lbpoolname):
      self.printError(self.warningMissingMemberMessage % (lbname, lbpoolname))

   def printInvalidInstanceMember(self, lbname, lbpoolname, instanceid):
      self.printError(self.invalidInstanceMemberMessage % (lbname, lbpoolname, instanceid))

   def printRequestMessage(self, code, message, href):
      self.printError(self.invalidRequestMessage % (code, message, href))

   def printResponseMessage(self, code, message):
      self.printError(self.invalidResponseMessage % (code, message))
