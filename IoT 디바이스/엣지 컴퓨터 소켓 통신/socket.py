import cv2
import numpy as np
import socket

# IoT 디바이스 -> 엣지 컴퓨터 실시간 영상 전송

# 서버의 IP 주소와 포트 번호
server_ip = '192.168.109.243'
server_port = 8080

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((server_ip, server_port))

# 카메라 초기화
camera = cv2.VideoCapture(0)  # 카메라 장치 번호 (일반적으로 0)

while True:
    # 프레임 읽기
    ret, frame = camera.read()

    # 프레임 크기 변경 (선택 사항)
    # frame = cv2.resize(frame, (640, 480))
    # 프레임 인코딩
    _, img_encoded = cv2.imencode('.jpg', frame)
    data = np.array(img_encoded).tobytes()

    # 데이터 전송
    try:
        client_socket.sendall(len(data).to_bytes(4, 'big'))  # 데이터 길이 전송
        client_socket.sendall(data)  # 이미지 데이터 전송
    except socket.error as e:
        print("전송 오류:", e)
        break

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 클라이언트 소켓 닫기
client_socket.close()

# 카메라 해제
camera.release()
cv2.destroyAllWindows()