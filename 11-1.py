import numpy as np
import cv2

# 트랙바
def on_k_changed(pos):
    global k_value

    k_value = pos

    if k_value < 1:
        k_value = 1

    trainAndDisplay()

# 애드포인트 - 헬퍼 함수
def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])

# 훈련 및 보여주기
def trainAndDisplay():
    trainData = np.array(train, dtype=np.float32)
    labelData = np.array(label, dtype=np.int32)

    knn.train(trainData, cv2.ml.ROW_SAMPLE, labelData)

    h, w = img.shape[:2]

    for y in range(h):
        for x in range(w):
            sample = np.array([[x, y]]).astype(np.float32)

            ret, _, _, _ = knn.findNearest(sample, k_value)
            ret = int(ret)

            if ret == 0:
                img[y, x] = (128, 128, 255)
            
            elif ret == 1:
                img[y, x] = (128, 255, 128)
            
            elif ret == 2:
                img[y, x] = (255, 128, 128)



