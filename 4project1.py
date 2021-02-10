import cv2
import numpy as np
import matplotlib.pylab as plt

src = cv2.imread('football1.jpg')

dst1 = cv2.bilateralFilter(src, -1, 20, 7)
# 20이랑 7은 sigma라고 생각해주면 좋을듯하다.

dst2 = 255 - cv2.Canny(src, 30, 120)
# Canny로 Edge를 검출한다.

dst2 = cv2.cvtColor(dst2, cv2.COLOR_GRAY2BGR)
# 파일 형식이 같아야 되어서 GRAY를 BGR로 바꿔주면 된다!

fin1 = cv2.bitwise_and(dst1, dst2)
# bitwise_and로 dst1과 dst2를 겹친다.

cv2.imshow('fin1', fin1)
cv2.waitKey(0)
cv2.destroyAllWindows()


