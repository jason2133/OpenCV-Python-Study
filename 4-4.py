import cv2
import numpy as np

src = cv2.imread('./4/noise.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.medianBlur(src, 3)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
