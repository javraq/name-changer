"""A program that changes the names from XXXXX to A01, A02, A03, etc, and logs every action"""
import os
import glob
from shutil import copyfile

#ask for all the inputs
ex = input ("welcome to the changer of names!\nThis program will change a bunch of names for you!\nMake sure you put all the files in the old files folder!\nwatch out only use files of one type of extension\nWhat is the extension? ")
input_name= input ("Every file will get its own name being YOURINPUT01 ,02 ,03 etc etc \nWhat is the name you want to use? ")
x = input ("At what number do you want to start counting? ")

#change x from string to int
x = int(x)

# Determinate where the files are
path = 'Old_files/*.' + ex
files = glob.glob(path)

for name in files:
    #if/else statement for deteriminate if you should put a 0 in front of it
    if x < 10:
        new_file_name = input_name + "0" + str(x) + "." + ex
    else:
        new_file_name = input_name + str(x) + "." + ex

    #the actual name changer
    with open(name, 'r') as f:
        log = open('old_new_names.txt', 'a')
        logname = str(f.name)
        logname_final= logname[10:]
        log.write (logname_final + " , " + new_file_name + '\n')
        log.close
        f.close()
        os.rename(f.name , new_file_name)

    #Counter for name every new name
    x = x + 1
