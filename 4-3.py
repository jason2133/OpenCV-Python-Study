import cv2
import numpy as np

src = cv2.imread('./4/rose.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('src', src)

for sigma in range(1, 6):
    dst = cv2.GaussianBlur(src, (0, 0), sigma)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()
