# @file utils.py
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

import os
import sys
import hashlib
import shutil

import base64
from urllib.parse import quote, unquote
from codecs import encode
import zlib
#SAVE import numpy as np
import pandas as pd

from load.file import *
from load.rias import *

#from flatten_json import flatten

# Constants

TOOLNAME = 'drawIT'
TOOLVERSION = '0.5.1'

#ACCOUNT_PLACEHOLDER = '(Account-ID)'
#KEY_PLACEHOLDER = '(API-Key)'
#INPUT_PLACEHOLDER = '(Input-File)'
#OUTPUT_PLACEHOLDER = '(Output-Directory)'

# Following static string is included in binary - update version here.
COPYRIGHT = TOOLNAME + ' ' + TOOLVERSION + ' - Copyright 2022 IBM Corporation'

# Messages

toolheader = TOOLNAME + '\n'
starttoolmessage = 'Starting with input from %s'
donetoolmessage = 'Completed with output to %s'
startprovidermessage = 'Generating Resource for provider'
backupdirectorymessage = 'Backed up existing output directory %s to %s'
warningmessage = '(Warning) %s'
invalidmessage = '(Error) %s: %s'
invalidmodemessage = '(Error) Invalid run mode: %s'
invalidinputdirectorymessage = '(Error) Invalid input directory: %s'
invalidinputfilemessage = '(Error) Invalid input file: %s'
invalidoutputtypemessage = '(Error) Invalid output type: %s'
invalidprotocolmessage = '(Error) Invalid protocol: %s'
invalidgatewayspecmessage = '(Error) Invalid gateway specification: %s'
invalidpublicgatewaymessage = '(Error) Invalid public gateway: %s'
invalidnicmessage = '(Error) Invalid nic: %s'
invalidsecondarynicmessage = '(Error) Invalid secondary nic: %s'
invalidfipreferencemessage = '(Error) Invalid FIP reference: %s'
invalidinstancereferencemessage = '(Error) Invalid Instance reference: %s'
invalidsubnetreferencemessage = '(Error) Invalid Subnet reference: %s'
invalidzonereferencemessage = '(Error) Invalid Zone reference for Subnet: %s'
invalidvpcreferencemessage = '(Error) Invalid VPC reference: %s'
invalidlbreferencemessage = '(Error) Invalid LB reference: %s'
invalidlbprivatemessage = '(Warning) Private LB not implemented: %s'
missinginputmessage = '(Error) No input files found: %s'
missingimagemessage = '(Error) Image %s not found'
missingregionmessage = '(Error) Region %s not found'
missingzonemessage = '(Error) Zone %s not found'
missingsubnetmessage = '(Error) Subnet for %s not found'
missingimageprofilemessage = '(Error) Image profile %s not found'
missingvolumeprofilemessage = '(Error) Volume profile %s not found'
missingvaluemessage = '(Error) Required value missing on column %s, row %s'
processingsheetmessage = 'Processing %s'

# Global data

userdata = {
    'runmode': 'batch',
    'inputtype': 'json',
    #'apikey': 'rW7EOXWZbYXbxxhD3HkIPvpVbDfGiKvauniVIEEuzvdY',
    #'accountid': ACCOUNT_PLACEHOLDER,
    #'apikey': KEY_PLACEHOLDER,
    #'inputfile': INPUT_PLACEHOLDER,
    'accountid': '',
    'apikey': '',
    'inputfile': '',
    #'nogui': True,
    'region': 'us-south',
    'outputfile': 'output',
    'outputfolder': os.path.join(os.path.expanduser('~'), 'Documents', TOOLNAME),
    'outputtype': 'xml',
    'outputlayout': 'kk',
    'outputsplit': 'none',
    'outputdetail': 'medium',
    'outputshapes': 'prescribed',
    'inputdata': {
        'vpcs': {},
        'subnets': {},
        'instances': {},
        'networkInterfaces': {},
        'publicGateways': {},
        'floatingIPs': {},
        'vpnGateways': {},
        'vpnConnections': {},
        'loadBalancers': {},
        'loadBalancerListeners': {},
        'loadBalancerPools': {},
        'loadBalancerMembers': {},
        'volumes': {},
        'networkACLs': {},
        'securityGroups': {},
        'keys': {}
    },
    'setupdata': {
        'nics': {},
        'regions': {},
        'vpcs': {},
        'zones': {}
    },
    'outputdata': {}
}

