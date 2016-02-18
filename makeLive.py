#!/usr/bin/python
import subprocess
import shutil
import os

file-site = input("Enter the file path (start from year): ")
projectNumber = input("Enter the project number: ")
newProject = input("Is this a new project? (Type Y for yes): ")
finderWindow = input("Want to open a new Finder window? (Type y for yes): ")
def link-it(filePath):
    filePath = filePath.replace("\\", "/") #take care of windows weirdness
    print(filePath[0:8])
    #/Volumes/marketing$/Creative Services/2016/NBS/FACTS_K12_Sales_Mktg/6806_RenWeb_Upsell_To_FGAA_4/Design/Production/6806_RenWeb_Upsell_to_FGAA_4_0218.html
    if filePath[0:8] == '/Volumes':
        fullFile = filePath
        yearStart = filePath.find('2')
        emailServerCommon = filePath[yearStart:8] #year and main division i.e. NDS
    else: #emteet.io
        serverPath = "/Volumes/marketing$/Creative Services/"
        fullFile = serverPath + filePath #add weird server path
        emailServerCommon = filePath[:8] #year and main division i.e. NDS
    emailServerPath = "/Volumes/Communications/email/"

    innerFolders = [] #list of inner divisions like i.e. MBLE_EP
    for folder in os.listdir(emailServerPath + emailServerCommon):
        if os.path.isdir(emailServerPath + emailServerCommon + "/" + folder) == True:
            innerFolders.append(folder)
    fileInnerStart = filePath.find(projectNumber)
    fileInner = filePath[9:fileInnerStart - 1] #get inner division from file path
    fileTitleStart = filePath.rfind(projectNumber)
    fileTitle = filePath[fileTitleStart:] #get file name
    def new-one():
        newDir = emailServerPath + emailServerCommon + "/" + fileInner + "/" + projectNumber
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        shutil.copy(fullFile, newDir + "/")
        if finderWindow.lower() == 'y':
            subprocess.call(["open", "-R", newDir])
        print("http://www.nelnet.net/marketingprod/email/{0}/{1}/{2}/{3}".format(emailServerCommon, fileInner, projectNumber, fileTitle))
    if newProject.lower() == "y":
        new-one()
    else:
        for folder in innerFolders:
            if folder == fileInner:
                for smallFolder in os.listdir(emailServerPath + emailServerCommon + "/" + fileInner):
                    if os.path.isdir(emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder) == True and smallFolder == projectNumber:
                        if finderWindow.lower() == 'y':
                            shutil.copy(fullFile, emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder + "/")
                            subprocess.call(["open", "-R", emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder + "/"])
                        else:
                            shutil.copy(fullFile, emailServerPath + emailServerCommon + "/" + fileInner + "/" + smallFolder + "/")
                        print("http://www.nelnet.net/marketingprod/email/{0}/{1}/{2}/{3}".format(emailServerCommon, fileInner, smallFolder, fileTitle))
#things to add: fix wonky folders, make project number not input based.

link-it(file-site)
