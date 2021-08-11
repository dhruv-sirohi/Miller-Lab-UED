import os
import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt
import time
data_pull_dir = r'C:\Users\dhruv\Downloads\Bismuth_Data'
data_push_dir = r'C:\Users\dhruv\Downloads\Bismuth_Data_Processed'
dims = (150,150)

file_num = 0

#source: https://www.codespeedy.com/how-to-iterate-over-files-in-a-given-directory-in-python/

for subdirectories, directories, files in os.walk(data_push_dir):
    for file_name in files:
        file_loc = subdirectories + os.path.sep + file_name
        if file_loc.endswith(".jpg") or file_loc.endswith(".tiff") or file_loc.endswith(".TIF") or file_loc.endswith(".TIFF"):
            os.remove(file_loc)

print("done removing files")

"""
max_vals = []
file_names = []
for subdirectories, directories, files in os.walk(data_pull_dir):
    for file_name in files:
        file_loc = subdirectories + os.path.sep + file_name
        if file_loc.endswith(".tiff"):
            
            #print(file_loc)
            print("file #{}".format(str(file_num)))
            file_num += 1
            photo = Image.open(file_loc)
            
            photo_arr = np.array(photo)

            max_vals.append(np.max(photo_arr))
            file_names.append(file_loc)

            del_file_loc = file_loc.replace('Bismuth_Data','Bismuth_Data_Processed')
            push_file_loc = del_file_loc.replace('tiff','npy')
            
            np.save(file=push_file_loc,arr=photo_arr,allow_pickle = True)   

for i in range(0,10):
    max_val = max(max_vals)
    index_val = max_vals.index(max_val)
    max_val_file_name = file_names[index_val]
    print("Max value: " + max_val)
    print("File name: " + max_val_file_name)
    del max_vals[index_val]
    del file_names[index_val]


print("done")
"""
