import cv2

img = cv2.imread('../img/blank_500.jpg')

cv2.circle(img, (150, 150), 100, (255, 0, 0))

cv2.circle(img, (300, 150), 70, (0, 255, 0), 5)

cv2.circle(img, (400, 150), 50, (0, 0, 255), -1)

cv2.imshow('circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


