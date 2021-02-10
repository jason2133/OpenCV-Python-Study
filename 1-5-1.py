import sys
import cv2

img1 = cv2.imread('./1/images/road_marking_evening_clouds_horizon_120298_1920x1080.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('./1/images/road_marking_evening_clouds_horizon_120298_1920x1080.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image1')
cv2.namedWindow('image2')

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)

cv2.waitKey()

cv2.destroyAllWindows()
