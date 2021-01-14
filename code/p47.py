import cv2

img = cv2.imread('../img/elonmusk_a.jpg')

cv2.putText(img, "Elon The GOD", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
cv2.putText(img, "Falcon 9", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
cv2.putText(img, "SpaceX", (50, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
cv2.putText(img, "Tesla", (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0))
cv2.putText(img, "Open AI", (200, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

cv2.imshow('Elon Haha', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
