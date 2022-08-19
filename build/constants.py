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

names = {
   'internetName': 'Internet',
   'publicNetworkName': 'Public<br>Network',
   'publicUserName': 'User',
   'enterpriseNetworkName': 'Enterprise<br>Network',
   'enterpriseUserName': 'Enterprise User'
}

points = {
   'iconWidth': 48,
   'iconHeight': 48,

   'groupWidth': 240,
   'groupHeight': 152,

   'minGroupWidth': 240,
   'minGroupHeight': 48,

   'groupSpace': 30,
   'topSpace': 70,
   'textGroupSpace': 10,
   'textTopSpace': 70,
   'iconSpace': 48,

   'leftSpace': 0,

   'firstIconX': 0,
   'firstIconY': 0,

   'secondIconX': 0,
   'secondIconY': 0,

   'publicIconCount': 2,
   'publicNetworkWidth': 0,
   'publicNetworkHeight': 0,

   'enterpriseIconCount': 1,
   'enterpriseNetworkWidth': 0,
   'enterpriseNetworkHeight': 0
}

points['leftSpace'] = points['iconSpace'] * 3
points['firstIconX'] = points['iconSpace']
points['firstIconY'] = points['topSpace']

points['secondIconX'] = points['iconSpace']
points['secondIconY'] = points['firstIconY'] + points['iconHeight'] + points['iconSpace']

points['publicNetworkWidth'] = points['iconSpace'] * 3
points['publicNetworkHeight'] = points['topSpace'] + (points['iconSpace'] * points['publicIconCount']) + (points['iconHeight'] * points['publicIconCount'])

points['enterpriseNetworkWidth'] = points['iconSpace'] * 3
points['enterpriseNetworkHeight'] = points['topSpace'] + (points['iconSpace'] * points['enterpriseIconCount']) + (points['iconHeight'] * points['enterpriseIconCount'])

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
