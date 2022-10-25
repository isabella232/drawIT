# @file drawit.py
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

from argparse import ArgumentParser
from configparser import ConfigParser
from os import path
from platform import system as platform_system
from sys import exit as sys_exit

from common.common import Common
from diagram.diagram import Diagram
from load.load import Load

class Config:
    def __init__(self, appName):
        
        # platform specific...
        if self.isWindows():
            self.filename = appName + ".ini"
        else:
            self.filename =  path.expanduser('~') + '/Library/Application Support/' + appName + ".ini"
        
        self.config = ConfigParser()
        if path.exists(self.filename):
            self.config.read(self.filename)
        if not self.config.has_section("parameters"):
            self.config.add_section("parameters")

        # platform specific...
        if not self.has("inputFile"):
            if self.isWindows():
                self.setInputFile("./" + appName)
            else:
                self.setInputFile(path.expanduser('~') + '/' + appName)

        # platform specific...
        if not self.has("outputDirectory"):
            if self.isWindows():
                self.setOutputDirectory("./" + appName)
            else:
                self.setOutputDirectory(path.join(path.expanduser('~'), 'Documents', appName))

    def isWindows(self):
        #return hasattr(sys, 'getwindowsversion')
        return platform_system == 'Windows'

    def get(self,propertyName):
        if propertyName in self.config["parameters"]:
            return self.config["parameters"][propertyName]
        else:
            return None
    
    def set(self,propertyName,value):
        self.config.set("parameters",propertyName,value)
        
    def has(self,propertyName):
        return self.config.has_option("parameters",propertyName)

    def write(self):
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)
            
    def getAPIKey(self):
        return self.get("apiKey")
    
    def setAPIKey(self,apiKey):
        self.set("apiKey",apiKey)

    def getAccountID(self):
        return self.get("accountID")
    
    def setAccountID(self,apiKey):
        self.set("accountID",accountID)

    def getInputFile(self):
        return self.get("inputFile")
    
    def setInputFile(self,inputFile):
        self.set("inputFile",inputFile)

    def getOutputFile(self):
        return self.get("outputFile")
    
    def setOutputFile(self,outputFile):
        self.set("outputFile",outputFile)

    def getOutputDirectory(self):
        return self.get("outputDirectory")
    
    def setOutputDirectory(self,outputDirectory):
        self.set("outputDirectory",outputDirectory)

    def getOutputFolder(self):
        return self.get("outputFolder")
    
    def setOutputFolder(self,outputFolder):
        self.set("outputFolder",outputFolder)

    def getTablesFolder(self):
        return self.get("tablesFolder")
    
    def setTablesFolder(self,tablesFolder):
        self.set("tablesFolder",tablesFolder)

    def getOutputSplit(self):
        return self.get("outputSplit")
    
    def setOutputSplit(self,outputSplit):
        self.set("outputSplit",outputSplit)

    def getOutputShapes(self):
        return self.get("outputShapes")
    
    def setOutputShapes(self,outputShapes):
        self.set("outputShapes",outputShapes)

    def getOutputLayout(self):
        return self.get("outputLayout")
    
    def setOutputLayout(self,outputLayout):
        self.set("outputLayout",outputLayout)

    def getRegion(self):
        return self.get("region")
    
    def setRegion(self,region):
        self.set("region",region)

    def getShapes(self):
        return self.get("shapes")
    
    def setShapes(self,shapes):
        self.set("shapes",shapes)

    def getSplit(self):
        return self.get("split")
    
    def setSplit(self,region):
        self.set("split",split)

    def getRunMode(self):
        return self.get("runmode")
    
    def setRunMode(self,runmode):
        self.set("runmode",runmode)

    def getCloudType(self):
        return self.get("cloudtype")
    
    def setCloudType(self,cloudtype):
        self.set("cloudtype",cloudtype)

