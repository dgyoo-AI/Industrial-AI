import colorsys

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

def ImageMakePad(src):
	img = image.load_img(src)
	width = img.width
	height = img.height
	if width > height:
		height = width
	else:
		width = height
	width = width + width // 10
	height = height + height // 10
	try:
		img_resize = tf.image.resize_with_pad(img, width, height)
		x = img_to_array(img_resize)
		xcopy = x.copy()
		black_pixels_mask = np.all(xcopy == [0, 0, 0], axis=-1)
		xcopy[black_pixels_mask] = [68, 1, 84]
		xcopy = xcopy.reshape((1,) + xcopy.shape)
	except Exception as e:
		print(e)
	return xcopy

def MakeFolders(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath)

def MakeShearingImg(x, dest_dir, filename, makenum):
	np.random.seed(10)
	try:
		datagen = ImageDataGenerator(
			#shear_range=0.5,
			shear_range=0.8,
			fill_mode='constant',
			cval=0,
		)

		i = 0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'shear.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth, img_copy, file_format='png')

			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)

def MakeTranlateImg(x, dest_dir, filename, makenum):
	np.random.seed(10)
	try:
		datagen = ImageDataGenerator(
			width_shift_range=0.1,#0.05
			height_shift_range=0.1,#0.05
			fill_mode='constant',
			cval=0,
		)
		i = 0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'trans.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth, img_copy, file_format='png')
			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)

def MakeFlipImg(x,dest_dir,filename,makenum):
	np.random.seed(10)
	try:
		datagen = ImageDataGenerator(
			vertical_flip= True,
			horizontal_flip= True,
			fill_mode='constant',
			cval=0,
		)
		i = 0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'flip.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth, img_copy, file_format='png')

			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)



def MakeZoomImg(x,dest_dir,filename,makenum):
	np.random.seed(100)
	try:
		datagen = ImageDataGenerator(
			 	zoom_range=0.1,
			    #zoom_range=0.4,
				fill_mode='constant',
				cval=0,
		)
		i = 0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'zoom.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth, img_copy, file_format='png')

			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)

def MakeMixImage(x,dest_dir,filename,makenum):
	np.random.seed(100)
	try:
		datagen = ImageDataGenerator(
				rotation_range=150,
				width_shift_range=0.05,
				height_shift_range=0.05,
				shear_range=0.5,
				zoom_range=0.05,
				fill_mode='constant',
				cval=0,
		)

		i =0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'mix.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth,img_copy,file_format='png')

			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)


def MakeRotateImg(x,dest_dir,filename,makenum):
	np.random.seed(100)
	try:
		datagen = ImageDataGenerator(
				rotation_range=170,
				fill_mode='constant',
				cval=0,
		)
		i =0
		for batch in datagen.flow(x, batch_size=1):
			savepth = dest_dir + '/' + filename + '_' + str(i) + 'rot.png'
			img_copy = batch[0].copy()
			black_pixels_mask = np.all(batch[0] == [0, 0, 0], axis=-1)
			img_copy[black_pixels_mask] = [68, 1, 84]
			image.save_img(savepth,img_copy,file_format='png')

			i += 1
			if i > makenum:
				break;

	except Exception as e:
		print(e)

image_loc_folder = os.getcwd() +'/waferimages_test/training/';
labels2 = ['Center', 'Donut', 'Edge-Loc', 'Edge-Ring', 'Loc', 'Random', 'Scratch', 'Near-full']

for i in range(8):
	#if i != 7:
	#	continue
	loc = image_loc_folder + labels2[i]
	file_list = os.listdir(loc)
	ncnt = 10000 - len(file_list)
	multiful = 1;
	#if i == 7:
	#	multiful = 2


	if ncnt > 0 :

		locmakeRotFile = loc + '_rotate';
		MakeFolders(locmakeRotFile)
		locmakeZoomFile = loc + '_zoom';
		MakeFolders(locmakeZoomFile)
		locmakeFlipFile = loc + '_flip';
		MakeFolders(locmakeFlipFile)
		locmakeTranslateFile = loc + '_translate';
		MakeFolders(locmakeTranslateFile)
		locmakeShearingFile = loc + '_shearing';
		MakeFolders(locmakeShearingFile)
		locmakeMixFile = loc + '_Mix';
		MakeFolders(locmakeMixFile)
		j = 0
		print(len(file_list))
		for j in range(len(file_list)):

			ori_filename = loc +'/'+file_list[j]
			x = ImageMakePad(ori_filename)
			filename = file_list[j].replace('.png','')
			MakeRotateImg(x,locmakeRotFile,filename,20*multiful)
			MakeZoomImg(x, locmakeZoomFile, filename, 1)
			MakeFlipImg(x, locmakeFlipFile, filename, 2)
			MakeTranlateImg(x, locmakeTranslateFile, filename, 2)
			MakeShearingImg(x, locmakeShearingFile, filename, 5)
			MakeMixImage(x, locmakeMixFile, filename, 10)

print('finish')






