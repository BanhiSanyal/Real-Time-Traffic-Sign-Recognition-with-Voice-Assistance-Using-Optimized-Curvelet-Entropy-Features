# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:28:50 2020

@author: Banhi
"""

import numpy as np
import pickle
import cv2
from os import listdir
from os.path import join, dirname, realpath
from sklearn.preprocessing import LabelBinarizer
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation, Flatten, Dropout, Dense
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os



path = "D:\\signDatabasePublicFramesOnly\\vid0"



EPOCHS = 50
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((256, 256))
image_size = 0
directory_root = path
width = 256
height = 256
depth = 3


def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, default_image_size)
            return img_to_array(image)
        else:
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

image_list, label_list = [], []




"""
try:
    print("Loading images")
    plant_disease_folder_list = listdir(join(dirname(path), "vid0", "frameAnnotations-vid_cmp2.avi_annotations"))
    for plant_disease_folder in plant_disease_folder_list:
        plant_disease_image_list = listdir(join(dirname(path), "PlantVillage-Dataset", "raw", plant_disease_folder))
        for single_plant_disease_image in plant_disease_image_list:
            print(f"Processing {single_plant_disease_image}")
            images = listdir(join(dirname(path), "PlantVillage-Dataset", "raw", plant_disease_folder,
                                  single_plant_disease_image))
            for image in images[:30]:
                image_directory = join(dirname(path), "PlantVillage-Dataset", "raw", plant_disease_folder,
                                       single_plant_disease_image, image)
                if image_directory.endswith(".jpg") == True or image_directory.endswith(".JPG") == True:
                    image_list.append(convert_image_to_array(image_directory))
                    # label_list.append(plant_disease_folder)
                    label_list.append(single_plant_disease_image)
                    # label_list.append(image)
    print("Image loading completed")
except Exception as e:
    print(f"Error : {e}")
"""


image_size = len(image_list)

label_binarizer = LabelBinarizer()
image_labels = label_binarizer.fit_transform(label_list)
pickle.dump(label_binarizer, open('label_transform.pkl', 'wb'))
n_classes = len(label_binarizer.classes_)














