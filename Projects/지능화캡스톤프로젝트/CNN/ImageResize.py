
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

import os
from os.path import join
import numpy as np
import pandas as pd
import gc
import matplotlib.pyplot as plt
import PIL
import PIL.Image
#import cv2
import tensorflow as tf
from matplotlib import colors

width = 26
height = 26


image_loc_folder = os.getcwd() +'/waferimages/training/';
#image_loc_folder = os.getcwd() +'/waferimages/testing/';
labels2 = ['Center', 'Donut', 'Edge-Loc', 'Edge-Ring', 'Loc', 'Random', 'Scratch', 'Near-full']


image_src_root_folder = os.getcwd() +'/waferimages/training-copy/';
#image_src_root_folder = os.getcwd() +'/waferimages/testing-copy/';

def MakeFolders(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath)


for i in range(8):
    if i!= 7:
        continue
    ori_folder = image_src_root_folder+labels2[i]+'/'

    file_list = os.listdir(ori_folder)
    save_folder = image_loc_folder +labels2[i]+'/'
    MakeFolders(save_folder)
    #copy_cnt = 0;
    if len(file_list) > 10000:
        copy_cnt = 10000
    else :
        copy_cnt = len(file_list)

    for j in range(copy_cnt):
        load_name = ori_folder+file_list[j]
        img = image.load_img(load_name)
        img_resize = tf.image.resize(img, (width, height))
        save_name = save_folder+file_list[j]
        image.save_img(save_name,img_resize)

print('finish')