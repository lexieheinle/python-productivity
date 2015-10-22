#!/usr/bin/python
import subprocess
import shutil
import time
import os

currentUser = os.getcwd()
userStart = currentUser.find("Users")
userEnd = currentUser.find("/", userStart + 6)
user = currentUser[userStart + 6:userEnd]
users = {"lheinle": ["Lexie", "Brackets", r'/Applications/Brackets.app/Contents/MacOS/Brackets'], "seckles": ["Steph", "DreamWeaver", r'/Applications/Adobe Dreamweaver CC 2015/Adobe Dreamweaver CC 2015.app/Contents/MacOS/Dreamweaver'], "dlipskey": ["Claire", "DreamWeaver", r'/Applications/Adobe Dreamweaver CC 2015/Adobe Dreamweaver CC 2015.app/Contents/MacOS/Dreamweaver'], "mlambie": ["Mitch", "DreamWeaver", r'/Applications/Sublime Text 2.app/Contents/MacOS/Sublime Text 2'] }
print("Hi, {} \n Let's start/edit an email project!".format(users[user][0]))
fileSite = input("Enter the file path (start from year and go to the production /) If you don't have it, type N: ") 
projectNumber = input("Enter the project number: ")
newProject = input("Is this a new project? (Type y for yes): ")
def brackIt(filePath):
    if filePath.lower() == 'n':
        print("Let's find that file path!") #assumes 2015 email date
        serverPath = "/Volumes/marketing$/Creative Services/2015/"
        mainDivision = input("Enter the main division.(i.e. NDS) :")
        if os.path.isdir(serverPath + mainDivision) == True:
            print(serverPath + mainDivision)
        subDivisions = input("Enter the sub division. (i.e. MBLE_EP) :")#need to search for correct project folder
        #fullFile = "{}/{}/{}/serverPath + file
        
    else:
        filePath = filePath.replace("\\", "/") #take care of windows weirdness
        serverPath = "/Volumes/marketing$/Creative Services/" 
        fullFile = serverPath + filePath #add weird server path
        startFileName = filePath.find(projectNumber)
        endFileName = filePath.find("Design")
        fileName = filePath[startFileName:endFileName - 1] #cuts from project number to title
        programPath = users[user][2]
    def newOne():
        templates = {"MMA": "Interactive/Templates/Emails/Templates/MMA_Template508.html", "GreenOperational": "Interactive/Templates/Emails/Templates/Nelnet/Green-Operational-Template.html", "GreenWelcome": "Interactive/Templates/Emails/Templates/Nelnet/Green-Welcome-Template.html", "BluePromotional": "Interactive/Templates/Emails/Templates/Nelnet/Blue-Promotional-Template.html", "QM-BluePromotional": "Interactive/Templates/Emails/Templates/Nelnet/QM_Blue-Promotional-Template.html", "QM-GreenOperational": "Interactive/Templates/Emails/Templates/Nelnet/QM_Green-Operational-Template.html", "QM-GreenWelcome": "Interactive/Templates/Emails/Templates/Nelnet/QM_Green-Welcome-Template.html"}
        print("Your template options are: ")
        for key in templates.keys():
            print (key, sep=" | ")
        templateChoice = input("Which template do you need? (Select via title): ")
        templateFilePath = serverPath + templates[templateChoice]
        newFilePath = fullFile + fileName +"_{}{}.html".format(time.strftime("%m"), time.strftime("%d"))
        print("This is the new file you created:\n\n" + filePath + fileName + "_{}{}.html".format(time.strftime("%m"), time.strftime("%d")) ) #this is used for makeLive
        shutil.copy(templateFilePath, newFilePath) #copy the template 
        subprocess.check_call(["open", "-a", programPath, newFilePath])
    if newProject.lower() == 'y':
        newOne()
    else:
        htmlFiles = [];
        for file in os.listdir(fullFile):
            if file.endswith(".html"):
                htmlFiles.append(file)
        print("Here are all the files in that folder...")
        print (htmlFiles)
        correctFile = eval(input("Select the file you need to edit by entering 1 for first: "))
        numConvert = correctFile - 1 #adjust for zero based files location
        print("Copying, moving and opening {}".format(htmlFiles[numConvert]))
        #should filename rely on file folders?
        baseStart = htmlFiles[numConvert].rfind("_") 
        baseTitle = htmlFiles[numConvert][:baseStart] #filename without Date
        oldFilePath = serverPath + filePath + htmlFiles[numConvert]
        newFilePath = fullFile + baseTitle +"_{}{}.html".format(time.strftime("%m"), time.strftime("%d"))
        print("This is the new file you created:\n\n" + filePath + baseTitle + "_{}{}.html".format(time.strftime("%m"), time.strftime("%d"))) #this is used for makeLive
        shutil.copy(oldFilePath, newFilePath) #copy old file with new name
        oldProd = filePath.replace("Production", "_oldProduction") #find old production folder path
        shutil.move(oldFilePath, serverPath + oldProd + htmlFiles[numConvert]) #move old file to production
        subprocess.check_call(["open", "-a", programPath, newFilePath])
        print("\nThank you for using Lexie's findIt program. \n Any suggestions give Lexie a hollar!")
#things to add....Add commonly used templates, add version 1 or 2 options, automatically get project number from path, open finder window also from input
brackIt(fileSite)
