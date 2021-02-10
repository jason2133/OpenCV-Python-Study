import cv2

src = cv2.imread('./3/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('img', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
