import cv2
import numpy as np
import sys

src = cv2.imread('./8/ronaldo1.jpg')

# 사각형 지정을 통한 초기 분할

# 마스크
mask = np.zeros(src.shape[:2], np.uint8)

# 배경 Background
bgdModel = np.zeros((1, 65), np.float64)

# 전경 Foreground
fgdModel = np.zeros((1, 65), np.float64)

# (1, 65) 두 자리, np.float64

# 배경모델, 전경모델 만들고 얘네를 계속 업데이트하는 방식으로 프로그램 동작

# 사각형 영역 지정해서 초기화
rc = cv2.selectROI(src)

cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
# cv2.GC_INIT_WITH_RECT
# 사각형 내가 지정할테니까 그 사각형 가지고 업데이트해라

# 0 : cv2.GC_BGD
# 2 : cv2.GC_PR_BGD

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')

dst = src * mask2[:, :, np.newaxis]

# 초기 분할 결과 출력
cv2.imshow('dst', dst)

# 왼쪽 버튼을 눌렀을 때는 Foreground를 등록하겠다
# 오른쪽 버튼을 눌렀을 때는 Background를 등록하겠다

# 마우스 무브 : 왼쪽 버튼 - Foreground - 파란색
# 마우스 무브 : 오른쪽 버튼 - Background - 빨간색

# 마우스 이벤트 처리 함수 등록
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(dst, (x, y), 3, (255, 0, 0), -1)
        cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1)
        cv2.imshow('dst', dst)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(dst, (x, y), 3, (0, 0, 255), -1)
        cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1)
        cv2.imshow('dst', dst)
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x, y), 3, (255, 0, 0), -1)
            cv2.circle(mask, (x, y), 3, cv2.GC_FGD, -1)
            cv2.imshow('dst', dst)
        elif flags & cv2.EVENT_FLAG_RBUTTON:
            cv2.circle(dst, (x, y), 3, (0, 0, 255), -1)
            cv2.circle(mask, (x, y), 3, cv2.GC_BGD, -1)
            cv2.imshow('dst', dst)


cv2.setMouseCallback('dst', on_mouse)
# 마우스 이벤트 받기 위해서 이 함수를 추가

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER
        # 사용자가 지정한 전경/배경 정보를 활용하여 영상 분할
        cv2.grabCut(src, mask, rc, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        dst = src * mask2[:, :, np.newaxis]
        cv2.imshow('dst', dst)
    elif key == 27:
        break

cv2.destroyAllWindows()


