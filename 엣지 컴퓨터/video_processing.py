
import cv2

def read_video_filename(filename_file):
    with open(filename_file, 'r') as f:
        video_filename = f.read().strip()
    return video_filename

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps * 2, (int(cap.get(3)), int(cap.get(4))))

    skip_frames = 4

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video', frame)
        out.write(frame)

        for _ in range(skip_frames):
            cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# 파일에서 동영상 파일 이름 읽어오기
filename_file = 'filename.txt'  # 동영상 파일 이름이 저장된 파일 경로
video_filename = read_video_filename(filename_file)
print("Received video filename:", video_filename)

# 동영상 파일 열기
output_path = '/home/root1/Desktop/videos_Preprocessor/videos.mp4'
process_video(video_filename, output_path)


