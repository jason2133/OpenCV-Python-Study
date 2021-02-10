import cv2
import numpy as np
import matplotlib.pylab as plt

# 흑백
src1 = cv2.imread('./3/lenna.bmp', cv2.IMREAD_GRAYSCALE)

# 정식 cv2
dst1 = cv2.add(src1, 100)

# numpy : 255보다 값이 커지면 해당 값에서 255를 뺀 값이 적용된다.
dst2 = src1 + 100

# 칼라
src2 = cv2.imread('./3/lenna.bmp')

# 밑에 2개는 결과 동일
dst3 = cv2.add(src2, (100, 100, 100, 0))
dst4 = np.clip(src2 + 100., 0, 255).astype(np.uint8)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()
