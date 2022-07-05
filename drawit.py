# @file drawit.py
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

import sys
import argparse
import configparser

#SAVE import tkinter
#SAVE from tkinter import filedialog
#SAVE from tkinter import IntVar
#SAVE from tkinter import messagebox

from build.diagrams import Diagrams
from common.utils import *

class Config:
    def __init__(self, appName):
        
        # platform specific...
        if self.isWindows():
            self.filename = appName + ".ini"
        else:
            self.filename =  os.path.expanduser('~') + '/Library/Application Support/' + appName + ".ini"
        
        self.config = configparser.ConfigParser()
        if os.path.exists(self.filename):
            self.config.read(self.filename)
        if not self.config.has_section("parameters"):
            self.config.add_section("parameters")

        # platform specific...
        if not self.has("inputFile"):
            if self.isWindows():
                self.setInputFile("./" + appName)
            else:
                self.setInputFile(os.path.expanduser('~') + '/' + appName)

        # platform specific...
        if not self.has("outputDirectory"):
            if self.isWindows():
                self.setOutputDirectory("./" + appName)
            else:
                self.setOutputDirectory(os.path.join(os.path.expanduser('~'), 'Documents', TOOLNAME))

    def isWindows(self):
        return hasattr(sys, 'getwindowsversion')

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

    def getOutputDirectory(self):
        return self.get("outputDirectory")
    
    def setOutputDirectory(self,outputDirectory):
        self.set("outputDirectory",outputDirectory)

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

