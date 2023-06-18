# 베이스 이미지 설정
FROM python:3.7.6

# 작업 디렉토리 생성 및 코드 복사
WORKDIR . .
COPY . .

RUN apt-get update -y

# 필요한 패키지 설치
RUN pip install torch==1.7.1

RUN pip3 install openpifpaf

RUN pip install -r requirements.txt

# 컨테이너 실행 시 실행할 명령어 설정
CMD [ "python", "testxml2.py" ]

