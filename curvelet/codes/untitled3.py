# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:59:18 2020

@author: Banhi
"""

import cv2
from PIL import Image
import os
import shutil


import numpy
import sys, time
#import medians_1D
import numpy as np
from os.path import join, dirname, realpath, isfile



def demo(target_array, array_length):
    sorted_array = sort(target_array)
    median = sorted_array[round(array_length/2)]
    return median








def histeq(img):
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)






  
path='E:/vector/code try/pic.png'
print(path)
image = Image.open(path)
#image.show()
print(image.format)
print(image.mode)
print(image.size)
print(image.palette)
#image.shape()

new_image = image.resize((200, 200))





print("Conversion of original image to grayscale")

greyscale_image = new_image.convert('L')
greyscale_image.save('greyscale_image.jpg')