class drawit():
   def __init(self):
      self.diagrams = None

   top = None
   statusText = None
   #SAVE top = tkinter.Tk()
   #top.title(TOOLNAME + ' ' + COPYRIGHT.split(' ')[2])
   #SAVE title = COPYRIGHT.split(' - ')
   #SAVE top.title(title[0])
   #SAVE statusText = tkinter.StringVar()

   printmessage(COPYRIGHT)
   #printmessage(toolheader)

   def main(self): 

        config = Config("drawIT")  
        self.apiKey = config.getAPIKey()
        self.accountID = config.getAccountID()
        self.inputFile = config.getInputFile()
        self.outputDirectory = config.getOutputDirectory()
      
        parser = argparse.ArgumentParser(description='Draw IT')

        parser.add_argument('-key', dest='apikey',  default=userdata['apikey'], help='API Key')
        parser.add_argument('-account', dest='accountid',  default=userdata['accountid'], help='Account ID')
        parser.add_argument('-input', dest='inputfile',  default=userdata['inputfile'], help='JSON or YAML file')
        parser.add_argument('-region', dest='region', default=userdata['region'], help='au-syd, br-sao, ca-tor, eu-de, eu-gb, jp-osa, jp-tok, us-east, us-south')
        parser.add_argument('-output', dest='outputfolder', default=os.path.join(self.outputDirectory, userdata['outputfolder']), help='output directory')
        #parser.add_argument('-type', dest='outputtype', default=userdata['outputtype'], help='drawio or puml type')
        #parser.add_argument('-layout', dest='outputlayout', default=userdata['outputlayout'], help='layout method')
        parser.add_argument('-detail', dest='outputdetail', default=userdata['outputdetail'], help='low, medium, or high')
        parser.add_argument('-split', dest='outputsplit', default=userdata['outputsplit'], help='none, region, or vpc')
        parser.add_argument('-shapes', dest='outputshapes', default=userdata['outputshapes'], help='logical or prescribed')

        #parser.add_argument('-nogui', dest='nogui', action='store_true', default=userdata['nogui'], help="No gui (batch mode)")
        parser.add_argument('-mode', dest='runmode', default=userdata['runmode'], help="batch, gui, or web")
        parser.add_argument('--version', action='version', version='drawIT ' + COPYRIGHT.split(' ')[1])
        
        args = parser.parse_args()

        apikey = args.apikey.replace(' ', '')
        accountid = args.accountid.replace(' ', '')
        region = args.region.replace(' ', '')
        inputfile = args.inputfile.replace(' ', '')
        outputfolder = args.outputfolder.replace(' ', '')
        outputtype = "xml"
        #outputtype = args.outputtype.replace(' ', '').lower()
        #outputlayout = args.outputlayout.replace(' ', '').lower()
        outputdetail = args.outputdetail.replace(' ', '').lower()
        outputsplit = args.outputsplit.replace(' ', '').lower()
        outputshapes = args.outputshapes.replace(' ', '').lower()
        runmode = args.runmode.replace(' ', '').lower()

        userdata['apikey'] = apikey
        userdata['accountid'] = accountid
        userdata['region'] = region
        userdata['inputfile'] = inputfile
        userdata['outputfolder'] = outputfolder
        userdata['outputtype'] = outputtype
        #userdata['outputlayout'] = outputlayout
        userdata['outputdetail'] = outputdetail
        userdata['outputsplit'] = outputsplit
        userdata['outputshapes'] = outputshapes
        userdata['runmode'] = runmode

        self.minInfo = False

        done = False

        if args.runmode == 'batch':
            #try: 
                #printmessage(COPYRIGHT)
                #print(toolheader)

                # Check for existing input file and exit if not valid.
                #if not os.path.isfile(self.inputFile):
                #    print(invalidinputfilemessage % inputfile)
                #    return

                apiKey = userdata['apikey']
                accountID = userdata['accountid']
                region = userdata['region']
                inputfile = userdata['inputfile']

                #backupdirectory(userdata)

                if len(apiKey) > 0:
                    userdata['inputtype'] = 'rias'
                    inputbase = apikey
                    outputfile = inputbase + '.' + outputtype
                    userdata['outputfile'] = outputfile
                    if len(accountID) > 0:
                        printmessage(starttoolmessage % ('RIAS for API Key ' + apikey + ' and Account ID ' + accountid + ' in region ' + region))
                    else:
                        printmessage(starttoolmessage % 'RIAS for API Key ' + apikey + ' in region ' + region)
                elif len(inputfile) > 0:
                    basename = os.path.basename(inputfile)
                    inputbase = os.path.splitext(basename)[0]
                    inputtype = os.path.splitext(basename)[1][1:]
                    if inputtype == 'yaml' or inputtype == 'yml':
                        userdata['inputtype'] = 'yaml'
                    elif inputtype == 'json':
                        userdata['inputtype'] = 'json'
                    else:
                        printerror(invalidinputfilemessage % args.inputfile)
                        return
                    outputfile = inputbase + '.' + outputtype
                    userdata['outputfile'] = outputfile
                    printmessage(starttoolmessage % inputfile)
                else:
                    printerror(invalidmodemessage % args.runmode)
                    return

                self.diagrams = Diagrams(userdata)
                self.diagrams.buildDiagrams()

                #self.diagrams = Diagrams(userdata)
                #inputdata = load(userdata)
                #if inputdata != None:
                #    userdata['inputdata'] = inputdata

                #    setupdata = loadAnalyze(userdata)
                #    userdata['setupdata'] = setupdata

                #    self.diagrams.buildDiagrams()

                printmessage(donetoolmessage % outputfolder)

                done = True

        elif args.runmode == 'gui':
            import tkinter
            from tkinter import filedialog
            from tkinter import IntVar
            from tkinter import messagebox
        
            top = tkinter.Tk()
            title = COPYRIGHT.split(' - ')
            top.title(title[0])
            statusText = tkinter.StringVar()

            frame = tkinter.Frame(self.top)
            frame.pack(fill=tkinter.X, side=tkinter.TOP)
            frame.grid_columnconfigure(1, weight=1)            
            row = 1
            
            genbutton = tkinter.Frame(frame)
            eGenerate = tkinter.Button(genbutton, text="Generate", state='normal', fg="blue", command=lambda: onClickGenerate())
            genbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eGenerate.pack(side=tkinter.LEFT)
            row = row + 1
            
            tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            tkinter.Label(frame, text="API Key").grid(row=row)
            lAPIKey = tkinter.Entry(frame, bd=5)
            lAPIKey.insert(0, apikey)
            lAPIKey.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            config.set("apiKey",apikey)
            config.write()
            row = row + 1

            tkinter.Label(frame, text="Account ID").grid(row=row)
            lAccountID = tkinter.Entry(frame, bd=5)
            lAccountID.insert(0, accountid)
            lAccountID.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            config.set("accountID", accountid)
            config.write()
            row = row + 1

            tkinter.Label(frame, text="- or -").grid(row=row, columnspan=2)
            row = row + 1

            #tkinter.Label(frame, text="Yaml").grid(row=row)
            #lInputFile = tkinter.Label(frame, text=inputfile)
            tkinter.Label(frame, text="YAML File").grid(row=row)
            lInputFile = tkinter.Entry(frame, bd=5)
            lInputFile.insert(0, inputfile)
            lInputFile.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            row = row + 1

            if len(apikey) > 0:
                lInputFile.delete(0, 'end')
                self.inputFile = ''
                config.set("inputFile", self.inputFile)
                config.write()

            def onClickSelectInputFile():
                file_selected = filedialog.askopenfilename(initialdir = self.inputFile,title = "Select YAML")
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
                    
            inputbutton = tkinter.Frame(frame)
            eSelectInputFile = tkinter.Button(inputbutton, text="Select YAML", fg="blue", command=lambda: onClickSelectInputFile())
            inputbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eSelectInputFile.pack(side=tkinter.RIGHT)
            row = row + 1

            #inputfile = userdata['inputfile']
            #basename = os.path.basename(inputfile)
            #inputbase = os.path.splitext(basename)[0]
            #inputtype = os.path.splitext(basename)[1][1:]
            #outputfile = inputbase + '.' + outputtype
            #userdata['outputfile'] = outputfile

            tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            #tkinter.Label(frame, text="Output").grid(row=row)
            #lOutputDirectory = tkinter.Label(frame, text=outputfolder)
            tkinter.Label(frame, text="Directory").grid(row=row)
            lOutputDirectory = tkinter.Entry(frame, bd=5)
            lOutputDirectory.insert(0, outputfolder)
            #lOutputDirectory.grid(row=row,column=1)
            lOutputDirectory.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
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
                    userdata['outputfolder'] = self.outputDirectory
                    
            outputbutton = tkinter.Frame(frame)
            eSelectOutputDirectory = tkinter.Button(outputbutton, text="Select Directory", fg="blue", command=lambda: onClickSelectOutputDirectory())
            outputbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eSelectOutputDirectory.pack(side=tkinter.RIGHT)
            row = row + 2

            tkinter.Label(frame, text="").grid(row=row, columnspan=2)
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
                "Germany",
                "Osaka",
                "Sao Paulo",
                "Sydney",
                "Tokyo",
                "Toronto",
                "United Kingdom",
                "US East",
                "US South"]
            eRegion = tkinter.StringVar(self.top)
            eRegion.set("US South")
            tkinter.Label(frame, text="Region").grid(row=row)
            #regionmenu = tkinter.OptionMenu(self.top, eRegion, *regionoptions).grid(row=row)
            regionmenu = tkinter.OptionMenu(frame, eRegion, *regionoptions).grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            #regionmenu.pack()
            row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            detailoptions = [
                "Low", 
                "Medium",
                "High"]
            eOutputDetail = tkinter.StringVar(self.top)
            eOutputDetail.set("Medium")
            tkinter.Label(frame, text="Detail Level").grid(row=row)
            shapemenu = tkinter.OptionMenu(frame, eOutputDetail, *detailoptions).grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            row = row + 1

            shapeoptions = [
                "Logical", 
                "Prescribed"]
            eOutputShape = tkinter.StringVar(self.top)
            eOutputShape.set("Prescribed")
            tkinter.Label(frame, text="Diagram Type").grid(row=row)
            #shapemenu = tkinter.OptionMenu(self.top, eOutputShape, *shapeoptions)
            shapemenu = tkinter.OptionMenu(frame, eOutputShape, *shapeoptions).grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            #shapemenu.pack()
            row = row + 1

            splitoptions = [
                "Single", 
                "Region", 
                "VPC"]
            eOutputSplit = tkinter.StringVar(self.top)
            eOutputSplit.set("VPC")
            tkinter.Label(frame, text="File Organization").grid(row=row)
            #splitmenu = tkinter.OptionMenu(self.top, eOutputSplit, *splitoptions)
            splitmenu = tkinter.OptionMenu(frame, eOutputSplit, *splitoptions).grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            #splitmenu.pack()
            row = row + 1

            def onClickGenerate():
                try:
                    #self.statusText.set("       Generating IBM2 for " + str(self.inputFile) + "...")
                    self.statusText.set("Starting")
                    frame.after_idle(onClickGenerate)                   

                    #outputtype = str(eOutputType.get())
                    #if outputtype == "Generate Drawio": 
                    #    outputtype = "drawio"
                    #elif outputtype == "Generate PlantUML":
                    #    outputtype = "puml"
                    #userdata['outputtype'] = outputtype

                    outputdetail = str(eOutputDetail.get())
                    if outputdetail == "Low":
                        outputdetail = "low"
                    elif outputdetail == "Medium":
                        outputdetail = "medium"
                    elif outputdetail == "High":
                        outputdetail = "high"
                    userdata['outputdetail'] = outputdetail

                    outputshapes = str(eOutputShape.get())
                    if outputshapes == "Logical":
                        outputshapes = "logical"
                    elif outputshapes == "Prescribed":
                        outputshapes = "prescribed"
                    userdata['outputshapes'] = outputshapes

                    outputsplit = str(eOutputSplit.get())
                    if outputsplit == "None":
                        outputsplit = "none"
                    elif outputsplit == "Region":
                        outputsplit = "region"
                    elif outputsplit == "VPC":
                        outputsplit = "vpc"
                    userdata['outputsplit'] = outputsplit

                    region = str(eRegion.get())
                    if region == "Germany":
                        region = "eu-de"
                    elif region == "Osaka":
                        region = "jp-osa"
                    elif region == "Sao Paulo":
                        region = "br-sao"
                    elif region == "Sydney":
                        region = "au-syd"
                    elif region == "Tokyo":
                        region = "jp-tok"
                    elif region == "Toronto":
                        region = "ca-tor"
                    elif region == "United Kingdom":
                        region = "eu-gb"
                    elif region == "US East":
                        region = "us-east"
                    elif region == "US South":
                        region = "us-south"
                    userdata['region'] = region

                    accountid = str(lAccountID.get())
                    userdata['accountid'] = accountid

                    #apikey = self.apiKey
                    apikey = str(lAPIKey.get())
                    userdata['apikey'] = apikey 

                    #inputfile = self.inputFile
                    inputfile = str(lInputFile.get())
                    userdata['inputfile'] = inputfile

                    #outputfolder = self.outputDirectory
                    outputfolder = str(lOutputDirectory.get())
                    userdata['outputfolder'] = outputfolder

                    self.statusText.set("Starting")
                    #print(starttoolmessage % self.inputFile)

                    if len(apikey) > 0:
                        userdata['inputtype'] = 'rias'
                        inputbase = apikey
                        outputfile = str(inputbase) + '.' + outputtype
                        userdata['outputfile'] = outputfile
                        if len(accountid) > 0:
                            printmessage(starttoolmessage % ('RIAS for API Key ' + apikey + ' and Account ID ' + accountid + ' in region ' + region))
                        else:
                            printmessage(starttoolmessage % 'RIAS for API Key ' + apikey + ' in region ' + region)
                    elif len(inputfile) > 0:
                        basename = os.path.basename(self.inputFile)
                        inputbase = os.path.splitext(basename)[0]
                        inputtype = os.path.splitext(basename)[1][1:]
                        if inputtype == 'yaml' or inputtype == 'yml':
                            userdata['inputtype'] = 'yaml'
                        elif inputtype == 'json':
                            userdata['inputtype'] = 'json'
                        else:
                           printerror(invalidinputfilemessage % args.inputfile)
                           return
                        outputfile = inputbase + '.' + outputtype
                        userdata['outputfile'] = outputfile
                        printmessage(starttoolmessage % inputtype + ' File: ' + inputfile)
                    else:
                        printerror(invalidmodemessage % args.runmode)
                        sys.exit()

                    self.diagrams = Diagrams(userdata)
                    self.diagrams.buildDiagrams()

                    #self.diagrams = Diagrams(userdata)
                    #inputdata = load(userdata)
                    #if inputdata != None:
                    #    userdata['inputdata'] = inputdata

                    #    setupdata = loadAnalyze(userdata)
                    #    userdata['setupdata'] = setupdata

                    #    self.diagrams.buildDiagrams()

                    printmessage(donetoolmessage % self.outputDirectory)
                    self.statusText.set("Completed")

                    sys.exit()

                except Exception as error:
                    self.statusText.set("Generate failed")
                    messagebox.showinfo("Generate failed", str(error))
                    #traceback.print_exc()
                    #traceback.print_last()

            eGenerate.pack(side=tkinter.RIGHT)

            #SAVE self.statusText.set("Ready")    
            statusText.set("Ready")    
    
            statusLabel = tkinter.Label(self.top, textvariable=self.statusText)
            statusLabel.pack(side=tkinter.RIGHT)
    
            #SAVE self.top.mainloop()
            top.mainloop()

        elif args.runmode == 'web':
            userdata['inputtype'] = 'web'
            basename = os.path.basename(inputfile)
            inputbase = os.path.splitext(basename)[0]
            inputtype = os.path.splitext(basename)[1][1:]
            outputfile = inputbase + '.' + outputtype
            userdata['outputfile'] = outputfile

            self.diagrams = Diagrams(userdata)
            self.diagrams.buildDiagrams()

            #self.diagrams = Diagrams(userdata)
            #inputdata = load(userdata)
            #if inputdata != None:
            #    userdata['inputdata'] = inputdata

            #   setupdata = loadAnalyze(userdata)
            #    userdata['setupdata'] = setupdata

            #    self.diagrams.buildDiagrams()

            #    #print("XML begin")
            #    #print('<mxfile type="device" compressed="false"></mxfile>');
            #    #print("XML end")
            
        else:
            printerror(invalidmodemessage % args.runmode)

#main()

if __name__ == "__main__":
   main = drawit()
   main.main()
