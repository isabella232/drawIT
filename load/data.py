# @file data.py
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

from load.analyze import Analyze
from load.file import File
from load.rias import RIAS
from common.utils import *

class Data:
   def __init__(self, user):
      self.inputtype = user['inputtype']
      self.inputdata = None
      self.normalizeddata = None
      self.setupdata = None
      self.file = File(user)
      self.rias = RIAS(user)
      self.analyze = Analyze(user)

   def loadData(self):
      if self.inputtype == 'rias':
         self.inputdata = self.rias.loadRIAS()
         if self.inputdata != None:
            self.normalizeddata = self.rias.normalizeData(self.inputdata)
            userdata['inputdata'] = self.normalizeddata
      elif self.inputtype == 'json':
         self.inputdata = self.file.loadJSON()
         if self.inputdata != None:
            self.normalizeddata = self.file.normalizeData(self.inputdata)
            userdata['inputdata'] = self.normalizeddata
      else:
         self.inputdata = self.file.loadYAML()
         if self.inputdata != None:
            self.normalizeddata = self.file.normalizeData(self.inputdata)
            userdata['inputdata'] = self.normalizeddata
   
      if self.normalizeddata != None:
         self.setupdata = self.analyze.analyzeData() 
         userdata['setupdata'] = self.setupdata
