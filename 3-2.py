import sys
import numpy as np
import cv2
# from matplotlib import pyplot as plt


src1 = cv2.imread('./3/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./3/square.bmp', cv2.IMREAD_GRAYSCALE)

# if src1 is None or src2 is None:
#     print('Image load failed!')
#     sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
# plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
# plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
# plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
# plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
# plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
# plt.show()
