# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:48:03 2020

@author: Banhi
"""

import os
import shutil

import cv2
import numpy
import sys, time
#import medians_1D
from numpy import *
from os.path import join, dirname, realpath, isfile
train_path = "F:\\ResearchPractice\\Dataset\\GTSRB_Final_Training_Images\\GTSRB\Final_Training\\Images\\"
test_path = "F:\\ResearchPractice\\Dataset\\GTSRB_Final_Test_Images\\GTSRB\\Final_Test\\Images\\"
preprocessed_train_path = "F:\\ResearchPractice\\Dataset\\GTSRB_Final_Training_Images\\GTSRB\\Final_Training\\Preprocessed_images\\"
preprocessed_test_path = "F:\\ResearchPractice\\Dataset\\GTSRB_Final_Test_Images\\GTSRB\\Final_Test\\Preprocessed_images\\"


def demo(target_array, array_length):
    sorted_array = sort(target_array)
    median = sorted_array[round(array_length/2)]
    return median

def process(image, window = 4, threshold = 9, spam = False):
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
    image_array = reshape(array(image, dtype=uint8), (ylength,xlength))
    filter_window = array(zeros((W,W)))
    target_vector = array(zeros(vlength))
    pixel_count = 0
    try:
        # loop over image with specified window W
        for y in range(window, ylength-(window+1)):
            for x in range(window, xlength-(window+1)):
                # populate window, sort, find median
                filter_window = image_array[y-window:y+window+1,x-window:x+window+1]
                target_vector = reshape(filter_window, ((vlength), ))
                # internal sort
                median = demo(target_vector, vlength)
                # median = medians_1D.quick_select(target_vector, vlength)
	            # check for threshold
                if not threshold > 0:
                    image_array[y,x] = median
                    pixel_count += 1
                else:
                    scale = zeros(vlength)
                    for n in range(vlength):
                        scale[n] = abs(int(target_vector[n]) - int(median))
                    scale = sort(scale)
                    Sk = 1.4826 * (scale[round(vlength/2)])
                    if abs(int(image_array[y,x]) - int(median)) > (threshold * Sk):
                        image_array[y,x] = median
                        pixel_count += 1

    except TypeError:
        # print ("Error in processing function:", err)
        # NameError, ArithmeticError, LookupError
        sys.exit(2)

    # print (pixel_count, "pixel(s) filtered out of", xlength*ylength)
    return image_array
    # convert array back to sequence and return
    # return reshape(image_array, (xlength * ylength, )).tolist()


def histeq(img):
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)


def psnr_ad_mse(img, ref):
    h, w = ref.shape[:2]
    SE = (double(img) - double(ref)) ** 2  # Squared Error
    MSE = sum(sum(SE)) / (h * w)  # Mean Square Error
    MAXI = 255
    if MSE == 0:
        return inf, 0
    psnr = 10 * log10((MAXI ^ 2) / MSE)
    return psnr, MSE

# psnr1, psnr2, mse1, mse2, count1, count2 = 0, 0, 0, 0, 0, 0

def preprocess(img_location):
    img = cv2.imread(img_location)  # , cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("original image", img)
    # cv2.waitKey(0)

    # resize
    img = cv2.resize(img, (200, 200))
    # cv2.imshow("resized image", img)
    # cv2.waitKey(0)

    # RGB to Grayscale
    print("Conversion of original image to grayscale")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # psnr, mse = psnr_ad_mse(gray, img)
    # cv2.imshow("grayscale", gray)
    # cv2.waitKey(0)

    # Adaptive Median Filter
    print("Adaptive Median Filter")
    # output1 = process(gray, window = 2)
    output = process(gray)
    # print(psnr_ad_mse(output, gray))
    # psnr1, mse1 = psnr_ad_mse(output1, gray)
    # psnr2, mse2 = psnr_ad_mse(output, gray)
    # if psnr1 == inf or (psnr1 > psnr2 and mse1 < mse2):
    #     print("5X5:")
    #     print(psnr1, mse1)
    #     count1 = count1+1
    # else:
    #     print("9X9:")
    #     print(psnr2, mse2)
    #     count2 = count2+1
    # cv2.imshow("adaptive median filter", output)
    # cv2.waitKey(0)
    # return count1, count2

    kernel = numpy.ones((5, 5), numpy.uint8)
    # erosion
    print("Erosion")
    img_erosion = cv2.erode(output, kernel, iterations=1)
    # print(psnr_ad_mse(img_erosion, gray))
    # cv2.imshow("erosion", img_erosion)
    # cv2.waitKey(0)

    # dilation
    print("Dilation")
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
    # print(psnr_ad_mse(img_dilation, img_erosion))
    # cv2.imshow("dilation", img_dilation)
    # cv2.waitKey(0)

    # histogram equalisation
    print("Histogram Equalisation")
    equalized = histeq(img_dilation)
    # print(psnr_ad_mse(equalized, img_dilation))
    # cv2.imshow("equalized", equalized)
    # cv2.waitKey(0)

    return equalized

test_images = [f for f in os.listdir(test_path) if (isfile(join(test_path, f)) and f.endswith('.ppm'))]
preprocessed_testimages = []
for image in test_images:
    img_location = join(test_path, image)
    img = preprocess(img_location)
    preprocessed_testimages.append(img)
    cv2.imwrite(join(preprocessed_test_path, image), img)

# count_win5, count_win9 = 0, 0
# class_folder = join(dirname(path), "color")
classes = [f for f in os.listdir(train_path)]
preprocessed_trainimages = []
count1, count2 = 0, 0
for single_class in classes:
    images_path = join(dirname(train_path), single_class)
    images = [f for f in os.listdir(images_path) if (isfile(join(images_path, f)) and f.endswith('.ppm'))]
    # c = 0
    for image in images:
        img_location = join(images_path, image)
        # c = c+1
        img = preprocess(img_location)
        preprocessed_trainimages.append(img)
        cv2.imwrite(join(preprocessed_train_path, single_class, image), img)
        # count1, count2 = preprocess(img_location, count1, count2)
        # if True:
        # if c == 5:
        #     break
    # if True:
    # if c <= 5:
    #     break
# except Exception as e:
#     pass
# print('5X5:', count1, '9X9:', count2)