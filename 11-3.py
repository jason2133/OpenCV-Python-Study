import sys
import numpy as np
import cv2


oldx, oldy = -1, -1

# 마우스 콜백 함수
# 마우스로 숫자를 입력할 것이기 때문에
# 필기체 인식이려나
def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)


# 여기부터가 실제 프로그램 시작하는 코드라고 보면 된다

# 학습 & 레이블 행렬 생성

digits = cv2.imread('./11/digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

# 가로, 세로
# 가로 1000 세로 2000
h, w = digits.shape[:2]

# 각각의 부분 영상을 짤라내는 파이썬 코드
# 50개로 분할하겠다
# 각각의 행에 대해서 나눈다

# 리스트 형태로 만들어진 cells
cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]

# ndarray로 변환
cells = np.array(cells)

# 훈련 이미지
# 5000 x 400
# float32
train_images = cells.reshape(-1, 400).astype(np.float32)

# 정답을 알려주는 행렬
# 5000행 x 1열로 구성되어 있다
# int32
train_labels = np.repeat(np.arange(10), len(train_images)/10)

# KNN 학습

knn = cv2.ml.KNearest_create()
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

# 사용자 입력 영상에 대해 예측

# 400 x 400
img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    key = cv2.waitKey()

    if key == 27:
        break

    # 스페이스바
    # 스페이스바 치면 그 그린 모습을 입력으로 받아들이겠다
    elif key == ord(' '):
        # 400 x 400을 20 x 20으로 리사이즈
        test_image = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)
        test_image = test_image.reshape(-1, 400).astype(np.float32)

        ret, _, _, _ = knn.findNearest(test_image, 5)
        print(int(ret))

        # 출력하고나서는 영상을 까만색으로 칠해준다.
        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
