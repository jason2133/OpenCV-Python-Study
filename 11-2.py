import numpy as np
import cv2

# TrackBar
def on_k_changed(pos):
    global k_value

    # k_value가 1보다 작으면 1로 정해라
    k_value = pos
    if k_value < 1:
        k_value = 1

    # 훈련하고 보여주어라
    trainAndDisplay()

# 포인트 추가해라
# train과 label 추가
def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])

# 훈련하고 보여주어라
def trainAndDisplay():
    
    # 훈련 데이터 - float Data
    trainData = np.array(train, dtype=np.float32)
    
    # 레이블 데이터 - int Data
    labelData = np.array(label, dtype=np.int32)

    # ROW_SAMPLE : 데이터 하나가 한 행으로 들어간다
    knn.train(trainData, cv2.ml.ROW_SAMPLE, labelData)

    h, w = img.shape[:2]

    # 각각의 픽셀 for loop
    for y in range(h):
        for x in range(w):
            # 각각의 점들을 이용해서 sample을 계산한다
            sample = np.array([[x, y]]).astype(np.float32)

            # findnearest를 활용해서 예측한다
            # sample과 k_value를 통해서 예측을 하고
            # 얘가 속한 클래스가 0번인지 1번인지 2번인지 예측
            ret, _, _, _ = knn.findNearest(sample, k_value)

            ret = int(ret)
            if ret == 0:
                img[y, x] = (128, 128, 255)
            elif ret == 1:
                img[y, x] = (128, 255, 128)
            elif ret == 2:
                img[y, x] = (255, 128, 128)

    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            # 빨강
            cv2.circle(img, (x, y), 5, (0, 0, 128), -1, cv2.LINE_AA)
        elif l == 1:
            # 녹색
            cv2.circle(img, (x, y), 5, (0, 128, 0), -1, cv2.LINE_AA)
        elif l == 2:
            # 파랑
            cv2.circle(img, (x, y), 5, (128, 0, 0), -1, cv2.LINE_AA)

    cv2.imshow('knn', img)


# 학습 데이터 & 레이블
train = []
label = []

# k값
k_value = 1

# 이미지
img = np.full((500, 500, 3), 255, np.uint8)

# KNN 객체
knn = cv2.ml.KNearest_create()

# 랜덤 데이터 생성
NUM = 30
rn = np.zeros((NUM, 2), np.int32)

# (150, 150) 근방의 점은 0번 클래스로 설정
cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 150, rn[i, 1] + 150, 0)

# (350, 150) 근방의 점은 1번 클래스로 설정
# 랜덤 숫자 생성
# 평균 0이고, 표준편차 50인 형태
cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 350, rn[i, 1] + 150, 1)
    # x 좌표, y 좌표, 이 점의 클래스

# (250, 400) 근방의 점은 2번 클래스로 설정
cv2.randn(rn, 0, 70)
for i in range(NUM):
    addPoint(rn[i, 0] + 250, rn[i, 1] + 400, 2)

# 영상 출력 창 생성 & 트랙바 생성
cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', 1, 5, on_k_changed)

# KNN 결과 출력
trainAndDisplay()
# KNN 학습을 하고 그 모습을 보여준다.

cv2.waitKey()
cv2.destroyAllWindows()




