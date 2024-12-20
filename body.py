import cv2 
import mediapipe as mp 
import time 

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# cap = cv2.VideoCapture('computer vision/files/1.mp4')
cap = cv2.VideoCapture(0)
ptime = 0 
target_width, target_height = 840, 480
while True :
    success , frame = cap.read()
    img = cv2.resize(frame, (target_width, target_height))

    imgRgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRgb)
    print(results.pose_landmarks)
    if results.pose_landmarks :
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime - ptime)
    ptime = cTime
    cv2.putText(img , str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,0),3)

    cv2.imshow('nigga',img)
    if cv2.waitKey(1) == ord('q'):
        break

