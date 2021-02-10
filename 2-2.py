import cv2
import numpy as np
import matplotlib.pylab as plt
import sys

img1 = np.empty((480, 640), dtype=np.uint8)
img2 = np.zeros((480, 640, 3), dtype=np.uint8)
img3 = np.ones((480, 640), dtype=np.uint8) * 255
# * 255를 해줘야 하얗게 칠해줄 수 있다. 255가 흰색이다.

img4 = np.full((480, 640, 3), (0, 255, 255), dtype=np.uint8)
img5 = np.full((480, 640, 3), (110, 120, 250), dtype=np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img5', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()

