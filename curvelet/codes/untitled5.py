# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:17:23 2020

@author: Banhi
"""

from PIL import Image
import os
import shutil
import array
import cv2
import numpy as np
import sys, time


path='E:/vector/code try/pic.png'
print(path)
#image = Image.open(path)
#print(image.shape)

#print(type(image))

image = cv2.imread(path)
#print(type(im))

#print(im.shape)
#print(type(im.shape))

window = 4 
threshold = 9 
spam = False



size = image.shape[:2]
    ## set filter window and image dimensions
W = 2*window + 1
ylength, xlength = size
vlength = W*W
if spam:
        print ('Image length in X direction: ', xlength)
        print ('Image length in Y direction: ', ylength)
        print ('Filter window size: ', W, 'x', W)

    # create 2-D image array and initialize window
image_array =np.reshape(array(image, dtype=np.uint8), (ylength,xlength))
filter_window = array(np.zeros((W,W)))
target_vector = array(np.zeros(vlength))
pixel_count = 0
try:
        # loop over image with specified window W
        for y in range(window, ylength-(window+1)):
            for x in range(window, xlength-(window+1)):
                # populate window, sort, find median
                filter_window = image_array[y-window:y+window+1,x-window:x+window+1]
                target_vector = np.reshape(filter_window, ((vlength), ))
                # internal sort
                median = np.demo(target_vector, vlength)
                # median = medians_1D.quick_select(target_vector, vlength)
	            # check for threshold
                if not threshold > 0:
                    image_array[y,x] = median
                    pixel_count += 1
                else:
                    scale = np.zeros(vlength)
                    for n in range(vlength):
                        scale[n] = abs(int(target_vector[n]) - int(median))
                    scale = scale.sort
                    Sk = 1.4826 * (scale[round(vlength/2)])
                    if abs(int(image_array[y,x]) - int(median)) > (threshold * Sk):
                        image_array[y,x] = median
                        pixel_count += 1

except TypeError:
        # print ("Error in processing function:", err)
        # NameError, ArithmeticError, LookupError
        sys.exit(2)

    # print (pixel_count, "pixel(s) filtered out of", xlength*ylength)
print(image_array)
    # convert array back to sequence and return
    # return reshape(image_array, (xlength * ylength, )).tolist()
 



