class drawit:
   title = None
   top = None
   statusText = None
   data = None
   diagram = None 
   common = None
   generate = None

   def __init__(self):
      self.common = Common()
      self.title = self.common.getToolTitle()

   #SAVE top = tkinter.Tk()
   #top.title(TOOLNAME + ' ' + COPYRIGHT.split(' ')[2])
   #SAVE title = COPYRIGHT.split(' - ')
   #SAVE top.title(title[0])
   #SAVE statusText = tkinter.StringVar()

   #printmessage(self.common.getToolCopyright())
   #printmessage(toolheader)

   def main(self): 

        config = Config("drawIT")  
        apikey = config.getAPIKey()
        accountid = config.getAccountID()
        inputfile = config.getInputFile()
        outputfile = config.getOutputFile()
        outputfolder = config.getOutputFolder()
        outputdirectory = config.getOutputDirectory()
        tablesfolder = config.getTablesFolder()
        outputsplit = config.getOutputSplit()
        outputshapes = config.getOutputShapes()
        outputlayout = config.getOutputLayout()
        runmode = config.getRunMode()
        cloudtype = config.getCloudType()
        region = config.getRegion()
      
        parser = ArgumentParser(description='drawIT')

        parser.add_argument('-key', dest='apikey', default=self.common.getAPIKey(), help='API Key')
        parser.add_argument('-account', dest='accountid', default=self.common.getAccountID(), help='Account ID')
        parser.add_argument('-input', dest='inputfile', default=self.common.getInputFile(), help='JSON/YAML')
        parser.add_argument('-region', dest='region', default=self.common.getRegion().value, help='all, au-syd, br-sao, ca-tor, eu-de, eu-gb, jp-osa, jp-tok, us-east, us-south')
        parser.add_argument('-output', dest='outputfolder', default=path.join(outputdirectory, self.common.getOutputFolder()), help='output directory')
        parser.add_argument('-split', dest='outputsplit', default=self.common.getOutputSplit().value, help='single, combine, region, vpc, or vpc:vpcid')
        parser.add_argument('-shapes', dest='outputshapes', default=self.common.getOutputShapes().value, help='logical or prescribed')
        parser.add_argument('-layout', dest='outputlayout', default=self.common.getOutputLayout().value, help='horizontal, vertical, horizontalnolink, verticalnolink')
        parser.add_argument('-tables', dest='tablesfolder', default=self.common.getTablesFolder(), help='tables directory')

        parser.add_argument('-mode', dest='runmode', default=self.common.getRunMode().value, help="batch, gui, web, or terraform")
        parser.add_argument('-cloud', dest='cloudtype', default=self.common.getCloudType().value, help="ibm")
        parser.add_argument('--version', action='version', version='drawIT ' + self.common.getToolTitle().split(' ')[1])
        
        args = parser.parse_args()

        #apikey = args.apikey.replace(' ', '')
        #accountid = args.accountid.replace(' ', '')
        #region = args.region.replace(' ', '')
        #inputfile = args.inputfile.replace(' ', '')
        #outputfolder = args.outputfolder.replace(' ', '')
        #outputtype = "xml"
        #outputdetail = args.outputdetail.replace(' ', '').lower()
        #outputsplit = args.outputsplit.replace(' ', '').lower()
        #outputshapes = args.outputshapes.replace(' ', '').lower()
        #runmode = args.runmode.replace(' ', '').lower()

        apikey = args.apikey
        accountid = args.accountid
        region = args.region.lower()
        inputfile = args.inputfile
        outputfolder = args.outputfolder
        tablesfolder = args.tablesfolder
        outputtype = "xml"
        outputsplit = args.outputsplit.lower()
        outputshapes = args.outputshapes.lower()
        outputlayout = args.outputlayout.lower()
        runmode = args.runmode.lower()
        cloudtype = args.cloudtype.lower()

        self.common.setAPIKey(apikey)
        self.common.setAccountID(accountid)
        self.common.setRegion(region)
        self.common.setInputFile(inputfile)
        self.common.setOutputFolder(outputfolder)
        self.common.setCloudType(cloudtype)

        if cloudtype != 'ibm':
           self.common.printInvalidCloud(cloudtype)
           return

        if outputshapes == "logical":
            self.common.setLogicalShapes()
        else: # outputshapes == "prescribed"
            self.common.setPrescribedShapes()

        if outputlayout == "horizontal":
            self.common.setHorizontalLayout()
        elif outputlayout == "horizontalnolink":
            self.common.setHorizontalNoLinkLayout()
        elif outputlayout == "verticalnolink":
            self.common.setVerticalNoLinkLayout()
        else: # outputlayout == "vertical"
            self.common.setVerticalLayout()

        if outputsplit == "single":
            self.common.setSingleSplit()
        elif outputsplit == "combine":
            self.common.setCombineSplit()
        elif outputsplit == "region":
            self.common.setRegionSplit()
        else: # outputsplit == "vpc" or "vpc:vpcname"
            outputvpc = outputsplit.split(':')
            if outputvpc[0] == 'vpc' and len(outputvpc) > 1:
                self.common.setDesignatedVPC(outputvpc[1])
            self.common.setVPCSplit()

        if region == "eu-de":
            self.common.setGermanyRegion()
        elif region == "jp-osa":
            self.common.setOsakaRegion()
        elif region == "br-sao":
            self.common.setSaoPauloRegion()
        elif region == "au-syd":
            self.common.setSydneyRegion()
        elif region == "jp-tok":
            self.common.setTokyoRegion()
        elif region == "ca-tor":
            self.common.setTorontoRegion()
        elif region == "eu-gb":
            self.common.setUnitedKingdomRegion()
        elif region == "us-east":
            self.common.setUSEastRegion()
        elif region == "us-south":
            self.common.setUSSouthRegion()
        else:
            self.common.setAllRegion()

        self.minInfo = False

        done = False

        if self.common.isBatchMode(args.runmode):
            #try: 
                #printmessage(COPYRIGHT)
                #print(toolheader)

                # Check for existing input file and exit if not valid.
                #if not path.isfile(self.inputFile):
                #    print(invalidinputfilemessage % inputfile)
                #    return

                apikey = self.common.getAPIKey()
                accountid = self.common.getAccountID()
                region = self.common.getRegion().value
                inputfile = self.common.getInputFile()
                outputtype = 'xml'

                #backupdirectory(options)

                if len(apikey) > 0:
                    self.common.setInputRIAS()
                    inputbase = apikey
                    outputfile = inputbase + '.' + outputtype
                    self.common.setOutputFile(outputfile)
                    if len(accountid) > 0:
                        self.common.printStartRIASwithAccount(apikey, accountid, region)
                    else:
                        self.common.printStartRIASwithKey(apikey, region)
                elif len(inputfile) > 0:
                    basename = path.basename(inputfile)
                    inputbase = path.splitext(basename)[0]
                    inputtype = path.splitext(basename)[1][1:]
                    if inputtype == 'yaml' or inputtype == 'yml':
                        self.common.setInputYAML()
                    elif inputtype == 'json':
                        self.common.setInputJSON()
                    else:
                        self.common.printInvalidFile(args.inputfile)
                        return
                    outputfile = inputbase + '.' + outputtype
                    self.common.setOutputFile(outputfile)
                    self.common.printStartFile(inputfile, self.common.getCloudType().upper())
                else:
                    self.common.printInvalidInput()
                    return

                self.data = Load(self.common)
                if self.data.loadData():
                    self.diagram = Diagram(self.common, self.data)
                    self.diagram.buildDiagrams()
                    self.common.printDone(outputfolder)
                else:
                    self.common.printExit()

                done = True

        elif self.common.isGUIMode(args.runmode):
            from tkinter import Button, Entry, filedialog, Frame, IntVar, Label, messagebox, OptionMenu, StringVar, Tk, LEFT, RIGHT, TOP, E, W, X
        
            self.top = Tk()
            self.title = self.common.getToolTitle()
            self.top.title(self.title)
            self.statusText = StringVar()

            frame = Frame(self.top)
            frame.pack(fill=X, side=TOP)
            frame.grid_columnconfigure(1, weight=1)            
            row = 1
            
            genbutton = Frame(frame)
            eGenerate = Button(genbutton, text="Generate", state='normal', fg="blue", command=lambda: onClickGenerate())
            genbutton.grid(row=row, columnspan=2, sticky=E)
            eGenerate.pack(side=LEFT)
            row = row + 1
            
            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            Label(frame, text="API Key").grid(row=row)
            lAPIKey = Entry(frame, bd=5)
            lAPIKey.insert(0, apikey)
            lAPIKey.grid(row=row, column=1, sticky=W + E)
            config.set("apiKey",apikey)
            config.write()
            row = row + 1

            Label(frame, text="Account ID").grid(row=row)
            lAccountID = Entry(frame, bd=5)
            lAccountID.insert(0, accountid)
            lAccountID.grid(row=row, column=1, sticky=W + E)
            config.set("accountID", accountid)
            config.write()
            row = row + 1

            Label(frame, text="- or -").grid(row=row, columnspan=2)
            row = row + 1

            #tkinter.Label(frame, text="Yaml").grid(row=row)
            #lInputFile = tkinter.Label(frame, text=inputfile)
            Label(frame, text="JSON/YAML").grid(row=row)
            lInputFile = Entry(frame, bd=5)
            lInputFile.insert(0, inputfile)
            lInputFile.grid(row=row, column=1, sticky=W + E)
            row = row + 1

            if len(apikey) > 0:
                lInputFile.delete(0, 'end')
                self.inputFile = ''
                config.set("inputFile", inputfile)
                config.write()

            def onClickSelectInputFile():
                file_selected = filedialog.askopenfilename(initialdir = inputfile,title = "Select JSON/YAML")
                if file_selected != None and len(file_selected) > 0:
                    self.inputFile = file_selected
                    lAPIKey.delete(0, 'end')
                    lInputFile.delete(0, 'end')
                    lInputFile.insert(0, self.inputFile)
                    lInputFile.configure(text=self.inputFile)
                    lAPIKey.delete(0, 'end')
                    self.apiKey = ''
                    config.set("apiKey", self.apiKey)
                    config.write()
                    config.set("inputFile", self.inputFile)
                    config.write()
                    
            inputbutton = Frame(frame)
            eSelectInputFile = Button(inputbutton, text="Select JSON/YAML", fg="blue", command=lambda: onClickSelectInputFile())
            inputbutton.grid(row=row, columnspan=2, sticky=E)
            eSelectInputFile.pack(side=RIGHT)
            row = row + 1

            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            Label(frame, text="Directory").grid(row=row)
            lOutputDirectory = Entry(frame, bd=5)
            lOutputDirectory.insert(0, outputfolder)
            lOutputDirectory.grid(row=row, column=1, sticky=W + E)
            row = row + 1

            def onClickSelectOutputDirectory():
                folder_selected = filedialog.askdirectory(initialdir = self.outputDirectory,title = "Select Directory")
                if folder_selected != None and len(folder_selected) > 0:
                    self.outputDirectory = folder_selected
                    lOutputDirectory.delete(0, 'end')
                    lOutputDirectory.insert(0, self.outputDirectory)
                    lOutputDirectory.configure(text=self.outputDirectory)
                    config.set("outputDirectory",self.outputDirectory)
                    config.write()
                    self.common.setOutputFolder(self.outputDirectory)
                    
            outputbutton = Frame(frame)
            eSelectOutputDirectory = Button(outputbutton, text="Select Directory", fg="blue", command=lambda: onClickSelectOutputDirectory())
            outputbutton.grid(row=row, columnspan=2, sticky=E)
            eSelectOutputDirectory.pack(side=RIGHT)
            row = row + 2

            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            #layoutoptions = [
            #    "Circular Layout", 
            #    "Distributed Recursive Layout", 
            #    "Fruchtermain-Reingold Layout",
            #    "Fruchtermain-Reingold 3D Layout",
            #    "Fruchtermain-Reingold Grid Layout",
            #    "Kamada-Kawai Layout",
            #    "Kamada-Kawai 3D Layout",
            #    "Large Graph Layout",
            #    "Random Layout",
            #    "Random 3D Layout",
            #    "Reingold-Tilford Tree Layout",
            #    "Reingold-Tilford Tree Polar Layout",
            #    "Spherical Layout"]
            #eOutputLayout = tkinter.StringVar(self.top)
            #eOutputLayout.set("Reingold-Tilford Tree Layout")
            #layoutmenu = tkinter.OptionMenu(self.top, eOutputLayout, *layoutoptions)
            #layoutmenu.pack()

            #typeoptions = [
            #    "Generate Drawio", 
            #    "Generate PlantUML"]
            #eOutputType = tkinter.StringVar(self.top)
            #eOutputType.set("Generate Drawio")
            #typemenu = tkinter.OptionMenu(self.top, eOutputType, *typeoptions)
            #typemenu.pack()

            regionoptions = [
                "All",
                "Germany",
                "Osaka",
                "Sao Paulo",
                "Sydney",
                "Tokyo",
                "Toronto",
                "United Kingdom",
                "US East",
                "US South"]
            eRegion = StringVar(self.top)
            eRegion.set("All")
            Label(frame, text="Region").grid(row=row)
            #regionmenu = tkinter.OptionMenu(self.top, eRegion, *regionoptions).grid(row=row)
            regionmenu = OptionMenu(frame, eRegion, *regionoptions).grid(row=row, column=1, sticky=W + E)
            #regionmenu.pack()
            row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            shapeoptions = [
                "Logical", 
                "Prescribed"]
            eOutputShape = StringVar(self.top)
            eOutputShape.set("Prescribed")
            Label(frame, text="Diagram Type").grid(row=row)
            #shapemenu = tkinter.OptionMenu(self.top, eOutputShape, *shapeoptions)
            shapemenu = OptionMenu(frame, eOutputShape, *shapeoptions).grid(row=row, column=1, sticky=W + E)
            #shapemenu.pack()
            row = row + 1

            shapelayout = [
                "Horizontal", 
                "Vertical",
                "Horizontal No Links", 
                "Vertical No Links"]
            eOutputLayout = StringVar(self.top)
            eOutputLayout.set("Vertical")
            Label(frame, text="Diagram Layout").grid(row=row)
            shapemenu = OptionMenu(frame, eOutputLayout, *shapelayout).grid(row=row, column=1, sticky=W + E)
            row = row + 1

            splitoptions = [
                "Single", 
                "Combine", 
                "Region", 
                "VPC"]
            eOutputSplit = StringVar(self.top)
            eOutputSplit.set("Single")
            Label(frame, text="File Organization").grid(row=row)
            #splitmenu = tkinter.OptionMenu(self.top, eOutputSplit, *splitoptions)
            splitmenu = OptionMenu(frame, eOutputSplit, *splitoptions).grid(row=row, column=1, sticky=W + E)
            #splitmenu.pack()
            row = row + 1

            def onClickGenerate():
                try:
                    self.statusText.set("Starting")
                    frame.after_idle(onClickGenerate)                   

                    outputshapes = str(eOutputShape.get()).lower()
                    if outputshapes == "logical":
                       self.common.setLogicalShapes()
                    else: # outputshapes == "prescribed"
                       self.common.setPrescribedShapes()

                    outputlayout = str(eOutputLayout.get()).lower()
                    if outputlayout == "horizontal":
                       self.common.setHorizontalLayout()
                    elif outputlayout == "horizontalnolink":
                       self.common.setHorizontalNoLinkLayout()
                    elif outputlayout == "verticalnolink":
                       self.common.setVerticalNoLinkLayout()
                    else: # outputlayout == "vertical"
                       self.common.setVerticalLayout()

                    outputsplit = str(eOutputSplit.get()).lower()
                    if outputsplit == "single":
                       self.common.setSingleSplit()
                    elif outputsplit == "combine":
                       self.common.setCombineSplit()
                    elif outputsplit == "region":
                       self.common.setRegionSplit()
                    else: # outputsplit == "VPC"
                       self.common.setVPCSplit()

                    region = str(eRegion.get()).lower()
                    if region == "eu-de":
                       self.common.setGermanyRegion()
                    elif region == "jp-osa":
                       self.common.setOsakaRegion()
                    elif region == "br-sao":
                       self.common.setSaoPauloRegion()
                    elif region == "au-syd":
                       self.common.setSydneyRegion()
                    elif region == "jp-tok":
                       self.common.setTokyoRegion()
                    elif region == "ca-tor":
                       self.common.setTorontoRegion()
                    elif region == "eu-gb":
                       self.common.setUnitedKingdomRegion()
                    elif region == "us-east":
                       self.common.setUSEastRegion()
                    elif region == "us-south":
                       self.common.setUSSouthRegion()
                    else:
                       self.common.setAllRegion()

                    accountid = str(lAccountID.get())
                    self.common.setAccountID(accountid)

                    apikey = str(lAPIKey.get())
                    self.common.setAPIKey(apikey)

                    #inputfile = self.inputFile
                    inputfile = str(lInputFile.get())
                    self.common.setInputFile(inputfile)

                    #outputfolder = self.outputDirectory
                    outputfolder = str(lOutputDirectory.get())
                    self.common.setOutputFolder(outputfolder)

                    outputtype = 'xml'

                    self.statusText.set("Starting")

                    if len(apikey) > 0:
                        self.common.setInputRIAS()
                        inputbase = apikey
                        outputfile = str(inputbase) + '.' + outputtype
                        self.common.setOutputFile(outputfile)
                        if len(accountid) > 0:
                           self.common.printStartRIASwithAccount(apikey, accountid, region)
                        else:
                           self.common.printStartRIASwithKey(apikey, region)
                    elif len(inputfile) > 0:
                        basename = path.basename(self.inputFile)
                        inputbase = path.splitext(basename)[0]
                        inputtype = path.splitext(basename)[1][1:]
                        if inputtype == 'yaml' or inputtype == 'yml':
                            self.common.setInputYAML()
                        elif inputtype == 'json':
                            self.common.setInputJSON()
                        else:
                           self.common.printInvalidFile(inputfile)
                           sys_exit()
                        outputfile = inputbase + '.' + outputtype
                        self.common.setOutputFile(outputfile)
                        self.common.printStartFile(inputfile, self.common.getCloudType().upper())
                    else:
                        self.common.printInvalidInput()
                        sys_exit()

                    self.data = Load(self.common)
                    if self.data.loadData():
                        self.diagram = Diagram(self.common, self.data)
                        self.diagram.buildDiagrams()
                        self.common.printDone(outputfolder)
                    else:
                        self.common.printExit()

                    self.statusText.set("Completed")

                    sys_exit()

                except Exception as error:
                    self.statusText.set("Generate failed")
                    messagebox.showinfo("Generate failed", str(error))
                    #traceback.print_exc()
                    #traceback.print_last()

            eGenerate.pack(side=RIGHT)

            #SAVE self.statusText.set("Ready")    
            self.statusText.set("Ready")    
    
            statusLabel = Label(self.top, textvariable=self.statusText)
            statusLabel.pack(side=RIGHT)
    
            #SAVE self.top.mainloop()
            self.top.mainloop()

        elif self.common.isWebMode(args.runmode):
            basename = path.basename(inputfile)
            inputbase = path.splitext(basename)[0]
            inputtype = path.splitext(basename)[1][1:]
            if inputtype == 'yaml' or inputtype == 'yml':
                self.common.setInputYAML()
            elif inputtype == 'json':
                self.common.setInputJSON()
            else:
                self.common.printInvalidFile(args.inputfile)
                return
            outputtype = 'xml'
            outputfile = inputbase + '.' + outputtype
            self.common.setOutputFile(outputfile)

            self.data = Load(self.common)
            if self.data.loadData():
                self.diagram = Diagram(self.common, self.data)
                self.diagram.buildDiagrams()

        elif self.common.isTerraformMode(args.runmode):
            from terraform.common.common import Common
            from terraform.generate.generate import Generate

            buildcommon = Common()

            outputfolder = self.common.getOutputFolder()
            buildcommon.setInputType('xlsx')
            buildcommon.setInputDirectory(tablesfolder)
            basename = path.basename(outputfolder)
            buildcommon.setOutputDirectory(path.join(outputfolder, basename + '.resources'))

            self.generate = Generate(buildcommon)
            self.generate.all()
   
        else:
            self.common.printInvalidMode(args.runmode)

#main()

if __name__ == "__main__":
   main = drawit()
   main.main()
