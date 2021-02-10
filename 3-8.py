import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./3/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
dst2 = cv2.equalizeHist(src)

# cv2.imshow('dst', dst)
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

