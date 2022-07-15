# @file diagrams.py
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

import math 

from build.shapes import Shapes
from load.data import Data
from common.utils import *

class Diagrams:
   def __init__(self, user):
      self.inputdata = user['inputdata']
      self.setupdata = user['setupdata']
      self.inputtype = user['inputtype']
      self.outputdetail = user['outputdetail']
      self.outputfolder = user['outputfolder']
      self.outputfile = user['outputfile']
      self.outputshapes = user['outputshapes']
      self.outputsplit = user['outputsplit']
      self.userregion = user['region']
      self.runmode = user['runmode']
      self.saveinstances = []
      self.data = Data(user)
      self.shapes = Shapes(user)

   def buildDiagrams(self):
      self.data.loadData()
      self.inputdata = userdata['inputdata']
      self.setupdata = userdata['setupdata']

      if self.outputfolder[-1] != '/':
         self.outputfolder = self.outputfolder + '/'

      regiondata = {}

      for regionname, regionvalues in self.setupdata['regions'].items():
         vpcdata = self.buildVPCs(regionname, regionvalues)
         regiondata[regionname] = vpcdata

      for regionname, regionvalues in regiondata.items():
         if self.userregion != "all" and self.userregion != regionname:
            # Covers the case for Yaml data which includes all regions whereas RIAS data can include single or all regions.
            continue
         for vpcname, vpcvalues in regionvalues.items():
            self.shapes.buildXML(vpcvalues, regionname + ':' + vpcname)
            if self.outputsplit == 'vpc':
               self.shapes.dumpXML(regionname + "_" + vpcname + "_" + self.outputfile, self.outputfolder)
               self.shapes.resetXML()
         if self.outputsplit == 'region':
            self.shapes.dumpXML(regionname + "_" + self.outputfile, self.outputfolder)
            self.shapes.resetXML()

         if self.outputsplit == 'none':
            self.shapes.dumpXML(self.outputfile, self.outputfolder)

   def buildVPCs(self, regionname, regionvalues):
      data = {}

      publicx = 0
      publicy = 0
      publicnode = self.shapes.buildPublicNetwork(publicnetworkname, '', publicnetworkname, '', publicx, publicy, publicnetworkwidth, publicnetworkheight)
      publicusernode = self.shapes.buildUser(publicusername, publicnetworkname, publicusername, '', firsticonx, firsticony, iconwidth, iconheight)
      publicinternetnode = self.shapes.buildInternet(internetname, publicnetworkname, internetname, '', secondiconx, secondicony, iconwidth, iconheight)

      enterprisex = 0
      enterprisey = publicnetworkheight + groupspace
      enterprisenode = self.shapes.buildEnterpriseNetwork(enterprisenetworkname, '', enterprisenetworkname, '', enterprisex, enterprisey, enterprisenetworkwidth, enterprisenetworkheight)
      enterpriseusernode = self.shapes.buildUser(enterpriseusername, enterprisenetworkname, enterpriseusername, '', firsticonx, firsticony, iconwidth, iconheight)

      if self.outputshapes == "logical":
         cloudname = "Cloud"
      else:
         cloudname = "IBM Cloud"

      for vpcid in regionvalues:
         vpcframe = findrow(userdata, self.inputdata['vpcs'], 'id', vpcid)
         if len(vpcframe) == 0:
            printerror(invalidvpcreferencemessage % vpcid)
         else:
            nodes = []
            links = []
            values = []
            
            nodes.append(publicnode)
            nodes.append(publicusernode)
            nodes.append(publicinternetnode)

            #SAVE publiclink = genlink(userdata, publicname, publicname, internetname)
            #SAVE links.append(publiclink)

            publicuserlink = self.shapes.buildDoubleArrow('', internetname, publicusername)
            links.append(publicuserlink)

            nodes.append(enterprisenode)
            nodes.append(enterpriseusernode)

            enterpriseuserlink = self.shapes.buildDoubleArrow('', internetname, enterpriseusername)
            links.append(enterpriseuserlink)

            vpcname = vpcframe['name']

            #SAVE if not vpcname.startswith('jww'):
            #SAVE    continue
         
            zonenodes, zonelinks, zonevalues, zonesizes = self.buildZones(vpcname, vpcid)
            nodes = nodes + zonenodes
            links = links + zonelinks
            values = values + zonevalues

            width = iconwidth
            height = iconheight

            routername = vpcname + '-router'
            routernode = self.shapes.buildRouter(routername, vpcname, routername, '', firsticonx, firsticony, width, height)
            nodes.append(routernode)

            routerlink = self.shapes.buildDoubleArrow('', routername, internetname)
            links.append(routerlink)

            width = 0
            height = 0
            for size in zonesizes:
               if size[0] > width:
                  width = size[0]

               height = height + size[1] + groupspace

            width = leftspace + width + groupspace  # space after inner groups
            height = height + topspace # space at top of outer group to top inner group
            height  = height - groupspace  # TODO Remove extra groupspace.

            x = groupspace
            y = topspace

            vpcnode = self.shapes.buildVPC(vpcname, regionname, vpcname, '', x, y, width, height) 
            nodes.append(vpcnode)

            x = 30
            y = 70

            width = width + (groupspace * 2)
            height = height + (topspace + groupspace)

            regionnode = self.shapes.buildRegion(regionname, cloudname, regionname, '', x, y, width, height)
            nodes.append(regionnode)
         
            #SAVE lbnodes, lblinks = genloadbalancers(userdata, vpcname, vpcid)
            #SAVE if len(lbnodes) > 0:
            #SAVE    nodes = nodes + lbnodes
            #SAVE    links = links + lblinks

            #publicwidth = (groupspace * 2) + (48 * 3)
            #x  = (groupspace * 4) + (48 * 3)  # Allow space for public network.
            x = publicnetworkwidth + groupspace  # Allow space for public network.
            y = 0

            width = width + (groupspace * 2)
            height = height + (topspace + groupspace)

            cloudnode = self.shapes.buildCloud(cloudname, '', cloudname, '', x, y, width, height)
            nodes.append(cloudnode)
   
            data[vpcname] = {'nodes': nodes, 'values': values, 'links': links}

      return data

   def buildZones(self, vpcname, vpcid):
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      vpcstable = self.setupdata['vpcs'] 
      count = 0
      for regionzonename in vpcstable[vpcid]:
         count = count + 1

         zonelink = self.shapes.buildLink(regionzonename + ':' + vpcname, regionzonename, vpcname)
         #SAVE links.append(zonelink)

         subnetnodes, subnetlinks, subnetvalues, subnetsizes = self.buildSubnets(regionzonename, vpcname)
         nodes = nodes + subnetnodes
         links = links + subnetlinks
         values = values + subnetvalues

         width = 0
         height = 0

         for size in subnetsizes:
            if size[0] > width:
               width = size[0]

            height = height + size[1] + groupspace

         width = leftspace + width + groupspace
         height = height + topspace  # space at top of outer group to top inner group
         height = height - groupspace

         x = (iconspace * 2) + iconwidth
         y = topspace + saveheight + (groupspace * (count - 1))

         saveheight += height

         zonename = regionzonename.split(':')[1]
         zonecidr = zonecidrs[zonename]

         zonenode = self.shapes.buildZone(regionzonename, vpcname, regionzonename, zonecidr, x, y, width, height)
         nodes.append(zonenode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([leftspace - groupspace, 0])

      return nodes, links, values, sizes

   def buildSubnets(self, zonename, vpcname): 
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      zonestable = self.setupdata['zones']
      count = 0
      save_subnetpubgateid = None

      for subnetid in zonestable[zonename]:
         count = count + 1
         pubgateid = None

         width = 0
         height = 0

         subnetframe = findrow(userdata, self.inputdata['subnets'], 'id', subnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         vpcframe = findrow(userdata, self.inputdata['vpcs'], 'id', subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = zonename.split(':')[0]
         regionzonename = regionname + ':' + subnetzonename;

         zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname)
         #SAVE links.append(zonelink)

         if 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            pubgateframe = findrow(userdata, self.inputdata['publicGateways'], 'id', subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.inputtype == 'rias': 
                  pubgatefipip = pubgateframe['floating_ip.address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         vpngateip = None
         vpngatename = None
         vpngateways = self.inputdata['vpnGateways']
         if not vpngateways.empty:
            if self.inputtype == 'rias': 
               vpngateframe = findrow(userdata, self.inputdata['vpnGateways'], 'subnet.id', subnetid)
            else:
               vpngateframe = findrow(userdata, self.inputdata['vpnGateways'], 'networkId', subnetid)
            if len(vpngateframe) > 0:
               vpngateid = vpngateframe['id']
               # TODO Retrieve VPNGatewayMember[], 
               #      For each memberi get public_ip and private_ip.
               vpngateip = ''
               vpngatename = vpngateframe['name']
               vpnsubnetid = subnetid

         instancenodes, instancelinks, instancevalues, instancesizes = self.buildInstances(subnetid, subnetname, subnetvpcname, vpcname)

         nodes = nodes + instancenodes
         links = links + instancelinks
         values = values + instancevalues

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = mingroupwidth
            height = mingroupheight
         else:
            width = groupspace
            height = 0

         for size in instancesizes:
            width = width + size[0] + groupspace

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + topspace + groupspace  # space at top and bottom of group

         #SAVE x = (iconspace * 2) + iconwidth
         #SAVE y = topspace + (height * (count - 1)) + (groupspace * (count - 1))

         x = (iconspace * 2) + iconwidth
         y = topspace + saveheight + (groupspace * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildSubnet(subnetid, regionzonename, subnetname, subnetcidr, x, y, width, height) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([leftspace - groupspace, 0])

         internetname = 'Internet'

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               publicnode = self.shapes.buildPublicGateway(subnetpubgateid, regionzonename, pubgatename, pubgatefipip, firsticonx, firsticony, iconwidth, iconheight)
               nodes.append(publicnode)

               routername = vpcname + '-router'
               publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid)
               links.append(publiclink1)
               publiclink2 = self.shapes.buildSingleArrow('', subnetpubgateid, routername)
               links.append(publiclink2)

            elif subnetpubgateid != save_subnetpubgateid:
               printerror(invalidpublicgatewaymessage % subnetpubgateid)

            else:
               publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid)
               links.append(publiclink1)

         if vpngateip != None:
            vpngatenode = self.shapes.buildVPNGateway(vpngatename, regionzonename, vpngatename, regionzonename, vpngateip, secondiconx, secondicony, iconwidth, iconheight)
            nodes.append(vpngatenode)
                
            routername = vpcname + '-router'
            # This link can be assumed since everything inside zone is accesible by the VPN.
            #vpnlink1 = gensolidlink_doublearrow(userdata, '', subnetname, vpngatename)
            #links.append(vpnlink1)
            vpnlink2 = self.shapes.buildDoubleArrow('', vpngatename, routername)
            links.append(vpnlink2)

            # label, source, target 
            #vpngatelink1 = gensolidlink_doublearrow(userdata, '', subnetname, vpngatename)
            #links.append(vpngatelink1)

            # label, source, target 
            #vpngatelink2 = gensolidlink_doublearrow(userdata, '', vpngatename, username)
            #links.append(vpngatelink2)

      return nodes, links, values, sizes

   def buildInstances(self, subnetid, subnetname, subnetvpcname, vpcname):
      nodes = []
      links = []
      values = []
      sizes = []

      #nicstable = self.setupdata['nics']
      subnets = self.setupdata['subnets']

      count = 0

      #for nicframe in nicstable[subnetid]:
      for instanceframe in subnets[subnetid]:
         nics = instanceframe['network_interfaces'] if self.inputtype == 'rias' else instanceframe['networkInterfaces']
         for nicframe in nics:
            #if nicframe.empty:
            #   continue

            count = count + 1

            nicname = nicframe['name']
            #nicinstanceid = nicframe['instance.id']
            nicinstanceid = instanceframe['id'] if self.inputtype == 'rias' else nicframe['instanceId']

            nicfipid = None
            nicfipip = None
            nicfipname = None
 
            #nicip = nicframe['primary_ip.address']
            nicip = nicframe['primary_ip']['address'] if self.inputtype == 'rias' else nicframe['ip']
            nicid = nicframe['id']
            fipframe = findrow(userdata, self.inputdata['floatingIPs'], 'target.id', nicid)
            if len(fipframe) > 0:
               nicfipid = fipframe['id']
               nicfipip = fipframe['address']
               nicfipname = fipframe['name']

            instanceframe = findrow(userdata, self.inputdata['instances'], 'id', nicinstanceid)
            if len(instanceframe) == 0:
               printerror(invalidinstancereferencemessage % nicinstanceid)
               continue

            instancename = instanceframe['name']
            instanceid = instanceframe['id']

            # Ensure only one NIC initially.
            if compress(instanceid) in self.saveinstances:
               continue
            else:
               self.saveinstances.append(compress(instanceid))

            instanceOS = instanceframe['image.name']
            if instanceOS == None:
               instanceOS = 'Unknown OS'
            instanceprofile = instanceframe['profile.name'] 
            instancememory = instanceframe['memory']

            bandwidth = instanceframe['bandwidth']
            if bandwidth == '' or (isinstance(bandwidth, float) and math.isnan(bandwidth)):
               instancecpuspeed = 0
            else:
               instancecpuspeed = int(instanceframe['bandwidth'] / 1000)

            instancecpucount = instanceframe['vcpu.count']

            osdetails = instanceOS
            profiledetails = instanceprofile
            storagedetails = '100GB/3000IOPS'

            if self.outputdetail == "low": 
               width = iconwidth
               height = iconheight
               extrawidth = width * 3
               extraheight = height * 2
               x = width + (extrawidth * (count - 1)) + (groupspace * count)
               y = topspace
            else:
               width = 240
               height = 152
               x = (width * (count - 1)) + (groupspace * count) 
               y = topspace

            #SAVE x = (width * (count - 1)) + (groupspace * count) 
            #SAVE y = topspace

            #SAVE instancenode = geninstance(userdata, instancename, subnetname, nicip, instancedetails, width, height, x, y)

            #SAVE osnode = geninstanceexpandedstack(userdata, instancename, subnetname, nicip, width, height, x, y)

            bastion = False

            if self.outputdetail == "low": 
               if instancename.lower().find("bastion") != -1:
                  bastion = True
                  instancenode = self.shapes.buildInstanceBastion(instanceid, subnetid, instancename, nicip, x, y, width, height)
               else:
                  instancenode = self.shapes.buildInstance(instanceid, subnetid, instancename, nicip, x, y, width, height)
               sizes.append([extrawidth, extraheight])
            else:
               if instancename.lower().find("bastion") != -1:
                  bastion = True
                  instancenode = self.shapes.buildInstanceBastionExpandedStack(instanceid, subnetid, instancename, nicip, x, y, width, height)
               else:
                  instancenode = self.shapes.buildInstanceExpandedStack(instanceid, subnetid, instancename, nicip, x, y, width, height)
               sizes.append([width, height])

            nodes.append(instancenode)

            if self.outputdetail != "low": 
               textwidth = width - (textgroupspace * 2)
               textheight = height - (texttopspace + textgroupspace)

               textx = textgroupspace
               texty = texttopspace

               textid = nicid + ':details'
               textname = instancename + ':details'

               stackwidth = 252
               stackheight = 16
               stackx = 16
               stacky = 64
               osnode = self.shapes.buildItemOS(nicid + ':' + osdetails, instanceid, osdetails, '', stackx, stacky, stackwidth, stackheight)
               profilenode = ''
               if profiledetails[0] == 'b':
                  profilenode = self.shapes.buildItemProfileBalanced(nicid + ':' + profiledetails, instanceid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight)
               elif profiledetails[0] == 'c' or profiledetails[0] == 'g':
                  profilenode = self.shapes.buildItemProfileCompute(nicid + ':' + profiledetails, instanceid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight)
               elif profiledetails[0] == 'm' or profiledetails[0] == 'u' or profiledetails[1] == 'v':
                  profilenode = self.shapes.buildItemProfileMemory(nicid + ':' + profiledetails, instanceid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight)
               storagenode = self.shapes.buildItemBlockStorage(nicid + ':' + storagedetails, instanceid, storagedetails, '', stackx, stacky + 48, stackwidth, stackheight)

               nodes.append(osnode)
               nodes.append(profilenode)
               nodes.append(storagenode)

            if nicfipip != None:
               # Save for option to show FIP icon.
               #SAVE fipnode = genfloatingip(userdata, nicfipname, nicfipip)
               #SAVE nodes.append(fipnode)
               #SAVE fiplink1 = gensolidlink_doublearrow(userdata, '', instancename, nicfipname)
               #SAVE links.append(fiplink1)
               #SAVE internetname = 'Internet'
               #SAVE fiplink2 = gensolidlink_doublearrow(userdata, '', nicfipname, internetname)
               #SAVE links.append(fiplink2)

               routername = vpcname + '-router'
               iplabel =  "fip:" + nicfipip
               fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername)
               links.append(fiplink)

      return nodes, links, values, sizes

   def buildLoadBalancers(self, vpcname, vpcid):
      nodes = []
      links = []

      lbtable = self.inputdata['loadBalancers'] 

      if len(lbtable) == 0:
         return nodes, links

      for lbindex, lb in lbtable.iterrows():
         lbid = lb['id']
         lbname = lb['name']

         if lbname[0:4] == 'kube':
            printerror(invalidlbreferencemessage % lbname)
            continue

         if self.inputtype == 'rias':
            lbispublic = lb['is_public']
            lbprivateips = lb['private_ips']
            lbpublicips = lb['public_ips']
         else:  # yaml
            lbispublic = lb['isPublic']
            lbprivateips = lb['privateIPs']
            lbpublicips = lb['publicIPs']

         if lbispublic == False:
            printerror(invalidlbprivatemessage % lbname)
            continue

         lbpubliciplist = ""
         for lbpublicip in lbpublicips:
            if self.inputtype == 'rias':
               ip = lbpublicip['address']
            else:
               ip = lbpublicip
            if lbpubliciplist == "":
               lbpubliciplist = ip
            else:
               lbpubliciplist = lbpubliciplist + " " + ip

         lbgenerated = False
                
         memberdata = findrow(userdata, self.inputdata['loadBalancerMembers'], 'id', lbid)
         if len(memberdata) > 0:
            membersall = memberdata['members']
         else:
            membersall = {}

         for members in membersall:
            for member in members:
               if self.inputtype == 'rias':
                  target = member['target']
                  address = target['address']
               else:
                  instanceid = member['instanceId']
                  instance = findrow(userdata, self.inputdata['instances'], 'id', instanceid)
                  if len(instance) > 0:
                     addressarray = instance['ipAddresses']
                     address = addressarray[0]
                  else:
                     address = "0.0.0.0"

               nicdata = findrow(userdata, self.inputdata['networkInterfaces'], 'primary_ip.address', address)
               if len(nicdata) != 0:
                  nicinstanceid = nicdata['instance.id']
                  instanceframe = findrow(userdata, self.inputdata['instances'], 'id', nicinstanceid)
                  instancename = instanceframe['name']
                  instancevpcid = instanceframe['vpc.id']

                  if instancevpcid == vpcid: 
                     if not lbgenerated:
                        lbgenerated = True
                        # TODO Handle spacing for > 1 LBs.
                        lbnode = self.shapes.buildLoadBalancer(lbname, vpcname, lbpubliciplist, secondiconx, secondicony, iconwidth, iconheight)
                        nodes.append(lbnode)
                        routername = vpcname + '-router'
                        lblink = self.shapes.buildDoubleArrow('', lbname, routername)
                        links.append(lblink)
                
                     # label, source, target 
                     instancelink = self.shapes.buildDoubleArrow('', instancename, lbname)
                     links.append(instancelink)

      return nodes, links
