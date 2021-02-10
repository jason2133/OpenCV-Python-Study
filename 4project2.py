import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('football1.jpg')

dst1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

dst2 = cv2.GaussianBlur(dst1, (0, 0), 17)

dst3 = cv2.divide(dst1, dst2) * 170

dst4 = cv2.add(dst3, 90)

cv2.imshow('fin', dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()

