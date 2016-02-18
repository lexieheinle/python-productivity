#!/usr/bin/python
import subprocess
import shutil
import time
import os
import re

currentUser = os.getcwd()
userStart = currentUser.find("Users")
userEnd = currentUser.find("/", userStart + 6)
user = currentUser[userStart + 6:userEnd]
users = {"lheinle": '/Users/lheinle/Documents/github/', "clipskey": '/Users/clipskey/Dev/', }
mmaPath = users[user] + 'MMAv3/'
print(os.path.isdir(mmaPath))
files = []
tokenFind = r'{{.*}}'
if os.path.isdir(mmaPath) == True:
    print(mmaPath)
    for file in os.listdir(mmaPath):
        print(file[:24])
        if file[:24] == 'messages-loan-statement-' and file.endswith(".html") and file[-10:] != '-demo.html':
            files.append(file)
print("Here are the files that will be searched for token regex.")
print(files)
for fil in files:
    oldFilPath = mmaPath + fil
    content = open(oldFilPath, "r")
    lines = content.readlines()
    newLines = []
    for line in lines:
        newLine = re.sub(tokenFind,'XXXXXX', line)
        newLines.append(newLine)
    content.close()
    newFilPath = mmaPath + fil[:-5] + '-demo.html'
    newContent = open(newFilPath, 'w')
    for newLine in newLines:
        newContent.write(newLine)
    newContent.close()
    print('Replaced tokens in {0}'.format(newFilPath))
