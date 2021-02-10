# 마스크 연산과 ROI

import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./2/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('./2/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./2/field.bmp', cv2.IMREAD_COLOR)

cv2.copyTo(src, mask, dst)

# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()



