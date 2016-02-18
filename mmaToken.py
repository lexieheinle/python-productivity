#!/usr/bin/python
import subprocess
import shutil
import time
import os
import re

current-user = os.getcwd()
user-start = current-user.find("Users")
user-end = current-user.find("/", user-start + 6)
user = current-user[user-start + 6:user-end]
users = {"lheinle": '/Users/lheinle/Documents/github/', "clipskey": '/Users/clipskey/Dev/', }
mma-path = users[user] + 'MMAv3/'
print(os.path.isdir(mma-path))
files = []
token-find = r'{{.*}}'
if os.path.isdir(mma-path) == True:
    print(mma-path)
    for file in os.listdir(mma-path):
        print(file[:24])
        if file[:24] == 'messages-loan-statement-' and file.endswith(".html") and file[-10:] != '-demo.html':
            files.append(file)
print("Here are the files that will be searched for token regex.")
print(files)
for fil in files:
    old-fil-path = mma-path + fil
    with open(old-fil-path, "r") as content:
        lines = content.readlines()
        new-lines = []
        for line in lines:
            new-line = re.sub(token-find,'XXXXXX', line)
            new-lines.append(new-line)
    new-fil-path = mma-path + fil[:-5] + '-demo.html'
    with open(new-fil-path, 'w') as new-content:
        for new-line in new-lines:
            new-content.write(new-line)
    print('Replaced tokens in {0}'.format(new-fil-path))
