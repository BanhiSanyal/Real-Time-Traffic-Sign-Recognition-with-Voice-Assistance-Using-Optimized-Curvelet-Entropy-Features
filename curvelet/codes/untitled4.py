# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 08:22:37 2020

@author: Banhi
"""

import cv2
import numpy as np

img = cv2.imread('pic.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

cv2.imwrite('E:/vector/code try/erosion.png',erosion)
#E:/vector/code try/pic.png'
#cv2.imshow(erosion)
dilation = cv2.dilate(erosion, kernel, iterations=1)
cv2.imwrite('E:/vector/code try/dilation.png',dilation)


print("Histogram Equalisation")
#equalized = histeq(greyscale_image)
equ = cv2.equalizeHist(dilation)
cv2.imwrite('E:/vector/code try/equ.png',equ)
