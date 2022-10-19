# 표준 모듈(Standard module): 파이썬에서 기본적으로 제공하는 모듈
# 라이브러리(Library) : 모듈들, 모듈의 집합
#   보통 다른 프로그래밍 언어에서는,
#   미리 만들어둔 도구의 성격을 지닌 기능들을 일컫는다. 
# 표준 라이브러리(Standard library): 표준 모듈의 집합

# math 모듈: 수학과 관련된 각종 다양한 상수와 함수들을 제공하는 모듈
# 상수(constant): 변수 중에서 값이 고정되어 변하지 않는 변수
import math
print("원주율:", math.pi)
print("자연 상수:", math.e)
# NumPy, Pandas: 파이썬 기초 데이터 분석 라이브러리
print("무한대", math.inf, type(math.inf))
print("숫자가 아님(nan)", math.nan, type(math.nan))
print(2 ** 3, math.pow(2, 3))
print(math.sqrt(4))
print(math.ceil(3.5), math.floor(3.5))
print(math.degrees(3.14), math.radians(180))
print(math.sin(3.14), math.cos(3.14), math.tan(3.14))

print("\n", "=" * 50, "\n")

# statisics 모듈
num_list = [3, 10 ,25]
total = 0
for num in num_list:
    total += num
avg = total / len(num_list)
print(avg)
from statistics import mean
print(mean(num_list))

print("\n", "=" * 50, "\n")

# random 모듈
import random
print(random.random())  # 0 이상 1 미만의 임의의 실수 1개 생성
# 1 이상 20 이하의 임의의 정수 만들기
for _ in range(10):
    # print(int(random.random()* 6) + 1)
    # print(random.randint(1, 6)) # a 이상 b이하의 임의의 정수 1개 생성
    print(random.randrange(1, 6, 2))  # range 범위에서 임의의 정수 1개 생성
menu_list = ["김밥", "라면", "만두"]
random.shuffle(menu_list) # 목록의 요소의 순서를 섞는 함수
print(menu_list)
print(random.sample(menu_list, 3))
print("오늘의 메뉴는?" , random.choice(menu_list)) # 시퀀스에서 임의의 요소 1개 추출
