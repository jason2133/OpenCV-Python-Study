# 영상 생성, 복사, 부분 영상 추출

import cv2
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('./2/HappyFish.jpg')
img2 = img1
img3 = img1.copy()

img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


