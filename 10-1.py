import cv2
import numpy as np

# 비디오 파일 열어요

cap = cv2.VideoCapture('./10/PETS2000.avi')

# 배경영상
# 1번째 프레임을 받아서 배경으로 등록한다.
_, back = cap.read()
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
# 차영상 움직임 모션 감지이므로 굳이 칼라일 필요가 없다
# 그레이 처리를 통해 연산량 감소

back = cv2.GaussianBlur(back, (0, 0), 1)
# 가우시안 블러 먹여서 노이즈 삭제

# 2번째 프레임부터 현재 프레임으로 받아서
# 1번째 프레임 배경과 서로 비교 ㄱㄱ
while True:
    _, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame = cv2.GaussianBlur(frame, (0, 0), 1)
    # 가우시안 블러 먹여서 노이즈 삭제

    # 빼가지고 절댓값을 씌운다
    diff = cv2.absdiff(back, frame)

    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    # 1번째 값은 threshold 값이, 2번째 값은 diff값이 불려와진다

    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    
    # 30밀리세컨드 쉬고 다음꺼 보여준다
    # 중간꺼 끊을 수 있게 키보드 입력 지정 ESC
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
