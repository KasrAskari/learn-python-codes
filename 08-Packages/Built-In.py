

###? Built-in Packages ###

import math
import os

print (math.pi)
print(math.sqrt(16))

path = "C:\Users\Asus\OneDrive\Documents\Visual Studio\Python"
filename = "image.jpg"

print(os.path.join(path, filename))



###? Not Built-in Packages ###
#~pip install "package name"
#~pip show "package name" --show version
#~pip install "package name==version" --install Version
#~pip uninstall "package name"

import numpy #^Matris
import gradio #^Mavhine Model Demo
import pandas #^Data Analysis
import cv2 #^Image Processing


#%%
###? Created Package ### --from myPackage.py
import myPackage

print (myPackage.func_add_numbers (13, 2))