# 동영상 처리 예제

import cv2
import numpy as np
import matplotlib.pylab as plt

cap = cv2.VideoCapture('./2/video1.mp4')

fps = round(cap.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)

while True:
    ret, frame = cap.read()
    # ret은 True / False 여부를 나타내고,
    # frame은 말그대로 동영상 프레임을 가져온다

    inversed = ~frame
    # 역으로 ㄱㄱ

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(0) == 27:
        break
    
    # ESC 누르면 끝!
    
    cap.release()
    cv2.destroyAllWindows()

