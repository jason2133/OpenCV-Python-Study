# 트랙바 사용하기
# 0은 검정, 255는 흰색

import cv2
import numpy as np
import matplotlib.pylab as plt

def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255
    
    img[:] = value
    # 숫자로 치환하고

    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)
# 모두 0으로 검정색으로 만들어라

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

