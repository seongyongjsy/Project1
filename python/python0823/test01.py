# 위치 전용 인수(positional-only-argument)
# 키워드 전용 인수(keyword-only-argument)
from unittest import result


def hello(a, /, b, *, c):
    # a : 위치 전용 인수
    # b : 일반 인수(위치 인수or 키워드 인수 모두 사용가능)
    # c : 키워드 전용 인수 - 키워드 인수로만 사용 가능
    print(f"{a=}, {b=}, {c=}")

# hello(10, 20, 30) # c를 키워드 인수로 사용하지 않았기 때문에 오류
hello(10, 20, c = 30)
hello(10, b=20, c = 30)
# hello(a= 10, b= 20, c = 30) # a를 위치 인수로 사용하지 않았기 때문에 오류

def calc(*nums, op="+"): # 가변 인수 뒤에 작성된 인수는 키워드 전용 인수 취급
    print(nums, op) 
calc(10, 20, 30, "-") #"-"는 nums 가변인수에 전달됨
calc(10, 20, 30, op = "-") 

print("-" * 30)

# 람다 표현식(lambda expression), 람다 함수
# def double(x):
#     return x*2
double = lambda x: x*2
print(double(10))
print(double(20))

num_list = [10, 15, 20, 25, 30]
print(list(map(lambda x: x*10, num_list)))  # num_list 의 모든 요소에 대해 *10 적용
print(list(filter(lambda x: x>20, num_list)))   # 20초과의 요소만 선택하기
print(list(filter(lambda x: x<20, num_list)))   # 20 미만의 요소만 선택하기
print(list(filter(lambda x: x%2==0, num_list))) # 짝수만 선별하기
print(list(filter(lambda x: x%2!=0, num_list))) # 홀수만 선별하기

# 람다 함수 예제 - 소수 구하기
num_list = list(range(2,30))
print(list(filter(lambda x: all(x % i !=0 for i in range(2, x)), num_list)))

result_list = []
for x in num_list:
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        result_list.append(x)
print(result_list)