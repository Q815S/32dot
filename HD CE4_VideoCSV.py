import cv2, csv, mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.2)
video_path = 'C:\\Users\\user\\Downloads\\GEPEV.mp4'

cap = cv2.VideoCapture(video_path)

csv_file = open('GEPEV.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Frame', 'X', 'Y', 'Visibility'])
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print('저장되었어요. csv 파일이 정상적으로 저장되었는지 확인해주세요.')
        break
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        landmarks = []
        for idx, landmark in enumerate(results.pose_landmarks.landmark):
            landmarks.append([idx, landmark.x, landmark.y, landmark.visibility])
            csv_writer.writerow([frame_count, idx, landmark.x, landmark.y, landmark.visibility])
        frame_count += 1
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Pose LandMark', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

csv_file.close()
cap.release()
cv2.destroyAllWindows()