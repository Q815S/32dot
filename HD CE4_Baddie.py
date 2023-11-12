import cv2, csv, subprocess, time, mediapipe as mp, numpy as np, tkinter as tk
from sklearn.metrics.pairwise import cosine_similarity
from screeninfo import get_monitors

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.2)
time.sleep(2)
video_path = '기지개체조.mp4'

cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

video_capture = cv2.VideoCapture(video_path)
total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

cap = cv2.VideoCapture(0)
subprocess.run(["cmd", "/c", "start", "", video_path], shell=True)

csv_file = open('cam_landmarks.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['X', 'Y', 'Visibility'])
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print('오류 발생! 카메라 시스템을 점검하십시오')
        break

    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.pose_landmarks:
        landmarks = []
        for landmark in results.pose_landmarks.landmark:
            landmarks.append([landmark.x, landmark.y, landmark.visibility])
            csv_writer.writerow([landmark.x, landmark.y, landmark.visibility])
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Pose LandMark', frame)
    frame_count += 1

    if frame_count >= total_frames:
        print('저장되었어요.')
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('사용자에 의해 임의로 중단되었어요.')
        break

csv_file.close()
cap.release()
subprocess.run(["taskkill", "/f", "/im", "Video.UI.exe"])
cv2.destroyAllWindows()

##점수 측정
file1 = 'cam_landmarks.csv'
data1 = []
with open(file1, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        data1.append([float(row[1]), float(row[2])])

file2 = '기지개체조.csv'
data2 = []
with open(file2, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        data2.append([float(row[1]), float(row[2])])

data1_array = np.array(data1)
data2_array = np.array(data2)
similarity_score = cosine_similarity(data1_array, data2_array)
similarity_percentage = ((((similarity_score[0][0] * 100)-50)**2)/25)

##새 창 띄우기
root = tk.Tk()
root.title("Ending")

second_display_width = None
second_display_height = None

monitors = get_monitors()
if len(monitors) > 1:
    second_display = monitors[1]  
    second_display_width = second_display.width
    second_display_height = second_display.height

if second_display_width and second_display_height:
    root.geometry(f'{second_display_width}x{second_display_height}+{second_display.x}+{second_display.y}')
else:
    root.geometry('800x600+0+0')

def close_after_10_seconds():
    time.sleep(10)
    root.destroy()

canvas_width = 100000
canvas_height = 100000
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill='#FEF4E8', width=0)

text_label = tk.Label(canvas, text=f'축하합니다! 점수는 {similarity_percentage:.2f}점입니다.\n\n체험이 끝났습니다.\n스태프의 안내에 따라 자리에 앉아주세요.', font=("LG Smart UI Mobile Regular", 40), bg='#FEF4E8')
text_label.place(relx=0.5, rely=0.5, anchor='center')
print(f'점수는 {similarity_percentage:.2f}점이에요.\n10초 후에 프로그램이 종료됩니다.')
root.after(10000, close_after_10_seconds)
root.mainloop()