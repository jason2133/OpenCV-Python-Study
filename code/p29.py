import cv2

video_file = '../video/teslafsd.mp4'
# 동영상 파일 불러오고

cap = cv2.VideoCapture(video_file)
# 비디오 파일 - 비디오 캡처 딱 한다

if cap.isOpened():
    while True:
        ret, img = cap.read()
        # 캡처 읽는다
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
            # 25ms의 지연시간 사용
            # 지연시간 = 1000 / fps
            # 25 = 1000 / 40
            # FPS - Frames Per Second : 초당 프레임 수
            # 보통 동영상 파일은 40fps인 경우가 가장 많다.

        else:
            break
        
else:
    print('cant open video')

cap.release()
# 캡처 자원 반납

cv2.destroyAllWindows()

