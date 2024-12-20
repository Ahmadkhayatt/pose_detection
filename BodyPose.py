import cv2 
import mediapipe as mp 
import time 

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('computer vision/files/2.mp4')
# cap = cv2.VideoCapture(0)
ptime = 0 
target_width, target_height = 480,840

# Dictionary to map landmark indices to body part names
pose_landmark_names = {
    0: "Nose", 11: "Left Shoulder", 12: "Right Shoulder",
    13: "Left Elbow", 14: "Right Elbow", 15: "Left Wrist", 16: "Right Wrist",
    23: "Left Hip", 24: "Right Hip", 25: "Left Knee", 26: "Right Knee",
    27: "Left Ankle", 28: "Right Ankle"
}

while True:
    success, frame = cap.read()
    if not success:
        break

    img = cv2.resize(frame, (target_width, target_height))
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRgb)

    # Check for pose landmarks
    if results.pose_landmarks:
        # Draw pose landmarks
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        # Loop through specific landmarks
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            if idx in pose_landmark_names:
                # Get the landmark coordinates
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                
                # Get body part name
                body_part = pose_landmark_names[idx]

                # Draw the body part name and coordinates on the frame
                cv2.putText(img, f"{body_part}: ({cx}, {cy})", (cx, cy - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - ptime)
    ptime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Pose Tracking', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
