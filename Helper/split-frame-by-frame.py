import cv2
import os

video_dir = 'C:\\Users\\abhay\\Downloads\\cctv_dataset\\noFight'

output_dir = 'nonfight'

os.makedirs(output_dir, exist_ok=True)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    current_frame = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Failed to capture frame from {video_path}. Exiting...")
            break


        name = f'{output_dir}/frame_{os.path.basename(video_path)}_{current_frame}.jpg'
        print(f'Creating... {name}')
        cv2.imwrite(name, frame)

        current_frame += 1

    cap.release()

for video_file in os.listdir(video_dir):
    if video_file.endswith('.mp4'):
        video_path = os.path.join(video_dir, video_file)
        process_video(video_path)
