from datetime import date
import os
import glob
from shutil import copy2, copyfile

# ADD INPUT FOR TYPE of file
lookfor = input("Archive All Files like: ")
# add input for path name
storein = input("Put the Files in this Folder: ")

# find all files
path = os.getcwd()
files = os.listdir(path)
# todays date prefix
date_prefix = date.today()
# version number for global variable
global version
version = 0
# build the path
global string
string = str(date_prefix) + '_V' + str(version) + '_' + str(storein)
print(string)

# iterate version number here
print(os.path.exists(string))

while os.path.exists(string) == True:
    version += 1
    string = str(date_prefix) + '_V' + str(version) + '_' + str(storein)
    print(version)
    print(string)
else:
    # create a new folder
    os.mkdir(string)

# confirm and show all files in the directory
# print('the CWD is: ' + os.getcwd())
# for file in files:
#     print('Here is one of all files in this folder.... ' + file)

# find only files that fit a criteria - .txt
for file in glob.glob('*' + lookfor + '*'):

    # add logic to skip folders
    if os.path.isdir(file) == True:
        print('this is a directory -->' + file)
        continue

    print('Found ---> ' + file)
    print(os.getcwd() + '\\' + file)
    print(os.getcwd() + '\\' + string + '\\' + file)
    copyfile(os.getcwd() + '\\' + file, os.getcwd() +
             '\\' + string + '\\' + file)
    # for each file that matches copy the file and place it in the correct folder
