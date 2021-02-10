import cv2
import numpy as np
import sys

# 영상 불러오기
obj = cv2.imread('./8/spades.png', cv2.IMREAD_GRAYSCALE)

# 객체가 검은색이고, 배경이 흰색이기 때문에
# 이 영상을 사용하고자 한다면
# 이 영상을 반전시켜서 사용해야 한다. (흰백 색깔 변경)
src = cv2.imread('./8/symbols.png', cv2.IMREAD_GRAYSCALE)


# 객체 영상 외곽선 검출
# 객체를 반전해서 이진화를 한다
# 그래서 cv2.THRESH_BINARY_INV를 사용함
# 그걸 obj_bin 사용
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)

# cv2.findContours로 외곽선 검출
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 이 변수에다가 외곽선 지정
obj_pts = obj_contours[0]

# 입력 영상 분석
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)

# 모든 객체의 정보를 contours에다가 지정한다
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# 결과 영상
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서

# contours는 각각의 점들의 집합 pts 하는걸 받는다

# pts는 객체 하나의 외곽선 정보
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue
    # 노이즈를 제거하는 의미

    # 바운딩 렉트 그려놓고
    rc = cv2.boundingRect(pts)
    cv2.rectangle(dst, rc, (255, 0, 0), 1)

    # 모양 비교
    # matchShapes를 사용해서 2개의 외곽선을 이용해서
    # 2개가 비슷한지 다른지를 판별한다
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)
    # cv2.CONTOURS_MATCH_I3 이용해서 비교, dist 거리 출력

    # dist 값을 각각의 객체 위에다가 출력 (소수점 4자리에서 반올림)
    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

    if dist < 0.1:
        cv2.rectangle(dst, rc, (0, 0, 255), 2)
    # dist가 0.1보다 작으면 빨간색 사각형으로 그린다
    # 그게 제일 유사한 객체니까

cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



