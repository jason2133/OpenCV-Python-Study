import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('./3/lenna.bmp')

colors = ['b', 'g', 'r']
bgr = cv2.split(src)

for (p, c) in zip(bgr, colors):
    # bgr은 그림 나눈거, colors는 그 칼라 이름

    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
    # 그 colors에 따라 hist 히스토그램을 그려라

plt.show()
