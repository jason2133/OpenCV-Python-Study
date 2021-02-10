# Matplotlib를 활용하여 창 하나에 여러장의 이미지 출력

import cv2
import sys
import numpy as np
import matplotlib.pylab as plt

img1 = cv2.imread('./1/cat.bmp')
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img3 = cv2.imread('./1/cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.subplot(121)
plt.axis('off')
plt.imshow(img2)

plt.subplot(122)
plt.axis('off')
plt.imshow(img3, cmap='gray')

plt.show()

# plt.subplot(123)
# plt.axis('off')
# plt.imshow(img1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


