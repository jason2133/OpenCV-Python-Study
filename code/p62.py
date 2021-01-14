import cv2

img = cv2.imread('../img/elonmusk_a.jpg')

print(type(img))
print(img.ndim)
print(img.shape)
print(img.size)
print(img.dtype)
print(img.itemsize)
