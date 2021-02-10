import cv2

src = cv2.imread('./3/lenna.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src, 100)
dst2 = src + 100

cv2.imshow('img1', dst1)
cv2.imshow('img2', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

