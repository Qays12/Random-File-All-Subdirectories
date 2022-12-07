import os
import random
import shutil

source = input("Enter the folder directory: ")
dest = input("Enter the Destination directory: ")

pathchooser = rf'{source}'
files = os.listdir(pathchooser)
randomfile = random.choice(files)

dire_path = rf'{dest}'
for dir_path, subdir_list, file_list in os.walk(dire_path):
    for fname in subdir_list:
        full_path = os.path.join(dir_path, fname)
        print(full_path)
        path = rf'{source}/{randomfile}'
        sendpath = rf'{full_path}/{randomfile}'
        shutil.copy(path, sendpath)