zonecidrs = {
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

iconwidth = 48
iconheight = 48

groupwidth = 240
groupheight = 152

mingroupwidth = 240
mingroupheight = 48

groupspace = 30
topspace = 70
textgroupspace = 10
texttopspace = 70
iconspace = 48
#leftspace = iconwidth + groupspace
leftspace = iconspace * 3

firsticonx = iconspace
firsticony = topspace

secondiconx = iconspace
secondicony = firsticony + iconheight + iconspace

publiciconcount = 2
publicnetworkwidth = iconspace * 3
publicnetworkheight = topspace + (iconspace * publiciconcount) + (iconheight * publiciconcount)

enterpriseiconcount = 1
enterprisenetworkwidth = iconspace * 3
enterprisenetworkheight = topspace + (iconspace * enterpriseiconcount) + (iconheight * enterpriseiconcount)

internetname = 'Internet'
publicnetworkname = 'Public<br>Network'
publicusername = 'User'
enterprisenetworkname = 'Enterprise<br>Network'
enterpriseusername = 'Enterprise User'

# Utility functions

def inflate(b,b64=False):
    """~2016 draw.io started compressing 'using standard deflate'
        https://about.draw.io/extracting-the-xml-from-mxfiles/
        experience has shown this is deflate WITH NO HEADER
    """
    if b64: # optional, additionally base64 decode
        b = base64.b64decode(b)
    decompress = zlib.decompressobj(-zlib.MAX_WBITS)
    inflated = decompress.decompress(b);
    decoded = inflated.decode('utf8')
    unquoted = unquote(decoded)
    return unquoted

def deflate(b,b64=False):
    compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15, memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY)
    quoted = quote(b)
    #deflated = compress.compress(bytes(quoted, 'iso-8859-1'), safe='~()*!.\'')
    deflated = compress.compress(bytes(quoted, 'iso-8859-1'))
    deflated += compress.flush()
    deflatedstring = str(encode(deflated, 'hex'), 'utf-8')
    return deflatedstring

# isna returns True for NA values such as None or numpy.NaN.
# isna returns False for empty strings or numpy.inf unless
# set pandas.userdata.mode.use_inf_as_na = True
# Note:
# Empty spreadsheet values start out as NaN but if a value is
# added and later deleted then the value can be an empty string.
# Checking pd.isna here doesn't work as value is 'nan'.
#def novalue(value):
#   empty = pd.isna(value)
#   if empty:
#      return True
#   if type(value) == str:
#      value = value.replace(' ', '')
#      if value == '':
#         return True
#   if isinstance(value, str):
#      value = value.replace(' ', '')
#      if value == '':
#         return True
#      else:
#         return False
#   else:
#      return False

def truncateText(text, size, linebreak):
    if text.find(linebreak) == -1:
       if len(text) > size:
          return text[0:size-1] + '...'
       else:
          return text
    else:
       textsplit = text.split(linebreak)
       newtext = ''
       count = 0
       for name in textsplit:
          count = count + 1
          if len(name) == 0:
             continue
          elif len(name) > size:
             if count == 1:
                newtext = name[0:size-1] + '...'
             else:
                newtext = newtext + linebreak + name[0:size-1] + '...'
          else:
             if count == 1:
                newtext = name
             else:
                newtext = newtext + linebreak + name

       if len(newtext) > 0:
          return newtext
       else:
          return text

