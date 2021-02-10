import cv2
import numpy as np
import sys

src = cv2.imread('./8/nemo.jpg')

# 영상에서 니모 물고기 부분을 자동으로 분할

rc = cv2.selectROI(src)
# 관심 영역을 지정하는데

mask = np.zeros(src.shape[:2], np.uint8)
# 0 - 검정색으로 채워져 있다!
# 마스크는 모두 0으로, 검정색으로 채운다.

# 그랩컷 garbCut 함수

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)
# None, None : Background Model과 Foreground Model 일단 여기서는 안줘도 됨.
# 내부에서 5번의 Iteration -> 그 결과로 출력을 주어라

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
# probably background 또는 background : 얘네는 0으로 세팅
# foreground는 1로 세팅

# mask2는 0 또는 1로 구성되어 있는 행렬이니라

dst = src * mask2[:, :, np.newaxis]
# mask2 width, height 모두, np.newaxis 새로운 축으로 ㄱㄱ

# 마스크 결과 보고 싶으면은
mask = mask * 64

# 마스크 출력
cv2.imshow('mask', mask)
# 완전 검정이랑 회색은 Background (배경)
# 물고기 모양 문양은 Foreground (전경)

# Foreground 부분 전경만 잘려서 dst가 나온다

# 초기 분할 결과 출력
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()



