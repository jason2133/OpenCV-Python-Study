import cv2

src = cv2.imread('./3/candies.png', cv2.IMREAD_COLOR)

print('src.shape : ', src.shape)
print('src.dtype : ', src.dtype)

b, g, r = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.waitKey(0)
cv2.destroyAllWindows()
