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

from diagram.constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from diagram.shapes import Shapes

class Diagram:
   data = None
   common = None
   shapes = None
   cloudname = ""

   def __init__(self, common, data):
      self.common = common
      self.data = data
      self.shapes = Shapes(common)
      self.cloudname = ShapeName.CLOUD.value if self.common.isLogicalShapes() else ShapeName.IBM_CLOUD.value

   def buildDiagrams(self):
      outputFolder = self.common.getOutputFolder()
      if outputFolder[-1] != '/':
         self.common.setOutputFolder(outputFolder + '/')

      clouddata = self.buildAll()

      for regionname, regionvalues in clouddata.items():
         if self.common.getRegion().value != "all" and self.common.getRegion().value != regionname:
            # Covers the case for Yaml data which includes all regions whereas RIAS data can include single or all regions.
            continue
         if self.common.isCombineSplit():
            self.shapes.buildXML(regionvalues, regionname)
         else:
            for vpcid, vpcvalues in regionvalues.items():
              vpcnames = vpcid.split(':')
              self.shapes.buildXML(vpcvalues, vpcnames[1])

         self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())
         self.shapes.resetXML()

      return

   def buildAll(self):
      newvpcdata = {}
      regiondata = {}

      regionx = 30
      regiony = 70

      cloudx = 30
      cloudy = 70

      cloudwidth = 0
      cloudheight = 0

      nodes = []
      links = []
      values = []

      count = 0

      for regionname, regionvalues in self.data.getRegionTable().items():
         count += 1
         regionwidth = 0
         regionheight = 0

         vpcdata = self.buildVPCs(regionname, regionvalues)

         if self.common.isCombineSplit():
            # Loop thru all vpcs in region adding a region that contains all VPCs in that region.

            for vpcid, vpcvalues in vpcdata.items():
               nodes += vpcvalues['nodes']
               links += vpcvalues['links']
               values += vpcvalues['values']
               size = vpcvalues['sizes']

               regionwidth += size[0] + ShapePos.GROUP_SPACE.value
               if size[1] > regionheight:
                  regionheight = size[1]

            regionwidth += ShapePos.GROUP_SPACE.value
            regionheight += ShapePos.TOP_SPACE.value + ShapePos.GROUP_SPACE.value

            if regionwidth > cloudwidth:
               cloudwidth = regionwidth
            cloudheight += regionheight

            if count > 1:
              regiony += regionheight + ShapePos.GROUP_SPACE.value

            nodes, links, values = self.buildRegion(regionname, None, nodes, links, values, regionx, regiony, regionwidth, regionheight)
         else:
            # Loop thru all vpcs in region adding a region to each VPC in that region.

            for vpcid, vpcvalues in vpcdata.items():
               nodes = vpcvalues['nodes']
               links = vpcvalues['links']
               values = vpcvalues['values']
               size = vpcvalues['sizes']

               regionwidth = size[0] + ShapePos.GROUP_SPACE.value * 2
               regionheight = size[1] +  ShapePos.TOP_SPACE.value + ShapePos.GROUP_SPACE.value

               vpcnames = vpcid.split(':')

               nodes, links, values = self.buildRegion(regionname, vpcnames[0], nodes, links, values, regionx, regiony, regionwidth, regionheight)

               cloudwidth = regionwidth + ShapePos.GROUP_SPACE.value * 2
               cloudheight = regionheight + ShapePos.TOP_SPACE.value + ShapePos.GROUP_SPACE.value

               nodes, links, values = self.buildCloud(self.cloudname, vpcnames[0], nodes, links, values, cloudx, cloudy, cloudwidth, cloudheight)
               newvpcdata[vpcid] = {'nodes': nodes, 'links': links, 'values': values}

            regiondata[regionname] = newvpcdata

      if self.common.isCombineSplit():
         cloudx = 30
         cloudy = 70

         cloudwidth += ShapePos.GROUP_SPACE.value * 2
         cloudheight += ShapePos.TOP_SPACE.value + (ShapePos.GROUP_SPACE.value * count)

         nodes, links, values = self.buildCloud(self.cloudname, None, nodes, links, values, cloudx, cloudy, cloudwidth, cloudheight)

         regiondata[self.cloudname] = {'nodes': nodes, 'links': links, 'values': values}

      return regiondata

   def buildCloud(self, cloudname, vpcid, nodes, links, values, x, y, width, height):
      if vpcid == None:
         cloudid = cloudname.replace(" ", "")
      else:
         cloudid = cloudname.replace(" ", "") + ':' + vpcid

      x = ShapePos.PUBLIC_NETWORK_WIDTH.value + ShapePos.GROUP_SPACE.value  # Allow space for public network.
      y = 0

      cloudnode = self.shapes.buildShape('Cloud', ShapeKind.LOCATION, FillPalette.WHITE, cloudid, ShapeName.NO_PARENT.value, cloudname, '', '', x, y, width, height, None)
      nodes.append(cloudnode)

      if self.common.isLinks():
         nodes, links, values  = self.buildPublic(nodes, links, values)
         nodes, links, values  = self.buildEnterprise(nodes, links, values)

      return nodes, links, values

   def buildRegion(self, regionname, vpcid, nodes, links, values, x, y, width, height):
      if vpcid == None:
         regionid = regionname.replace(" ", "")
         cloudid = self.cloudname.replace(" ", "")
      else:
         regionid = regionname.replace(" ", "") + ':' + vpcid
         cloudid = self.cloudname.replace(" ", "") + ':' + vpcid

      regionnode = self.shapes.buildShape('Region', ShapeKind.LOCATION, ComponentFill.BACKEND, regionid, cloudid, regionname, '', '', x, y, width, height, None)
      nodes.append(regionnode)

      return nodes, links, values

   def buildPublic(self, nodes, links, values):
      publicx = 0
      publicy = 0

      publicnode = self.shapes.buildShape('PublicNetwork', ShapeKind.LOCATION, FillPalette.WHITE, ShapeName.PUBLIC_NETWORK.value, ShapeName.NO_PARENT.value, ShapeName.PUBLIC_NETWORK.value, '', '', publicx, publicy, ShapePos.PUBLIC_NETWORK_WIDTH.value, ShapePos.PUBLIC_NETWORK_HEIGHT.value, None)
      publicusernode = self.shapes.buildShape('User', ShapeKind.ACTOR, FillPalette.NONE, ShapeName.PUBLIC_USER.value, ShapeName.PUBLIC_NETWORK.value, ShapeName.PUBLIC_USER.value, '', '', ShapePos.FIRST_ICON_X.value, ShapePos.FIRST_ICON_Y.value, ShapePos.ICON_WIDTH.value, ShapePos.ICON_HEIGHT.value, None)
      publicinternetnode = self.shapes.buildShape('Internet', ShapeKind.NODE, FillPalette.NONE, ShapeName.INTERNET.value, ShapeName.PUBLIC_NETWORK.value, ShapeName.INTERNET.value, '', '', ShapePos.SECOND_ICON_X.value, ShapePos.SECOND_ICON_Y.value, ShapePos.ICON_WIDTH.value, ShapePos.ICON_HEIGHT.value, None)
      
      nodes.append(publicnode)
      nodes.append(publicusernode)
      nodes.append(publicinternetnode)
      publicuserlink = self.shapes.buildDoubleArrow('', ShapeName.INTERNET.value, ShapeName.PUBLIC_USER.value, None)
      links.append(publicuserlink)

      return nodes, links, values

   def buildEnterprise(self, nodes, links, values):
      enterprisex = 0
      enterprisey = ShapePos.PUBLIC_NETWORK_HEIGHT.value + ShapePos.GROUP_SPACE.value

      enterprisenode = self.shapes.buildShape('EnterpriseNetwork', ShapeKind.LOCATION, FillPalette.WHITE, ShapeName.ENTERPRISE_NETWORK.value, ShapeName.NO_PARENT.value, ShapeName.ENTERPRISE_NETWORK.value, '', '', enterprisex, enterprisey, ShapePos.ENTERPRISE_NETWORK_WIDTH.value, ShapePos.ENTERPRISE_NETWORK_HEIGHT.value, None)
      enterpriseusernode = self.shapes.buildShape('User', ShapeKind.ACTOR, FillPalette.NONE, ShapeName.ENTERPRISE_USER.value, ShapeName.ENTERPRISE_NETWORK.value, ShapeName.ENTERPRISE_USER.value, '', '', ShapePos.FIRST_ICON_X.value, ShapePos.FIRST_ICON_Y.value, ShapePos.ICON_WIDTH.value, ShapePos.ICON_HEIGHT.value, None)

      nodes.append(enterprisenode)
      nodes.append(enterpriseusernode)

      enterpriseuserlink = self.shapes.buildDoubleArrow('', ShapeName.INTERNET.value, ShapeName.ENTERPRISE_USER.value, None)
      links.append(enterpriseuserlink)

      return nodes, links, values

   def buildVPCs(self, regionname, regionvalues):
      vpcdata = {}

      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0
      savewidth = 0

      previousheight = 0
      previouswidth = 0

      count = 0

      for vpcid in regionvalues:
         nodes = []
         links = []
         values = []
         sizes = []

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

            zonenodes, zonelinks, zonevalues, zonesizes = self.buildAZs(vpcname, vpcid, usercidrs)
            nodes += zonenodes
            links += zonelinks
            values += zonevalues

            width = ShapePos.ICON_WIDTH.value
            height = ShapePos.ICON_HEIGHT.value

            if self.common.isLinks():
               routername = vpcname + '-router'
               routernode = self.shapes.buildShape('Router', ShapeKind.NODE, FillPalette.NONE, routername, vpcid, '', '', '', ShapePos.FIRST_ICON_X.value, ShapePos.FIRST_ICON_Y.value, width, height, None)
               nodes.append(routernode)

               routerlink = self.shapes.buildDoubleArrow('', routername, ShapeName.INTERNET.value, None)
               links.append(routerlink)

            width = 0
            height = 0

            if self.common.isVerticalLayout():
               for size in zonesizes:
                  if size[0] > width:
                     width = size[0]
                  height += size[1] + ShapePos.GROUP_SPACE.value

               width += ShapePos.LEFT_SPACE.value + ShapePos.GROUP_SPACE.value  # space after inner groups
               height += ShapePos.TOP_SPACE.value # space at top of outer group to top inner group
               height -= ShapePos.GROUP_SPACE.value  # TODO Remove extra groupspace.
            else:
               for size in zonesizes:
                  if size[1] > height:
                     height = size[1]
                  width += size[0] + ShapePos.GROUP_SPACE.value

               height += ShapePos.TOP_SPACE.value # space at top of outer group to top inner group
               height += ShapePos.GROUP_SPACE.value  # TODO Remove extra groupspace.

            if self.common.isVerticalLayout():
               if width > savewidth:
                  savewidth = width
               saveheight += height + ShapePos.GROUP_SPACE.value
            else:
               if height > saveheight:
                  saveheight = height
               savewidth += width + ShapePos.GROUP_SPACE.value

            if count == 1 or not self.common.isCombineSplit():
               x = ShapePos.GROUP_SPACE.value
               y = ShapePos.TOP_SPACE.value
            elif self.common.isVerticalLayout():
               y += previousheight + ShapePos.GROUP_SPACE.value
            else:
               x += previouswidth + ShapePos.GROUP_SPACE.value

            previousheight = height + ShapePos.GROUP_SPACE.value
            previouswidth = width

            if self.common.isCombineSplit():
               regionid = regionname.replace(" ", "")
            else:
               regionid = regionname.replace(" ", "") + ':' + vpcid

            vpcnode = self.shapes.buildShape('VPC', ShapeKind.LOCATION, FillPalette.WHITE, vpcid, regionid, vpcname, '', '', x, y, width, height, None) 
            nodes.append(vpcnode)

            nodes, links, values  = self.buildLoadBalancers(vpcname, vpcid, nodes, links, values)

            vpcdata[vpcid + ':' + vpcname] = {'nodes': nodes, 'links': links, 'values': values, 'sizes': [width, height]}

      return vpcdata

   def buildAZs(self, vpcname, vpcid, usercidrs):
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0
      savewidth = 0

      vpcTable = self.data.getVPCTable() 
      count = 0
      for regionzonename in vpcTable[vpcid]:
         count += 1

         if self.common.isLinks():
            zonelink = self.shapes.buildLink(regionzonename + ':' + vpcname, regionzonename, vpcname, None)
            #SAVE links.append(zonelink)

         subnetnodes, subnetlinks, subnetvalues, subnetsizes = self.buildSubnets(regionzonename, vpcname)
         nodes += subnetnodes
         links += subnetlinks
         values += subnetvalues

         width = 0
         height = 0

         for size in subnetsizes:
            if size[0] > width:
               width = size[0]

            height = height + size[1] + ShapePos.GROUP_SPACE.value

         width = ShapePos.LEFT_SPACE.value + width + ShapePos.GROUP_SPACE.value
         height = height + ShapePos.TOP_SPACE.value  # space at top of outer group to top inner group
         height = height - ShapePos.GROUP_SPACE.value

         if self.common.isVerticalLayout():
            x = (ShapePos.ICON_SPACE.value * 2) + ShapePos.ICON_WIDTH.value
            y = ShapePos.TOP_SPACE.value + saveheight + (ShapePos.GROUP_SPACE.value * (count - 1))
            saveheight += height
         else:
            x = (ShapePos.ICON_SPACE.value * 2) + ShapePos.ICON_WIDTH.value + savewidth + (ShapePos.GROUP_SPACE.value * (count - 1))
            y = ShapePos.TOP_SPACE.value
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

         zonenode = self.shapes.buildShape('AvailabilityZone', ShapeKind.LOCATION, ComponentFill.BACKEND, regionzonename, vpcid, zonename, zonecidr, '', x, y, width, height, None)
         nodes.append(zonenode)

         sizes.append([width, height])

         if count == 1:
            sizes.append([ShapePos.LEFT_SPACE.value - ShapePos.GROUP_SPACE.value, 0])

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

         if self.common.isLinks():
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

         nodes += instancenodes
         links += instancelinks
         values += instancevalues

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = ShapePos.MIN_GROUP_WIDTH.value
            height = ShapePos.MIN_GROUP_HEIGHT.value
         else:
            width = ShapePos.GROUP_SPACE.value
            height = 0

         for size in instancesizes:
            width = width + size[0] + ShapePos.GROUP_SPACE.value

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + ShapePos.TOP_SPACE.value + ShapePos.GROUP_SPACE.value  # space at top and bottom of group

         #SAVE x = (iconspace * 2) + iconwidth
         #SAVE y = topspace + (height * (count - 1)) + (groupspace * (count - 1))

         x = (ShapePos.ICON_SPACE.value * 2) + ShapePos.ICON_WIDTH.value
         y = ShapePos.TOP_SPACE.value + saveheight + (ShapePos.GROUP_SPACE.value * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildShape('Subnet', ShapeKind.LOCATION, FillPalette.WHITE, subnetid, regionzonename, subnetname, subnetcidr, '', x, y, width, height, None) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([ShapePos.LEFT_SPACE.value - ShapePos.GROUP_SPACE.value, 0])

         internetname = 'Internet'

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               publicnode = self.shapes.buildShape('PublicGateway', ShapeKind.NODE, FillPalette.NONE, subnetpubgateid, regionzonename, pubgatename, pubgatefipip, '', ShapePos.FIRST_ICON_X.value, ShapePos.FIRST_ICON_Y.value, ShapePos.ICON_WIDTH.value, ShapePos.ICON_HEIGHT.value, None)
               nodes.append(publicnode)

               if self.common.isLinks():
                  routername = vpcname + '-router'
                  publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid, None)
                  links.append(publiclink1)
                  publiclink2 = self.shapes.buildSingleArrow('', subnetpubgateid, routername, None)
                  links.append(publiclink2)

            elif subnetpubgateid != save_subnetpubgateid:
               self.common.printInvalidPublicGateway(subnetpubgateid)

            else:
               if self.common.isLinks():
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

               if self.common.isLinks():
                  routername = vpcname + '-router'
                  iplabel =  "fip:" + nicfipip
                  fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername, None)
                  #fiplink = self.shapes.buildDoubleArrow(iplabel, nicid, routername, None)
                  links.append(fiplink)
         else:
            secondarytext = ''
            meta = None

         #if self.common.isLowDetail(): 
         width = ShapePos.ICON_WIDTH.value
         height = ShapePos.ICON_HEIGHT.value
         extrawidth = width * 3
         extraheight = height * 2
         x = width + (extrawidth * (count - 1)) + (ShapePos.GROUP_SPACE.value * count)
         y = ShapePos.TOP_SPACE.value
         #else:
         #   width = 240
         #   height = 152
         #   x = (width * (count - 1)) + (ShapePos.GROUP_SPACE.value * count) 
         #   y = ShapePos.TOP_SPACE.value

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

         iconnode = self.shapes.buildShape(icontype, ShapeKind.NODE, FillPalette.NONE, iconid, subnetid, iconname, secondarytext, '', x, y, width, height, meta)
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

         if self.common.isLinks():
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

         nodes += instancenodes
         links += instancelinks
         values += instancevalues
         #nodes.append(instancenodes)
         #links.append(instancelinks)
         #values.append(instancevalues)

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = MIN_GROUP_WIDTH
            height = MIN_GROUP_HEIGHT
         else:
            width = ShapePos.GROUP_SPACE.value
            height = 0

         for size in instancesizes:
            width = width + size[0] + ShapePos.GROUP_SPACE.value

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + ShapePos.TOP_SPACE.value + ShapePos.GROUP_SPACE.value  # space at top and bottom of group

         x = (ShapePos.ICON_SPACE.value * 2) + ShapePos.ICON_WIDTH.value
         y = ShapePos.TOP_SPACE.value + saveheight + (ShapePos.GROUP_SPACE.value * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildShape('Subnet', ShapeKind.LOCATION, FillPalette.WHITE, subnetid, regionzonename, subnetname, subnetcidr, '', x, y, width, height, None) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([LEFT_SPACE - ShapePos.GROUP_SPACE.value, 0])

      return nodes, links, values, sizes

   def buildLoadBalancers(self, vpcname, vpcid, nodes, links, values):
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
                           nics = instance['networkInterfaces']
                           if nics:
                              for nic in nics:
                                 address = nic['ip']
                                 break
                           else:
                              return nodes, links, values
                        else:
                           return nodes, links, values

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
                              lbnode = self.shapes.buildShape('LoadBalancer', ShapeKind.NODE, FillPalette.NONE, lbid, vpcid, lbname, lbiplist, '', ShapePos.SECOND_ICON_X.value, ShapePos.SECOND_ICON_Y.value, ShapePos.ICON_WIDTH.value, ShapePos.ICON_HEIGHT.value, None)
                              nodes.append(lbnode)

                              if self.common.isLinks():
                                 routername = vpcname + '-router'
                                 lblink = self.shapes.buildDoubleArrow('', lbid, routername, None)
                                 links.append(lblink)
                 
                           if self.common.isLinks():
                              # label, source, target
                              #instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                              instancelink = self.shapes.buildDoubleArrow('', instanceid, lbid, None)
                              links.append(instancelink)

      return nodes, links, values

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = ZoneCIDR.AU_SYD_1
         case 'au-syd-2': cidr = ZoneCIDR.AU_SYD_2
         case 'au-syd-3': cidr = ZoneCIDR.AU_SYD_3

         case 'br-sao-1': cidr = ZoneCIDR.BR_SAO_1
         case 'br-sao-2': cidr = ZoneCIDR.BR_SAO_2
         case 'br-sao-3': cidr = ZoneCIDR.BR_SAO_3

         case 'ca-tor-1': cidr = ZoneCIDR.CA_TOR_1
         case 'ca-tor-2': cidr = ZoneCIDR.CA_TOR_2
         case 'ca-tor-3': cidr = ZoneCIDR.CA_TOR_3

         case 'eu-de-1': cidr = ZoneCIDR.EU_DE_1
         case 'eu-de-2': cidr = ZoneCIDR.EU_DE_2
         case 'eu-de-3': cidr = ZoneCIDR.EU_DE_3

         case 'eu-gb-1': cidr = ZoneCIDR.EU_GB_1
         case 'eu-gb-2': cidr = ZoneCIDR.EU_GB_2
         case 'eu-gb-3': cidr = ZoneCIDR.EU_GB_3

         case 'jp-osa-1': cidr = ZoneCIDR.JP_OSA_1
         case 'jp-osa-2': cidr = ZoneCIDR.JP_OSA_2
         case 'jp-osa-3': cidr = ZoneCIDR.JP_OSA_3

         case 'jp-tok-1': cidr = ZoneCIDR.JP_TOK_1
         case 'jp-tok-2': cidr = ZoneCIDR.JP_TOK_2
         case 'jp-tok-3': cidr = ZoneCIDR.JP_TOK_3

         case 'us-east-1': cidr = ZoneCIDR.US_EAST_1
         case 'us-east-2': cidr = ZoneCIDR.US_EAST_2
         case 'us-east-3': cidr = ZoneCIDR.US_EAST_3

         case 'us-south-1': cidr = ZoneCIDR.US_SOUTH_1
         case 'us-south-2': cidr = ZoneCIDR.US_SOUTH_2
         case 'us-south-3': cidr = ZoneCIDR.US_SOUTH_3

         case _: cidr = ZoneCIDR.NONE

      return cidr.value
