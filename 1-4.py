import cv2
import sys
import numpy as np
import matplotlib.pylab as plt

import os

file_list = os.listdir('./images')
img_files = [file for file in file_list if file.endswith('.jpg')]

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image Load Failed')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break
    
    idx += 1

    if idx >= cnt:
        idx = 0


