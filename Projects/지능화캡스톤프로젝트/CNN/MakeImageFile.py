import os
from os.path import join
import numpy as np
import pandas as pd
import gc
import matplotlib.pyplot as plt


datapath = join('data', 'wafer')

print(os.listdir("../input"))
import warnings
warnings.filterwarnings("ignore")

def MakeFolders(filepath):
	if not os.path.exists(filepath):
		os.makedirs(filepath)

parent_loc = os.getcwd();

df=pd.read_pickle("../input/LSWMD.pkl")
s = df.waferMap.size
print(df)
print(s)

for i in range(0,s):
	if df.trianTestLabel[i].size > 0:
		img = df.waferMap[i]
		trainTest = df.trianTestLabel[i][0][0]
		failure = df.failureType[i][0][0]
		if trainTest == "Training":
			savefolder = parent_loc+ '/waferimages_test/training/'+str(failure)
			loc = parent_loc+ '/waferimages_test/training/'+str(failure)+'/'+str(i)+'.png'
		else:
			savefolder = parent_loc + '/waferimages_test/testing/' + str(failure)
			loc = parent_loc+ '/waferimages_test/testing/'+str(failure)+'/'+str(i)+'.png'

		MakeFolders(savefolder)
		plt.imsave(loc,img)

	if i % 100 == 0:
		collected = gc.collect()
	i = i + 1

print('save finish')



