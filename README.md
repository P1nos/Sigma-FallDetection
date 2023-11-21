# 고령자 AI 상황인식시스템
------------

## 프로젝트 연구배경
+ 독거노인의 수는 계속 증가하고 있으며, 요양보호사 수는 턱없이 부족한 것이 사회적 문제

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/94a698a0-5e69-4c6a-ac55-0c27fd5f2f00)

출처 : 통계청 - 「장래가구추계 2017」, 「장래인구추계 2020」 2022

------------

## 프로젝트 필요성
+ 독거 노인이 계속 증가하고 있으므로 독거 노인을 관리하는 스마트 노인 관리 시스템이 필요함

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/33923ed2-5f3c-431b-a52b-04990c609f26)

------------

## 프로젝트 목표
+ 독거 노인의 안전, 이상, 경고, 위험을 판단하는 상황인식 시스템을 만드는 것

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/33923ed2-5f3c-431b-a52b-04990c609f26)

------------

## 프로젝트 현실적 제한 요소

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/6abc1b29-857e-408e-8cb6-0b6abb5d113b)


------------

## 프로젝트 세부 시스템 구조 (IoT 디바이스)
+ 카메라를 이용하여 실시간 동영상 전송

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/f0bf6deb-97d1-4c18-af3c-59144be52b1f)

------------

## 프로젝트 세부 시스템 구조 (엣지 컴퓨터)
+ IoT 디바이스의 실시간 영상 정보를 전처리, 낙상 분석 인공지능 소프트웨어로 분석하여 분석 결과로 위험 알람 서비스 동작

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/2381d0fd-f3ef-45d6-a38b-220cd60200e9)

------------

## 프로젝트 세부 시스템 구조 (AI)
+ 낙상 판단 AI 모델 ( openpifpaf 사용)
![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/970b8c59-b1b9-40d6-8176-13df992b053f)

1. 전경을 추출
2. 연결된 구성 요소를 결정하며 데이터 전처리를 추가로 함
3. 사람의 움직임을 감지
4. 동작 데이터와 깊이 데이터를 획득한 값을 픽셀 값 목록으로 작성, 깊이 참조 이미지를 빠르게 업데이트 진행
5. 이미지 데이터가 유사한 범위를 가지도록 정규화를 진행하고 데이터는 잡음을 억제하기 위해 중간 필터링 진행
6. SVM모델을 사용하여 임계 값 처리된 차이 맵 에서 가장 큰 임계 값을 기반절차에 의해 신호화 된 fall detection을 추출

------------

## 프로젝트 세부 시스템 구조 (WEB Server)
+ 엣지컴퓨터에서 인공지능 분석 후 위험 상황 발생 확인 시 즉시 웹 서버에 이미지 전송
+ 웹 서버에서 받은 데이터인 이름, 시간, 이미지를 DB에 저장
+ 사용자가 웹 페이지에서 낙상사고 확인 가능

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/1f35e772-957a-47d6-89a4-6625fe34bf3e)

------------

## 프로젝트 실행결과

![image](https://github.com/P1nos/Sigma-FallDetection/assets/90705236/a9e7d1b3-c95d-4c5c-95fb-3663de121f44)

