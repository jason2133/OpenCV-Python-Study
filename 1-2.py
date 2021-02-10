import cv2
import sys
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('./1/cat.bmp')

# 색깔을 변환한다 : cvtColor
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# 여기서는 BGR을 RGB로 바꾼다.

# 축 삭제
plt.axis('off')
plt.imshow(img2)
plt.show()

img3 = cv2.imread('./1/cat.bmp', cv2.IMREAD_GRAYSCALE)
# 흑백으로 읽은 다음

plt.axis('off')
plt.imshow(img3, cmap='gray')
plt.show()

