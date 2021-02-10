import cv2
import numpy as np
import matplotlib.pylab as plt
import sys

# 흑백 GRAY
img1 = cv2.imread('./1/cat.bmp', cv2.IMREAD_GRAYSCALE)

# 색깔 BGR
img2 = cv2.imread('./1/cat.bmp', cv2.IMREAD_COLOR)

# 언체인지드로 그대로 들어간다
img3 = cv2.imread('./1/cat.bmp', cv2.IMREAD_UNCHANGED)

print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img3.shape:', img3.shape)
print('img2.dtype:', img2.dtype)

h, w = img2.shape[:2]
print('img2 size : %d %d' % (h, w))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

if len(img2.shape) == 2:
    print('img2 is a grayscale image')
elif len(img2.shape) == 3:
    print('img2 is a truecolor image')

if len(img3.shape) == 2:
    print('img3 is a grayscale image')
elif len(img3.shape) == 3:
    print('img3 is a truecolor image')
