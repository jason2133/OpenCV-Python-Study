import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./3/candies.png', cv2.IMREAD_COLOR)

b, g, r = cv2.split(src)
# src에서 b g r 각각 나누어라.

# b = src[:, :, 0]
# g = src[:, :, 1]
# r = src[:, :, 2]
# 이거랑 같은 말이다. src에서 b g r 각각 나누는거다.

cv2.imshow('src', src)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

