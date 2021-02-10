# 2개의 동영상을 이어붙임.

import cv2
import numpy as np
import matplotlib.pylab as plt
import sys

# Video 불러오기
cap1 = cv2.VideoCapture('./2/video1.mp4')
cap2 = cv2.VideoCapture('./2/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오 안열렸다 이것아')
    
# 두 동영상의 크기, FPS는 같다고 가정
# frame 대충 24 정도임
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
# 24 frame

effect_frames = int(fps * 2)
# 1번째 동영상의 끝부분 2초, 2번째 동영상의 앞부분 2초가 겹쳐져서 영상 만들어짐
# 48 frame 정도의 값을 가지게 될 것임.

print('Frame_cnt1:', frame_cnt1)
print('Frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000 / fps)
# 두 프레임 사이의 시간 간격을 계산한다.

w = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output3.avi', fourcc, fps, (w, h))

# 1번 동영상에서 뒤에 48프레임 남겨놓고
# 앞부분은 out에 그대로 저장됨.
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        break
    
    out.write(frame1)

    cv2.imshow('frame', frame1)
    cv2.waitKey(delay)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # 합성하는 과정
    dx = int(w * i / effect_frames)

    # 이 부분을 주의해서 하면 된다.
    # 컬러 영상
    # frame = np.zeros((h, w, 3), dtype = np.uint8)
    
    # # 이 부분을 잘 계산하는거 여기를 잘해야 한다.
    # frame[:, 0:dx] = frame2[:, 0:dx]
    # frame[:, dx:w] = frame1[:, dx:w]

    # 점점 흐려지면서 코끼리가 나오는 영상
    alpha = 1.0 - (i / effect_frames)
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)


    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        break
    
    out.write(frame2)

    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()


