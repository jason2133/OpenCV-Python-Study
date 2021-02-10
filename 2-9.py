# 연산 시간 측정 방법

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./2/hongkong.jpg')

tm = cv2.TickMeter()

tm.start()

edge = cv2.Canny(img, 50, 100)

tm.stop()

print('Elapsed Time : %d ms' % (tm.getTimeMilli()))

