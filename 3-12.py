import cv2

src1 = cv2.imread('./3/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./3/square.bmp', cv2.IMREAD_GRAYSCALE)

src3 = cv2.add(src1, src2)
src4 = cv2.subtract(src1, src2)

src5 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)
src6 = cv2.absdiff(src1, src2)

cv2.imshow('img1', src1)
cv2.imshow('img2', src2)
cv2.imshow('img3', src3)
cv2.imshow('img4', src4)
cv2.imshow('img5', src5)
cv2.imshow('img6', src6)

cv2.waitKey(0)
cv2.destroyAllWindows()

