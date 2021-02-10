# 키보드 이벤트 처리하기

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./2/cat.bmp')
# cv2.IMREAD_GRAYSCALE

cv2.imshow('image1', img)

while True:
    if cv2.waitKey(0) == 27:
        break
    elif cv2.waitKey(0) == ord('i'):
        img = ~img
        cv2.imshow('image2', img)

cv2.destroyAllWindows()
