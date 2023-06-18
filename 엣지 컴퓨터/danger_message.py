import socket
from datetime import datetime
from twilio.rest import Client

HOST = '192.168.0.109'  # !!!호스트, 포트 번호 바꿔야함.
PORT = 9999

# Twilio 계정 정보
twilio_account_sid = 'AC171e017bd0b081d8d75b4c3fd2a320cd'
twilio_auth_token = 'e9793eaade598909a28cae321e1deba4'
twilio_phone_number = '+12542563792'
target_phone_number = '+82 10 5675 3371'

# Twilio 클라이언트 생성
client = Client(twilio_account_sid, twilio_auth_token)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

    while True:
        data = client_socket.recv(1024)
        received_data = data.decode()
        print('수신한 데이터:', received_data + " " + str(datetime.today()))

        if not data:
            break

        if received_data == 'falldown':
            message = client.messages.create(
                body='Falldown detected!',  # 전송할 메시지 내용
                from_=twilio_phone_number,  # Twilio에서 발급받은 전화번호
                to=target_phone_number  # 메시지를 받을 전화번호
            )

            print('메시지 전송 완료:', message.sid)

    client_socket.close()

