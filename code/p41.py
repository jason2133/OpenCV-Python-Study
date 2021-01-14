# 사각형 그리기

import cv2

img = cv2.imread('../img/blank_500.jpg')

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))

cv2.rectangle(img, (17, 17), (69, 74), (0, 255, 0), 10)

cv2.rectangle(img, (80, 90), (200, 240), (0, 0, 255), -1)
# 두께를 적는곳에 -1을 써버리면 사각형이 아예 다 해당 색깔로 채워진다.

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



