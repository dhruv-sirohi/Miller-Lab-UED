import os
import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt

data_pull_dir = r'C:\Users\dhruv\Downloads\Bismuth_Data'
#data_push_dir = r'C:\Users\dhruv\Downloads\Bismuth_Data_Processed'
dims = (150,150)

file_num = 0

#source: https://www.codespeedy.com/how-to-iterate-over-files-in-a-given-directory-in-python/

for subdirectories, directories, files in os.walk(data_pull_dir):
    for file_name in files:
        file_loc = subdirectories + os.path.sep + file_name
        if file_loc.endswith(".tiff"):
            print(file_loc)
            print("file #{}".format(str(file_num)))
            file_num += 1
            photo = Image.open(file_loc)
            if (photo.size == (150,150)):
                photo_arr = np.array(photo)/255
                image = Image.fromarray(photo_arr)
                image=image.convert('RGB')
                del_file_loc = file_loc.replace('Bismuth_Data','Bismuth_Data_Processed')
                push_file_loc = del_file_loc.replace('tiff','jpg')
                image.save(push_file_loc)
                
            else:
                #adding some black pixels to the top and bottom so that the image's aspect ratio doesn't change when resizing

                buffer_array = np.zeros((74, 1148))
                photo_arr = np.concatenate((buffer_array,np.array(photo),buffer_array),axis=0)/255  
                resized_photo = Image.fromarray(cv.resize(photo_arr,dims))
                #plt.imshow(resized_photo)
                #plt.show()
                #os.remove(file_loc)
                resized_photo=resized_photo.convert('RGB')
                #del_file_loc = file_loc.replace('Bismuth_Data','Bismuth_Data_Processed')
                push_file_loc = file_loc.replace('tiff','jpg')
                
                resized_photo.save(push_file_loc)

for subdirectories, directories, files in os.walk(data_pull_dir):
    for file_name in files:
        file_loc = subdirectories + os.path.sep + file_name
        if file_loc.endswith(".tiff"):
            os.remove(file_loc)

print("done")

"""   
photo=Image.fromarray(np.random.randn(100,100))
photo.save(data_custom_dir)
"""
