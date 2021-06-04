from datetime import date
import os
import shutil
import glob

# find all files
path = os.getcwd()
files = os.listdir(path)
# todays date prefix
date_prefix = date.today()
# version number for global variable
version = 0
# build the path
string = str(date_prefix) + '_V' + str(version) + '_' + 'EXAMPLE'

# add logic to iterate version number here
print(os.getcwd().isdir(string))

# create a new folder -- add prefix -- confirm verison number
os.mkdir(string)


# confirm director and show all files in the directory
print('the CWD is: ' + os.getcwd())
for file in files:
    print('Here is one of all files in this folder.... ' + file)

# find only files that fit a criteria - .txt
# not working?????
for file in glob.glob('*.txt'):
    print('txt file --> ' + file)
    # for each file that matches copy the file and place it in the correct folder
    # shutil.copy(r'\\{file}', r'\\{string}\\')
