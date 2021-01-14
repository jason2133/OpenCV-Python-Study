# OpenCV로 불러들인 이미지를 저장한다

import cv2

img_file = '../img/elonmusk_cybertruck.jpg'
# 불러오는 이미지 이름

save_file = '../img/elonmusk_cybertruck_gray.jpg'
# 저장시킬 이미지 이름

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# 이미지 파일을 읽어내고, 이걸 흑백으로 읽어낸다

cv2.imshow(img_file, img)
# 이미지 파일 보여줘요

cv2.imwrite(save_file, img)
# 저장시켜줘요

cv2.waitKey()
# 키보드 입력 있을 때까지 기다려요

cv2.destroyAllWindows()
# 만약에 입력 있으면 윈도우 창 닫아요


