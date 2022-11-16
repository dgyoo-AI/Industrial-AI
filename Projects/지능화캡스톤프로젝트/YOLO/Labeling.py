#!mkdir -p /archive/labels

import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import xml.etree.ElementTree as et

os.makedirs('../archive/labels', exist_ok=True)
unique_label_names = set()

# 라벨 불러오기
labels = []
label_list = os.listdir('../archive/annotations/')
for i in tqdm(range(len(label_list))):
    label = []
    f = open(os.path.join('../archive/labels', 'hard_hat_workers' + str(i) + '.txt'), 'w')
    xtree = et.parse('../archive/annotations/hard_hat_workers' + str(i) + '.xml')
    size = xtree.find('size')
    for e in xtree.findall('object'):
        name = e.find('name').text
        boundary = e.find('bndbox')
        xmin = int(boundary.find('xmin').text)
        ymin = int(boundary.find('ymin').text)
        xmax = int(boundary.find('xmax').text)
        ymax = int(boundary.find('ymax').text)
        label.append({
            'name': name,
            'boundary': {
                'xmin': xmin,
                'ymin': ymin,
                'xmax': xmax,
                'ymax': ymax
            }
        })
        unique_label_names.add(name)

        label_name = 0 if name == 'head' else \
            1 if name == 'helmet' else \
                2 if name == 'person' else 3
        width = int(size.find('width').text)
        height = int(size.find('height').text)
        xcenter = (xmax + xmin) / width / 2
        ycenter = (ymax + ymin) / height / 2
        xlen = (xmax - xmin) / width
        ylen = (ymax - ymin) / height

        content = "{name} {xcenter} {ycenter} {xlen} {ylen}\n".format(
            name=label_name,
            xcenter=xcenter,
            ycenter=ycenter,
            xlen=xlen,
            ylen=ylen)
        f.write(content)
    f.close()
    labels.append(label)