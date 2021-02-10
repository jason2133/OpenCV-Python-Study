import cv2
import sys

print('Hello World', cv2.__version__)

img = cv2.imread('./1/cat.bmp')

if img is None:
    print('Image Load Failed')
    sys.exit()

cv2.namedWindow('first')
cv2.imshow('first', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

