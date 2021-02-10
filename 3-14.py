import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./3/lenna.bmp', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()


