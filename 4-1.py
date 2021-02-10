import cv2
import numpy as np

src = cv2.imread('./4/rose.bmp', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])
                
# np.ones((3, 3), dtype = np.float64) / 9

dst = cv2.filter2D(src, -1, kernel)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

