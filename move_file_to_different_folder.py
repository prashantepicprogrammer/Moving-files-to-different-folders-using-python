import os
import shutil

currentfilepath = input('Enter the path of the file : ')
filename = input('Enter the file name : ')
pathwheretomove = input('Enter the path where you wanna move the file : ')
os.chdir(currentfilepath)
completepath = currentfilepath + filename

shutil.move(completepath , pathwheretomove)