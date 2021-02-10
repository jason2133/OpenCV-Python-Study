import numpy as np
import cv2
import matplotlib.pylab as plt

src = cv2.imread('./3/lenna.bmp')

colors = ['b', 'g', 'r']
bgr = cv2.split(src)
# b g r 나눈 다음에

for (p, c) in zip(bgr, colors):
    hist = cv2.calcHist([p], [0], None, [255], [0, 255])
    plt.plot(hist, color = c)

plt.show()
