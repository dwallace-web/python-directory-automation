import os
import shutil
import glob

# find all files
path = 'C:\\Users\\David\\Desktop\\example_downloads_folder\\start'
files = os.listdir(path)

for file in files:
    print('Here is one of all files in this folder.... ' + file)

# find only files that fit a criteria - .txt
os.chdir(path)
print('current directory is ' + path)

for file in glob.glob('*.txt'):
    print('txt file --> ' + file)

# confirm the CWD
print('the CWD is: ' + os.getcwd())

# move up the CWD
os.chdir('/tmp')

# qa the CWD
print('the CWD is: ' + os.getcwd())

# copy files to new folder


# add pre-fix & label files with the date they were moved


#
