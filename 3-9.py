import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./3/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.equalizeHist(src)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
