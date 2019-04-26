"""A program that changes the names from XXXXX to A01, A02, A03, etc, and logs every action"""
import os
import glob
from shutil import copyfile
x = 0

#Adjust your extention here
path = 'Old_files/*.txt'
files = glob.glob(path)

for name in files:
    # Adjust Your extension here
    new_file_name = "A" + str(x) + ".txt"

    with open(name, 'r') as f:
        log = open('old_new_names.txt', 'a')
        log.write (str(f.name) + " , " + new_file_name + '\n')
        log.close
        f.close()
        os.rename(f.name , new_file_name)

    
    x = x + 1
