# OpenCV를 통해 이미지 파일 읽기

import cv2

img_file = "../img/elonmusk_cybertruck.jpg"
img = cv2.imread(img_file)
# cv2.imread : 이미지를 읽는다, img read
# 기본값은 cv2.IMREAD_COLOR : RGB로 읽는다

if img is not None:
    # 이미지가 비어 있는게 아니라면

    cv2.imshow('Elon Original', img)
    # Elon Original 이름으로 img 파일을 보여주어라

    cv2.waitKey()
    # 키가 입력될 때까지 대기해라
    # waitKey 함수는 키보드의 입력이 있을 때까지 프로그램을 기다리게 한다.

    cv2.destroyAllWindows()
    # 창을 모두 닫아라
    # 키가 입력되면 표시한 창을 모두 닫고 나서 프로그램을 종료한다.

else:
    print('No Image File')
    # 아니면 이미지 파일 없는거다


