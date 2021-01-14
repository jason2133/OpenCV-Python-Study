# 500 x 500 크기의 아무것도 없는 흰색 이미지 만들기

import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)
cv2.imwrite('../img/blank_500.jpg', img)



