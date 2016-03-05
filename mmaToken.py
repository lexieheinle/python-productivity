#!/usr/bin/python
import subprocess
import shutil
import time
import os
import re

current_user = os.getcwd()
user_start = current_user.find("Users")
user_end = current_user.find("/", user_start + 6)
user = current_user[user_start + 6:user_end]
users = {"lheinle": '/Users/lheinle/Documents/github/', "clipskey": '/Users/clipskey/Dev/', }
mma_path = users[user] + 'MMAv3/'
print(os.path.isdir(mma_path))
files = []
token_find = r'{{.*}}'
if os.path.isdir(mma_path) == True:
    print(mma_path)
    for file in os.listdir(mma_path):
        print(file[:24])
        if file[:24] == 'messages-loan-statement-' and file.endswith(".html") and file[-10:] != '-demo.html':
            files.append(file)
print("Here are the files that will be searched for token regex.")
print(files)
for fil in files:
    old_file_path = mma_path + fil
    with open(old_file_path, "r") as content:
        lines = content.readlines()
        new_lines = []
        for line in lines:
            new_line = re.sub(token_find,'XXXXXX', line)
            new_lines.append(new_line)
    new_fil_path = mma_path + fil[:-5] + '-demo.html'
    with open(new_fil_path, 'w') as new_content:
        for new_line in new_lines:
            new_content.write(new_line)
    print('Replaced tokens in {0}'.format(new_fil_path))
