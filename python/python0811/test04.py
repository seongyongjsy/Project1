# 기타 제어문 예제
#  score = 0 # 점수를 누적할 변수 선언 및 0으로 초기화
#  while True:  
#     num = int(input("득점한 점수를 입력하세요(0을 입력하면 중단합니다.): ")) # 점수를 입력받음
#     if num == 0: #0을 입력한 경우,
#         break # 반복을 중단
#     score += num #입력받은 점수를 누적
#     print("누적 점수:", score) # 현재까지 누적된 점수를 출력

# print("최종 점수:", score)

#기타 제어문 예제2
from random import random
#print(random()) # 0 이상 1 미만의 임의의 실수(난수) 1개 생성

num = int(random() * 20) + 1 #1 이상 20 이하의 임의의 실수 생성
is_correct = False #정답 맞춘 여부를 저장할 bool 변수
chance = 3 # 시도 횟수
while chance > 0: # 시도 횟수가 남아있는 동안 게임을 진행
    ans = int(input("1~20 사이의 정수 하나를 입력하세요(남은 기회:" + str(chance) + "):"))

    if num > ans:
        print("입력하신 값이 정답보다 작습니다.")
    elif num < ans:
        print("입력하신 값이 정답보다 큽니다.")
    else:
        is_correct = True
        break

    chance -= 1 #시도 횟수를 감소시킴

if is_correct:
    print("정답입니다!")
else:
    print("맞추지 못했습니다..")
    print("정답은", num)