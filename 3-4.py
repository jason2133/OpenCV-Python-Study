import cv2
import numpy as np
import matplotlib.pylab as plt

src1 = cv2.imread('./3/candies.png', cv2.IMREAD_COLOR)

src2 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)

b, g, r = cv2.split(src2)


cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

