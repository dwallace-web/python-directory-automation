from datetime import date
import os
import shutil
import glob

# find all files
path = 'C:\\Users\\David\\Desktop\\example_downloads_folder\\start'
files = os.listdir(path)
# todays date prefix
date_prefix = date.today()
# version number for global variable
version = 0

print('todays date is ' + str(date_prefix))

# confirm the CWD
print('the CWD is: ' + os.getcwd())

# create a new folder -- add prefix -- confirm verison number
os.mkdir(str(date_prefix) + '_V' + str(version) + '_' + 'EXAMPLE2')

# add login to iterate version number


# confirm director and show all files in the directory
print('current directory is ' + path)
for file in files:
    print('Here is one of all files in this folder.... ' + file)


# find only files that fit a criteria - .txt
for file in glob.glob('*.txt'):
    print('txt file --> ' + file)
