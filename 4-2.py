import cv2
import numpy as np

src = cv2.imread('./4/rose.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('src', src)

for ksize in (3, 5, 7):
    dst = cv2.blur(src, (ksize, ksize))

    cv2.imshow('dst %d' % (ksize), dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()
