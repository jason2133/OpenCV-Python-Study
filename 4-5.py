import cv2
import numpy as np

src = cv2.imread('./4/lenna.bmp')

dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

