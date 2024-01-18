import cv2

# 녹화 시작 및 종료를 위한 상태 변환
recording = True

# mqtt_sub.py에서 녹화 종료를 위한 코드
def stop_recording(pid):
    global recording
    recording = False

# mqtt_sub.py에서 녹화 시작을 위한 코드
def start_recording():
    global recording
    recording = True
    
# True가 노트북 기준 오른쪽
def run(status: bool):
    if recording:
        if status:
            capGoalLine = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.11:554/stream1/out.h265")
            capLeft = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.12:554/stream1/out.h265")
            capRight = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.13:554/stream1/out.h265")
        else:
            capGoalLine = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.14:554/stream1/out.h265")
            capLeft = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.15:554/stream1/out.h265")
            capRight = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.16:554/stream1/out.h265")
    
        if(capGoalLine.isOpened()):
            print("GoalLine OK")
        if(capLeft.isOpened()):
            print("Left OK")
        if(capRight.isOpened()):
            print("Right OK")
    
        fourcc = cv2.VideoWriter_fourcc(*'X264')  # 비디오 코덱 설정
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        goalLineWidth = capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH)
        goalLineHeight = capGoalLine.get(cv2.CAP_PROP_FRAME_HEIGHT)
        goalLineFps= capGoalLine.get(cv2.CAP_PROP_FPS)

        camWidth = capLeft.get(cv2.CAP_PROP_FRAME_WIDTH)
        camHeight = capLeft.get(cv2.CAP_PROP_FRAME_HEIGHT)
        camFps = capLeft.get(cv2.CAP_PROP_FPS)

        print("capGoalLine: ", capGoalLine.get(cv2.CAP_PROP_FPS), ", ", capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capGoalLine.get(cv2. CAP_PROP_FRAME_HEIGHT))
        print("capLeft: ", capLeft.get(cv2.CAP_PROP_FPS), ", ", capLeft.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capLeft.get(cv2.   CAP_PROP_FRAME_HEIGHT))
        print("capRight: ", capRight.get(cv2.CAP_PROP_FPS), ", ", capRight.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capRight.get(cv2.       CAP_PROP_FRAME_HEIGHT))
    
        # 비디오 생성 객체
        # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
        if status: 
            outGoalLine = cv2.VideoWriter('leftOutput/goalline.mp4', fourcc, goalLineFps, (int(goalLineWidth), int(goalLineHeight)))     
            outLeft = cv2.VideoWriter('leftOutput/left.mp4', fourcc, camFps, (int(camWidth), int(camHeight))) # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
            outRight = cv2.VideoWriter('leftOutput/right.mp4', fourcc, camFps, (int(camWidth), int(camHeight)))
        else:  
            outGoalLine = cv2.VideoWriter('rightOutput/goalline.mp4', fourcc, goalLineFps, (int(goalLineWidth), int(goalLineHeight)))     
            outLeft = cv2.VideoWriter('rightOutput/left.mp4', fourcc, camFps, (int(camWidth), int(camHeight))) # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
            outRight = cv2.VideoWriter('rightOutput/right.mp4', fourcc, camFps, (int(camWidth), int(camHeight)))
    
    
        while True:
            # 프레임을 읽어옵니다.
            goalLineRet, goalLineFrame = capGoalLine.read()
            leftRet, leftFrame = capLeft.read()
            RightRet, RightFrame = capRight.read()
            print(goalLineRet, ", ", leftRet, ", ", RightRet)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 루프를 종료합니다.
                break
            if not goalLineRet:
                print("Failed GoalLine.")
                break
            if not leftRet:
                print("Failed left.")
                break
            if not RightRet:
                print("Failed right.")
                break
            # stop_recording() 을 통해 recording이 False가 되면 종료
            if not recording:
                print("record.py: stop")
                cv2.destroyAllWindows()  # 모든 이미지 창을 닫습니다.
                break
            
            # 프레임을 화면에 표시합니다, 나중에 삭제 가능
            cv2.imshow('GoalLineCam Recording', goalLineFrame)
            cv2.imshow('LeftCam Recording', leftFrame)
            cv2.imshow('RightCam Recording', RightFrame)
            # 프레임을 녹화 파일에 추가합니다.
            outGoalLine.write(goalLineFrame)
            outLeft.write(leftFrame)
            outRight.write(RightFrame)
    
        outGoalLine.release()
        outLeft.release()
        outRight.release()
        capGoalLine.release()
        capLeft.release()
        capRight.release()
