import cv2
import numpy as np
import socket
import time
import subprocess

# IoT 디바이스 -> 엣지 컴퓨터 실시간 영상 전송

# 서버의 IP 주소와 포트 번호
server_ip = '192.168.0.109'  # 모든 네트워크 인터페이스에서 연결을 수락
server_port = 8080

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 소켓 바인딩
server_socket.bind((server_ip, server_port))

# 클라이언트 연결 대기
server_socket.listen(1)

# 파일 저장을 위한 변수 초기화
file_index = 1
folder_path = "/home/root1/Desktop/videos/"  # 저장할 폴더 경로
file_prefix = "video"  # 저장할 파일 접두사

while True:
    print("클라이언트 연결 대기 중...")

    # 클라이언트 수락
    client_socket, client_address = server_socket.accept()
    print("클라이언트가 연결되었습니다:", client_address)

    # 프레임을 저장할 비디오 라이터 생성
    video_writer = None
    frame_count = 0
    start_time = time.time()

    # 파일 경로 저장
    video_path = folder_path + file_prefix + str(file_index) + ".mp4"
    with open("filename.txt", "w") as f:
        f.write(video_path)

    while True:
        # 데이터 길이 수신
        data_len = client_socket.recv(4)
        if not data_len:
            break

        # 이미지 데이터 수신
        data_len = int.from_bytes(data_len, 'big')
        data = b''
        while len(data) < data_len:
            packet = client_socket.recv(data_len - len(data))
            if not packet:
                break
            data += packet

        if not data:
            break

        # 이미지 디코딩
        nparr = np.frombuffer(data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # 비디오 라이터 생성 및 프레임 저장
        if video_writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_writer = cv2.VideoWriter(video_path, fourcc, 20.0, frame.shape[1::-1])

        video_writer.write(frame)
        frame_count += 1

        # 1분마다 파일 닫고 새로운 파일 생성
        elapsed_time = time.time() - start_time
        if elapsed_time >= 60:  # 1분 = 60
            video_writer.release()
            video_writer = None
            frame_count = 0
            start_time = time.time()

            # test.py 실행
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'python3 video_processing.py'], shell=False)

            # 10초 후에 ai_movement.py 실행
            time.sleep(10)
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'python3 openpifpaf_processing.py'], shell=False)

    # 클라이언트 소켓 닫기
    client_socket.close()

    # 남은 프레임 저장
    if video_writer is not None:
        video_writer.release()

    # 파일 인덱스 증가
    file_index += 1

# 서버 소켓 닫기
server_socket.close()
