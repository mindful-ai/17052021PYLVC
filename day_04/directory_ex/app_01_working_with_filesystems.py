
import os
import os.path
import shutil
import subprocess

path = r"C:\Users\Purushotham\Desktop\oracle\day_04\mydir"

os.chdir(path)

# Can we do the above logic using comprehension
exts = {os.path.splitext(file)[1][1:] for file in os.listdir()}

# create directories for each of the unique extensions
for ext in exts:
    os.mkdir(ext)

# move the files to the respective directories

for item in os.listdir():
    if os.path.isfile(item):
        src = item                           # test.txt
        dest = os.path.splitext(item)[1][1:] # txt
        finaldest = os.path.join(dest, item) # txt/test.txt
        shutil.move(src, finaldest)







