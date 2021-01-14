# FPS를 지정하여 동영상 재생
# video_play_fps

import cv2

video_file = '../video/teslafsd.mp4'

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    # FPS : Frame Per Seconds : 초당 프레임 구하기

    delay = int(1000 / fps)
    # 지연시간 = 1000 / FPS 로 구하면 된다.

    print('FPS: %f, Delay: %d ms' % (fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        
        else:
            break
        
else:
    print('cant open video')

cap.release()
cv2.destroyAllWindows()



