# @file diagram.py
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

# Hierarchy:
#   diagrams.py - iterate diagram objects, invokes shapes.py
#   shapes.py - build ibm types, invokes types.py
#   types.py - build drawio types, invokes xml.py with tables.py
#   elements.py - build drawio objects  

from math import isnan

from common.common import Common

from diagram.constants import *
from diagram.shapes import Shapes

class Diagram:
   data = None
   common = None
   shapes = None

   def __init__(self, common, data):
      self.common = common
      self.data = data
      self.shapes = Shapes(common)

   def buildDiagrams(self):
      outputFolder = self.common.getOutputFolder()
      if outputFolder[-1] != '/':
         self.common.setOutputFolder(outputFolder + '/')

      regiondata = {}

      for regionname, regionvalues in self.data.getRegionTable().items():
         vpcdata = self.buildVPCs(regionname, regionvalues)
         regiondata[regionname] = vpcdata

      for regionname, regionvalues in regiondata.items():
         #if self.userregion != "all" and self.userregion != regionname:
         if self.common.getRegion().value != "all" and self.common.getRegion().value != regionname:
            # Covers the case for Yaml data which includes all regions whereas RIAS data can include single or all regions.
            continue
         for vpcname, vpcvalues in regionvalues.items():
            self.shapes.buildXML(vpcvalues, regionname + ':' + vpcname)
            if self.common.isVPCSplit():
               self.shapes.dumpXML(regionname + "_" + vpcname + "_" + self.common.getOutputFile(), self.common.getOutputFolder())
               self.shapes.resetXML()
         if self.common.isRegionSplit():
            self.shapes.dumpXML(regionname + "_" + self.common.getOutputFile(), self.common.getOutputFolder())
            self.shapes.resetXML()

         if self.common.isSingleSplit():
            self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())

   def buildVPCs(self, regionname, regionvalues):
      data = {}

      if self.common.isLinkLayout():
         publicx = 0
         publicy = 0
         publicnode = self.shapes.buildShape('PublicNetwork', ShapeKind.LOCATION, FillPalette.WHITE, PUBLIC_NETWORK_NAME, NO_PARENT, PUBLIC_NETWORK_NAME, '', '', publicx, publicy, PUBLIC_NETWORK_WIDTH, PUBLIC_NETWORK_HEIGHT, None)
         publicusernode = self.shapes.buildShape('User', ShapeKind.ACTOR, FillPalette.NONE, PUBLIC_USER_NAME, PUBLIC_NETWORK_NAME, PUBLIC_USER_NAME, '', '', FIRST_ICON_X, FIRST_ICON_Y, ICON_WIDTH, ICON_HEIGHT, None)
         publicinternetnode = self.shapes.buildShape('Internet', ShapeKind.NODE, FillPalette.NONE, INTERNET_NAME, PUBLIC_NETWORK_NAME, INTERNET_NAME, '', '', SECOND_ICON_X, SECOND_ICON_Y, ICON_WIDTH, ICON_HEIGHT, None)

         enterprisex = 0
         enterprisey = PUBLIC_NETWORK_HEIGHT + GROUP_SPACE
         enterprisenode = self.shapes.buildShape('EnterpriseNetwork', ShapeKind.LOCATION, FillPalette.WHITE, ENTERPRISE_NETWORK_NAME, NO_PARENT, ENTERPRISE_NETWORK_NAME, '', '', enterprisex, enterprisey, ENTERPRISE_NETWORK_WIDTH, ENTERPRISE_NETWORK_HEIGHT, None)
         enterpriseusernode = self.shapes.buildShape('User', ShapeKind.ACTOR, FillPalette.NONE, ENTERPRISE_USER_NAME, ENTERPRISE_NETWORK_NAME, ENTERPRISE_USER_NAME, '', '', FIRST_ICON_X, FIRST_ICON_Y, ICON_WIDTH, ICON_HEIGHT, None)

      if self.common.isLogicalShapes():
         cloudname = "Cloud"
      else:
         cloudname = "IBM Cloud"

      nodes = []
      links = []
      values = []

      saveheight = 0
      savewidth = 0

      previousheight = 0
      previouswidth = 0

      #savex = 0
      #savey = 0

      count = 0

      for vpcid in regionvalues:
         #vpcframe = findrow(user, self.inputdata['vpcs'], 'id', vpcid)
         vpcframe = self.data.getVPC(vpcid)
         if len(vpcframe) == 0:
            self.common.printInvalidVPC(vpcid)
         else:
            count = count + 1

            vpcname = vpcframe['name']
            vpcid = vpcframe['id']

            if not self.common.isDesignatedVPC(vpcid):
               continue
         
            if 'availabilityZones' in vpcframe:
               usercidrs = vpcframe['availabilityZones']
            else:
               usercidrs = None

            if not self.common.isCombineSplit():
               nodes = []
               links = []
               values = []
            
            if self.common.isLinkLayout():
               nodes.append(publicnode)
               nodes.append(publicusernode)
               nodes.append(publicinternetnode)

               #SAVE publiclink = genlink(user, publicname, publicname, internetname)
               #SAVE links.append(publiclink)

               publicuserlink = self.shapes.buildDoubleArrow('', INTERNET_NAME, PUBLIC_USER_NAME, None)
               links.append(publicuserlink)

               nodes.append(enterprisenode)
               nodes.append(enterpriseusernode)

               enterpriseuserlink = self.shapes.buildDoubleArrow('', INTERNET_NAME, ENTERPRISE_USER_NAME, None)
               links.append(enterpriseuserlink)

            zonenodes, zonelinks, zonevalues, zonesizes = self.buildZones(vpcname, vpcid, usercidrs)
            nodes = nodes + zonenodes
            links = links + zonelinks
            values = values + zonevalues

            width = ICON_WIDTH
            height = ICON_HEIGHT

            if self.common.isLinkLayout():
               routername = vpcname + '-router'
               routernode = self.shapes.buildShape('Router', ShapeKind.NODE, FillPalette.NONE, routername, vpcid, '', '', '', FIRST_ICON_X, FIRST_ICON_Y, width, height, None)
               nodes.append(routernode)

               routerlink = self.shapes.buildDoubleArrow('', routername, INTERNET_NAME, None)
               links.append(routerlink)

            width = 0
            height = 0

            #x = GROUP_SPACE
            #y = TOP_SPACE

            if self.common.isVerticalLayout():
               for size in zonesizes:
                  if size[0] > width:
                     width = size[0]
                  height += size[1] + GROUP_SPACE

               width += LEFT_SPACE + GROUP_SPACE  # space after inner groups
               height += TOP_SPACE # space at top of outer group to top inner group
               height -= GROUP_SPACE  # TODO Remove extra groupspace.
            else:
               for size in zonesizes:
                  if size[1] > height:
                     height = size[1]
                  width += size[0] + GROUP_SPACE

               #width += LEFT_SPACE  # space after inner groups
               height += TOP_SPACE # space at top of outer group to top inner group
               height += GROUP_SPACE  # TODO Remove extra groupspace.

            #if count > 1:
            #   if self.common.isCombineSplit():
            #      if self.common.isVerticalLayout():
            #         x = savex
            #         y = savey + height + GROUP_SPACE
            #      else:
            #         x = savex + width + GROUP_SPACE
            #         y = savey

            #savex = x
            #savey = y
            #print(vpcname)
            #print(x)
            #print(y)
            #print(width)
            #print(height)

            #vpcnode = self.shapes.buildVPC(vpcid, regionname, vpcname, '', x, y, width, height, None) 
            #nodes.append(vpcnode)

            #x = 30
            #y = 70

            #width += GROUP_SPACE * 2
            #height += TOP_SPACE + GROUP_SPACE

            if self.common.isCombineSplit():
               if self.common.isVerticalLayout():
                  if width > savewidth:
                     savewidth = width
                  saveheight += height + GROUP_SPACE
               else:
                  if height > saveheight:
                     saveheight = height
                  savewidth += width + GROUP_SPACE

               if count == 1:
                  x = GROUP_SPACE
                  y = TOP_SPACE
               elif self.common.isVerticalLayout():
                  #x = GROUP_SPACE
                  #y = saveheight + GROUP_SPACE
                  #x += GROUP_SPACE
                  y += previousheight + GROUP_SPACE
               else:
                  #x = savewidth + GROUP_SPACE
                  #y = TOP_SPACE
                  x += previouswidth + GROUP_SPACE
                  #y += TOP_SPACE

               previousheight = height + GROUP_SPACE
               previouswidth = width

               vpcnode = self.shapes.buildShape('VPC', ShapeKind.LOCATION, FillPalette.WHITE, vpcid, regionname, vpcname, '', '', x, y, width, height, None) 
               nodes.append(vpcnode)
            else:
               x = GROUP_SPACE
               y = TOP_SPACE

               vpcnode = self.shapes.buildShape('VPC', ShapeKind.LOCATION, FillPalette.WHITE, vpcid, regionname, vpcname, '', '', x, y, width, height, None) 
               nodes.append(vpcnode)

               x = 30
               y = 70

               width += GROUP_SPACE * 2
               height += TOP_SPACE + GROUP_SPACE

               regionnode = self.shapes.buildShape('Region', ShapeKind.LOCATION, ComponentFill.BACKEND, regionname, cloudname, regionname, '', '', x, y, width, height, None)
               nodes.append(regionnode)
         
               lbnodes, lblinks  = self.buildLoadBalancers(vpcname, vpcid)
               if len(lbnodes) > 0:
                  nodes = nodes + lbnodes
                  links = links + lblinks

               #publicwidth = (groupspace * 2) + (48 * 3)
               #x  = (groupspace * 4) + (48 * 3)  # Allow space for public network.
               x = PUBLIC_NETWORK_WIDTH + GROUP_SPACE  # Allow space for public network.
               y = 0

               width += GROUP_SPACE * 2
               height += TOP_SPACE + GROUP_SPACE

               cloudnode = self.shapes.buildShape('Cloud', ShapeKind.LOCATION, FillPalette.WHITE, cloudname, NO_PARENT, cloudname, '', '', x, y, width, height, None)
               nodes.append(cloudnode)
   
               data[vpcname] = {'nodes': nodes, 'values': values, 'links': links}

      if self.common.isCombineSplit():
         x = 30
         y = 70

         width = savewidth
         height = saveheight

         width += GROUP_SPACE * 2
         height += TOP_SPACE + GROUP_SPACE

         regionnode = self.shapes.buildShape('Region', ShapeKind.LOCATION, ComponentFill.BACKEND, regionname, cloudname, regionname, '', '', x, y, width, height, None)
         nodes.append(regionnode)
         
         #lbnodes, lblinks  = self.buildLoadBalancers(vpcname, vpcid)
         #if len(lbnodes) > 0:
         #   nodes = nodes + lbnodes
         #   links = links + lblinks

         #publicwidth = (groupspace * 2) + (48 * 3)
         #x  = (groupspace * 4) + (48 * 3)  # Allow space for public network.
         x = PUBLIC_NETWORK_WIDTH + GROUP_SPACE  # Allow space for public network.
         y = 0

         width += GROUP_SPACE * 2
         height += TOP_SPACE + GROUP_SPACE

         cloudnode = self.shapes.buildShape('Cloud', ShapeKind.LOCATION, FillPalette.WHITE, cloudname, '', cloudname, '', '', x, y, width, height, None)
         nodes.append(cloudnode)
   
         data[regionname] = {'nodes': nodes, 'values': values, 'links': links}

      return data

   def buildZones(self, vpcname, vpcid, usercidrs):
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0
      savewidth = 0

      vpcTable = self.data.getVPCTable() 
      count = 0
      for regionzonename in vpcTable[vpcid]:
         count = count + 1

         if self.common.isLinkLayout():
            zonelink = self.shapes.buildLink(regionzonename + ':' + vpcname, regionzonename, vpcname, None)
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

            height = height + size[1] + GROUP_SPACE

         width = LEFT_SPACE + width + GROUP_SPACE
         height = height + TOP_SPACE  # space at top of outer group to top inner group
         height = height - GROUP_SPACE

         if self.common.isVerticalLayout():
            x = (ICON_SPACE * 2) + ICON_WIDTH
            y = TOP_SPACE + saveheight + (GROUP_SPACE * (count - 1))
            saveheight += height
         else:
            x = (ICON_SPACE * 2) + ICON_WIDTH + savewidth + (GROUP_SPACE * (count - 1))
            y = TOP_SPACE
            savewidth += width

         zonename = regionzonename.split(':')[1]

         if usercidrs != None:
            for usercidr in usercidrs:
                if zonename == usercidr['name']:
                   zonecidr = usercidr['addressPrefix']
                   break
                else:
                   zonecidr = ''
         else:
            zonecidr = self.getZoneCIDR(zonename)

         zonenode = self.shapes.buildShape('AvailabilityZone', ShapeKind.LOCATION, ComponentFill.BACKEND, regionzonename, vpcid, regionzonename, zonecidr, '', x, y, width, height, None)
         nodes.append(zonenode)

         sizes.append([width, height])

         if count == 1:
            sizes.append([LEFT_SPACE - GROUP_SPACE, 0])

      return nodes, links, values, sizes

   def buildSubnets(self, zonename, vpcname): 
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      zoneTable = self.data.getZoneTable()
      count = 0
      save_subnetpubgateid = None

      for subnetid in zoneTable[zonename]:
         count = count + 1
         pubgateid = None

         width = 0
         height = 0

         #subnetframe = findrow(user, self.inputdata['subnets'], 'id', subnetid)
         subnetframe = self.data.getSubnet(subnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         #vpcframe = findrow(user, self.inputdata['vpcs'], 'id', subnetvpcid)
         vpcframe = self.data.getVPC(subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = zonename.split(':')[0]
         regionzonename = regionname + ':' + subnetzonename;

         if self.common.isLinkLayout():
            zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname, None)
            #SAVE links.append(zonelink)

         if 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            #pubgateframe = findrow(user, self.inputdata['publicGateways'], 'id', subnetpubgateid)
            pubgateframe = self.data.getPublicGateway(subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.common.isInputRIAS(): 
                  pubgatefipip = pubgateframe['floating_ip.address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         #vpngateip = None
         #vpngatename = None
         #vpngateways = self.data.getVPNGateways()
         #if not vpngateways.empty:
         #   vpngateframe = self.data.getVPNGateway(subnetid)
         #   #if self.common.isInputRIAS():
         #   #   vpngateframe = findrow(user, self.inputdata['vpnGateways'], 'subnet.id', subnetid)
         #   #else:
         #   #   vpngateframe = findrow(user, self.inputdata['vpnGateways'], 'networkId', subnetid)
         #   if len(vpngateframe) > 0:
         #      vpngateid = vpngateframe['id']
         #      # TODO Retrieve VPNGatewayMember[], 
         #      #      For each memberi get public_ip and private_ip.
         #      vpngateip = ''
         #      vpngatename = vpngateframe['name']
         #      vpnsubnetid = subnetid

         instancenodes, instancelinks, instancevalues, instancesizes = self.buildSubnetIcons(subnetid, subnetname, subnetvpcname, vpcname)

         nodes = nodes + instancenodes
         links = links + instancelinks
         values = values + instancevalues

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = MIN_GROUP_WIDTH
            height = MIN_GROUP_HEIGHT
         else:
            width = GROUP_SPACE
            height = 0

         for size in instancesizes:
            width = width + size[0] + GROUP_SPACE

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + TOP_SPACE + GROUP_SPACE  # space at top and bottom of group

         #SAVE x = (iconspace * 2) + iconwidth
         #SAVE y = topspace + (height * (count - 1)) + (groupspace * (count - 1))

         x = (ICON_SPACE * 2) + ICON_WIDTH
         y = TOP_SPACE + saveheight + (GROUP_SPACE * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildShape('Subnet', ShapeKind.LOCATION, FillPalette.WHITE, subnetid, regionzonename, subnetname, subnetcidr, '', x, y, width, height, None) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([LEFT_SPACE - GROUP_SPACE, 0])

         internetname = 'Internet'

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               publicnode = self.shapes.buildShape('PublicGateway', ShapeKind.NODE, FillPalette.NONE, subnetpubgateid, regionzonename, pubgatename, pubgatefipip, '', FIRST_ICON_X, FIRST_ICON_Y, ICON_WIDTH, ICON_HEIGHT, None)
               nodes.append(publicnode)

               if self.common.isLinkLayout():
                  routername = vpcname + '-router'
                  publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid, None)
                  links.append(publiclink1)
                  publiclink2 = self.shapes.buildSingleArrow('', subnetpubgateid, routername, None)
                  links.append(publiclink2)

            elif subnetpubgateid != save_subnetpubgateid:
               self.common.printInvalidPublicGateway(subnetpubgateid)

            else:
               if self.common.isLinkLayout():
                  publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid, None)
                  links.append(publiclink1)

         #if vpngateip != None:
         #    # TODO Handle >1 VPN gateways.
         #   #vpngatenode = self.shapes.buildVPNGateway(vpngatename, regionzonename, vpngatename, vpngateip, points['thirdIconX'], points['thirdIconY'], points['iconWidth'], points['iconHeight'])
         #   vpngatenode = self.shapes.buildVPNGateway(vpngatename, subnetvpcid, vpngatename, vpngateip, points['thirdIconX'], points['thirdIconY'], points['iconWidth'], points['iconHeight'], None)
         #   nodes.append(vpngatenode)
                
         #   routername = vpcname + '-router'
         #   # This link can be assumed since everything inside zone is accesible by the VPN.
         #   #vpnlink1 = gensolidlink_doublearrow(user, '', subnetname, vpngatename)
         #   #links.append(vpnlink1)
         #   vpnlink1 = self.shapes.buildDoubleArrow('', regionzonename, vpngatename, None)
         #   links.append(vpnlink1)
         #   vpnlink2 = self.shapes.buildDoubleArrow('', vpngatename, routername, None)
         #   links.append(vpnlink2)

         #   # label, source, target 
         #   #vpngatelink1 = gensolidlink_doublearrow(user, '', subnetname, vpngatename)
         #   #links.append(vpngatelink1)

         #   # label, source, target 
         #   #vpngatelink2 = gensolidlink_doublearrow(user, '', vpngatename, username)
         #   #links.append(vpngatelink2)

      return nodes, links, values, sizes

   def buildSubnetIcons(self, subnetid, subnetname, subnetvpcname, vpcname):
      nodes = []
      links = []
      values = []
      sizes = []

      #nicstable = self.setupdata['nics']
      icons = self.data.getSubnetIconTable(subnetid)

      count = 0

      #for nicframe in nicstable[subnetid]:
      for iconframe in icons:
         count = count + 1

         iconname = iconframe['name']
         iconid = iconframe['id']
         icontype = iconframe['type']

         if icontype.lower() == 'instance':
            instancename = iconname
            instanceid = iconid
            instanceframe = iconframe

            if instancename.lower().find("bastion") != -1:
               icontype += "Bastion"

            nics = self.data.getNICTable(subnetid, instanceid)

            nicips = ''
            nicid = ''
            nicfipid = None
            nicfipip = None
            nicfipname = None
            nicfips = ''

            #for nicframe in nics:
            for nicframe in nics:
               #if nicframe.empty:
               #   continue

               nicname = nicframe['name']
               #nicinstanceid = nicframe['instance.id']
               nicinstanceid = instanceframe['id'] if self.common.isInputRIAS() else nicframe['instanceId']

               #nicip = nicframe['primary_ip.address']
               nicip = nicframe['primary_ip']['address'] if self.common.isInputRIAS() else nicframe['ip']
               if nicips == '':
                  nicips = nicip
               else:
                  nicips = nicips + '<br>' + nicip
               nicid = nicframe['id']

               #fipframe = findrow(user, self.inputdata['floatingIPs'], 'target.id', nicid)
               fipframe = self.data.getFloatingIP(nicid)
               if len(fipframe) > 0:
                  nicfipid = fipframe['id']
                  nicfipip = fipframe['address']
                  nicfipname = fipframe['name']
                  if nicfips == '':
                     nicfips = nicfipip
                  else:
                     nicfips = nicfips + '<br>' + nicfipip

            secondarytext = nicips

            meta = {}

            if 'image.name' in instanceframe:
               instanceOS = instanceframe['image.name']
               if instanceOS == None:
                  instanceOS = 'Unknown OS'
               meta = meta | {'Operating-System': instanceOS}

            if 'profile.name' in instanceframe:
               instanceprofile = instanceframe['profile.name'] 
               meta = meta | {'Profile': instanceprofile}

            if 'memory' in instanceframe:
               instancememory = instanceframe['memory']
               meta = meta | {'Memory': str(instancememory)}

            if 'bandwidth' in instanceframe:
               bandwidth = instanceframe['bandwidth']
               if bandwidth == '' or (isinstance(bandwidth, float) and isnan(bandwidth)):
                  instancecpuspeed = 0
               else:
                  instancecpuspeed = int(instanceframe['bandwidth'] / 1000)
               meta = meta | {'CPU-Speed': str(instancecpuspeed)}

            if 'vcpu.count' in instanceframe:
               instancecpucount = instanceframe['vcpu.count']
               meta = meta | {'CPU-Count': str(instancecpucount)}

            if meta:
               meta = meta | {'Boot-Volume': '100GB/3000IOPS'}
            else:
               meta = None

            if nicfipip != None:
               # Save for option to show FIP icon.
               #SAVE fipnode = genfloatingip(user, nicfipname, nicfipip)
               #SAVE nodes.append(fipnode)
               #SAVE fiplink1 = gensolidlink_doublearrow(user, '', instancename, nicfipname)
               #SAVE links.append(fiplink1)
               #SAVE internetname = 'Internet'
               #SAVE fiplink2 = gensolidlink_doublearrow(user, '', nicfipname, internetname)
               #SAVE links.append(fiplink2)

               if self.common.isLinkLayout():
                  routername = vpcname + '-router'
                  iplabel =  "fip:" + nicfipip
                  fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername, None)
                  #fiplink = self.shapes.buildDoubleArrow(iplabel, nicid, routername, None)
                  links.append(fiplink)
         else:
            secondarytext = ''
            meta = None

         #if self.common.isLowDetail(): 
         width = ICON_WIDTH
         height = ICON_HEIGHT
         extrawidth = width * 3
         extraheight = height * 2
         x = width + (extrawidth * (count - 1)) + (GROUP_SPACE * count)
         y = TOP_SPACE
         #else:
         #   width = 240
         #   height = 152
         #   x = (width * (count - 1)) + (GROUP_SPACE * count) 
         #   y = TOP_SPACE

         #SAVE x = (width * (count - 1)) + (groupspace * count) 
         #SAVE y = topspace

         #SAVE instancenode = geninstance(user, instancename, subnetname, nicip, instancedetails, width, height, x, y)

         #SAVE osnode = geninstanceexpandedstack(user, instancename, subnetname, nicip, width, height, x, y)

         #bastion = False

         #if self.common.isLowDetail(): 
         #   iconnode = self.shapes.buildIcon(nicid, subnetid, instancename, nicips, icontype, x, y, width, height, meta)
         #   sizes.append([extrawidth, extraheight])
         #else:
         #   iconnode = self.shapes.buildIconExpandedStack(nicid, subnetid, instancename, nicips, icontype, x, y, width, height, meta)
         #   sizes.append([width, height])

         iconnode = self.shapes.buildShape(icontype, ShapeKind.NODE, FillPalette.NONE, iconid, subnetid, iconname, secondarytext, icontype, x, y, width, height, meta)
         sizes.append([extrawidth, extraheight])

         nodes.append(iconnode)

         #if not self.common.isLowDetail(): 
         #   textwidth = width - (points['textGroupSpace'] * 2)
         #   textheight = height - (points['textTopSpace'] + points['textGroupSpace'])

         #   textx = points['textGroupSpace']
         #   texty = points['textTopSpace']

         #   #textid = nicid + ':details'
         #   textid = instanceid + ':details'
         #   textname = instancename + ':details'

         #   stackwidth = 252
         #   stackheight = 16
         #   stackx = 16
         #   stacky = 64
         #   osnode = self.shapes.buildItemOS(nicid + ':' + osdetails, nicid, osdetails, '', stackx, stacky, stackwidth, stackheight, None)
         #   profilenode = ''
         #   if profiledetails[0] == 'b':
         #      profilenode = self.shapes.buildItemProfileBalanced(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
         #   elif profiledetails[0] == 'c' or profiledetails[0] == 'g':
         #      profilenode = self.shapes.buildItemProfileCompute(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
         #   elif profiledetails[0] == 'm' or profiledetails[0] == 'u' or profiledetails[1] == 'v':
         #      profilenode = self.shapes.buildItemProfileMemory(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
         #   storagenode = self.shapes.buildItemBlockStorage(nicid + ':' + storagedetails, nicid, storagedetails, '', stackx, stacky + 48, stackwidth, stackheight, None)

         #   nodes.append(osnode)
         #   nodes.append(profilenode)
         #   nodes.append(storagenode)

         #if nicfipip != None:
         #   # Save for option to show FIP icon.
         #   #SAVE fipnode = genfloatingip(user, nicfipname, nicfipip)
         #   #SAVE nodes.append(fipnode)
         #   #SAVE fiplink1 = gensolidlink_doublearrow(user, '', instancename, nicfipname)
         #   #SAVE links.append(fiplink1)
         #   #SAVE internetname = 'Internet'
         #   #SAVE fiplink2 = gensolidlink_doublearrow(user, '', nicfipname, internetname)
         #   #SAVE links.append(fiplink2)

         #   routername = vpcname + '-router'
         #   iplabel =  "fip:" + nicfipip
         #   #fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername)
         #   fiplink = self.shapes.buildDoubleArrow(iplabel, nicid, routername, None)
         #   links.append(fiplink)

      return nodes, links, values, sizes

   def buildServices(self, regionname): 
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      serviceTable = self.data.getServiceTable()
      count = 0

      for serviceid in zoneTable[zonename]:
         count = count + 1
         pubgateid = None

         width = 0
         height = 0

         #subnetframe = findrow(user, self.inputdata['subnets'], 'id', subnetid)
         subnetframe = self.data.getSubnet(subnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         #vpcframe = findrow(user, self.inputdata['vpcs'], 'id', subnetvpcid)
         vpcframe = self.data.getVPC(subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = zonename.split(':')[0]
         regionzonename = regionname + ':' + subnetzonename;

         if self.common.isLinkLayout():
            zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname, None)
            #SAVE links.append(zonelink)

         if 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            #pubgateframe = findrow(user, self.inputdata['publicGateways'], 'id', subnetpubgateid)
            pubgateframe = self.data.getPublicGateway(subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.common.isInputRIAS(): 
                  pubgatefipip = pubgateframe['floating_ip.address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         instancenodes, instancelinks, instancevalues, instancesizes = self.buildSubnetIcons(subnetid, subnetname, subnetvpcname, vpcname)

         nodes = nodes + instancenodes
         links = links + instancelinks
         values = values + instancevalues

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = MIN_GROUP_WIDTH
            height = MIN_GROUP_HEIGHT
         else:
            width = GROUP_SPACE
            height = 0

         for size in instancesizes:
            width = width + size[0] + GROUP_SPACE

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + TOP_SPACE + GROUP_SPACE  # space at top and bottom of group

         x = (ICON_SPACE * 2) + ICON_WIDTH
         y = TOP_SPACE + saveheight + (GROUP_SPACE * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildShape('Subnet', ShapeKind.LOCATION, FillPalette.WHITE, subnetid, regionzonename, subnetname, subnetcidr, '', x, y, width, height, None) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([LEFT_SPACE - GROUP_SPACE, 0])

      return nodes, links, values, sizes

   def buildLoadBalancers(self, vpcname, vpcid):
      nodes = []
      links = []

      lbs = self.data.getLoadBalancers(vpcid)
      if lbs != None:
         for lbpool in lbs:
            #for lbmembers in lbs:
            for lbkey in lbpool:
               #for lbid, members in lbmembers.items():
               for lbid, members in lbpool[lbkey].items():
                  lb = self.data.getLoadBalancer(lbid)
                  lbid = lb['id']
                  lbname = lb['name']

                  if lbname[0:4] == 'kube':
                     # Kube LB not implemented for now.
                     # self.common.printInvalidLoadBalancer(lbname)
                     continue

                  if self.common.isInputRIAS():
                     lbispublic = lb['is_public']
                     lbprivateips = lb['private_ips']
                     lbpublicips = lb['public_ips']
                  else:  # yaml
                     lbispublic = lb['isPublic']
                     lbprivateips = lb['privateIPs']
                     lbpublicips = lb['publicIPs']
 
                  lbiplist = ""
                  if lbispublic == False:
                     for lbprivateip in lbprivateips:
                        if self.common.isInputRIAS():
                           ip = lbprivateip['address']
                        else:
                           ip = lbprivateip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip
                  else:
                     for lbpublicip in lbpublicips:
                        if self.common.isInputRIAS():
                           ip = lbpublicip['address']
                        else:
                           ip = lbpublicip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip

                  lbgenerated = False
               
                  for member in members:
                     if self.common.isInputRIAS():
                        # TODO Get instance id.
                        target = member['target']
                        address = target['address']
                     else:
                        instanceid = member['instanceId']
                        instance = self.data.getInstance(instanceid)
                        if len(instance) > 0:
                           addressarray = instance['ipAddresses']
                           address = addressarray[0]
                        else:
                           return nodes, links

                     nicdata = self.data.getNetworkInterface(address, instanceid)
                     if len(nicdata) != 0:
                        nicid = nicdata['id']
                        nicinstanceid = nicdata['instance.id']
                        instanceframe = self.data.getInstance(nicinstanceid)
                        instancename = instanceframe['name']
                        instancevpcid = instanceframe['vpc.id']

                        if instancevpcid == vpcid: 
                           if not lbgenerated:
                              lbgenerated = True
                              # TODO Handle spacing for > 1 LBs.
                              lbnode = self.shapes.buildShape('LoadBalancer', ShapeKind.NODE, FillPalette.NONE, lbid, vpcid, lbname, lbiplist, '', SECOND_ICON_X, SECOND_ICON_Y, ICON_WIDTH, ICON_HEIGHT, None)
                              nodes.append(lbnode)

                              if self.common.isLinkLayout():
                                 routername = vpcname + '-router'
                                 lblink = self.shapes.buildDoubleArrow('', lbid, routername, None)
                                 links.append(lblink)
                 
                           if self.common.isLinkLayout():
                              # label, source, target
                              instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                              links.append(instancelink)

      return nodes, links

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = AU_SYD_1
         case 'au-syd-2': cidr = AU_SYD_2
         case 'au-syd-3': cidr = AU_SYD_3

         case 'br-sao-1': cidr = BR_SAO_1
         case 'br-sao-2': cidr = BR_SAO_2
         case 'br-sao-3': cidr = BR_SAO_3

         case 'ca-tor-1': cidr = CA_TOR_1
         case 'ca-tor-2': cidr = CA_TOR_2
         case 'ca-tor-3': cidr = CA_TOR_3

         case 'eu-de-1': cidr = EU_DE_1
         case 'eu-de-2': cidr = EU_DE_2
         case 'eu-de-3': cidr = EU_DE_3

         case 'eu-gb-1': cidr = EU_GB_1
         case 'eu-gb-2': cidr = EU_GB_2
         case 'eu-gb-3': cidr = EU_GB_3

         case 'jp-osa-1': cidr = JP_OSA_1
         case 'jp-osa-2': cidr = JP_OSA_2
         case 'jp-osa-3': cidr = JP_OSA_3

         case 'jp-tok-1': cidr = JP_TOK_1
         case 'jp-tok-2': cidr = JP_TOK_2
         case 'jp-tok-3': cidr = JP_TOK_3

         case 'us-east-1': cidr = US_EAST_1
         case 'us-east-2': cidr = US_EAST_2
         case 'us-east-3': cidr = US_EAST_3

         case 'us-south-1': cidr = US_SOUTH_1
         case 'us-south-2': cidr = US_SOUTH_2
         case 'us-south-3': cidr = US_SOUTH_3

         case _: cidr = ''

      return cidr