def load(userdata):
    inputtype = userdata['inputtype']

    if inputtype == 'rias':
        inputdata = loadRIAS(userdata)
        normalizeddata = normalizeRIAS(userdata, inputdata)
    elif inputtype == 'json':
        inputdata = loadJSON(userdata)
        normalizeddata = normalizeYAML(userdata, inputdata)
    else:
        inputdata = loadYAML(userdata)
        normalizeddata = normalizeYAML(userdata, inputdata)

    return normalizeddata

def printline(userdata, name, line):
   genpath = userdata['outputfolder']

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

def printerror(*args):
    print(*args, file=sys.stderr)
    #sys.stderr.write(*args)

def printmessage(*args):
    print(*args, file=sys.stderr)
    #sys.stderr.write(*args)

def printxml(*args):
    sys.stdout.write(*args)
    #sys.stdout.write(deflate(*args))

# Backup output directory
def backupdirectory(userdata):
   genbackup = None
   genpath = userdata['outputfolder']
   # Check for existing output directory and backup if exists.
   if os.path.exists(genpath):
      backup = 1
      found = False
      genbackup = None
      # Find a new backup directory.
      while not found:
         genbackup = genpath + '.backup' + str(backup)
         if os.path.exists(genbackup):
            backup += 1
         else:
            found = True
      # Move existing output directory to backup directory.
      shutil.move(genpath, genbackup)

   # Create new empty output directory.
   os.makedirs(genpath)

   return

# Search functions

def finddictionary(userdata, dictionarylist, columnname, columnvalue):
   if len(dictionarylist) > 0:
      for dictionaryindex, dictionary in dictionarylist.iterrows():
         if dictionary[columnname] == columnvalue:
            return dictionary
   return {}

def findrow(userdata, dictionarylist, columnname, columnvalue):
   return finddictionary(userdata, dictionarylist, columnname, columnvalue)

def findlb(userdata, dictionarylist, columnname, columnvalue):
   if dictionarylist:
      for dictionary in dictionarylist:
         print(dictionary)
         column = dictionary[columnname]
         # TODO: Remove 0 in first column
         column = column[0]
         #print(column)
         #if dictionary[columnname] == columnvalue:
         if column == columnvalue:
            return dictionary
   return {}

#def findfip(userdata, dictionarylist, columnname, columnvalue):
#   if len(dictionarylist) > 0:
#      for dictionaryindex, dictionary in dictionarylist.iterrows():
#         if dictionary[columnname]  == columnvalue:
#            return dictionary
#         #if 'target' in dictionary:
#         #   target = dictionary['target']
#         #   if target[columnname] == columnvalue:
#         #      return dictionary
#   return {}

#def findvpn(userdata, dictionarylist, columnname, columnvalue):
#   if len(dictionarylist) > 0:
#      for dictionaryindex, dictionary in dictionarylist.iterrows():
#         if dictionary[columnname]  == columnvalue:
#            return dictionary
#      #   if 'subnet' in dictionary:
#      #      subnet = dictionary['subnet']
#      #      if subnet[columnname] == columnvalue:
#      #         return dictionary
#   return {}

# Calculate functions

def printcounts(userdata):
   inputdata = userdata['inputdata']
   setupdata = userdata['setupdata']

   vpcstable = setupdata['vpcs']
   for vpc in vpcstable:
      print("**************")
      print(vpc)

   subnetstable = setupdata['subnets']
   for keys, values in subnetstable.items():
      print("**************")
      print("**************")
      print(keys)
      print("--------------")
      print(len(values))

# Other functions

def getnormalized(data):
   normalized = pd.json_normalize(data)
   df = normalized.T.unstack()[0]
   return df

#def compress(string):
#   return letter + str(length := len(list(group))) if length > 1 else ''
#def compress(string):
#   return ''.join(
#           letter + str(len(list(group)))
#           for letter, group in itertools.groupby(string))

def compress(string):
   hash = hashlib.md5(string.encode())
   return hash.hexdigest()
