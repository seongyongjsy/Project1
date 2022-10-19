# 위치 인수(positional argument): 키워드 인수가 아닌 인수, 함수 호출 시 값을 바로 전달할 때
# 키워드 인수(keyword argument): 이름을 붙여서 전달하는 인수
from ast import operator
from cgitb import reset
from unittest import result


def hello(a , b): 
    print(f"{a=}, {b=}")

hello(10, 20) # 위치 인수 2개 전달
hello(a=100, b=200) # 키워드 인수 2개 전달
hello(b = 200, a = 100) # 키워드 인수 2개 순서 바꿔서 전달
hello(1000, b=2000) # 위치 인수와 키워드 인수 혼용 가능
# hello(b=2000, 1000) # 위치 인수는 반드시 키워드 인수 앞에 작성해야 함 

# print("hello", "world", sep="~", end = "!")

print("="*30)

# 인수의 기본값: 함수를 정의할 때, 인수에 대해 기본 값 설정 가능
def echo(something="Did you say anything?"):
    print(something)

# def echo(something):
#     if something is not None:
#         print(something)
#     else:
#         print("Did you say anything?")

echo("hello?")
echo()

print("=" * 30)

# 가변 인수: 인수를 가변 개수 받을 수 있도록 설정하는 문법
# print(10, 20, 30)
def calc(*nums): # 가변 인수는 1개만 작성 가능
    result = 0
    for num in nums: # 가변 인수는 함수 본문에서 목록(list)처럼 다룰 수 있음
        result += num
    return result

print(calc(10, 0))
print(calc(10, 20))
print(calc(10, 20, 30))

# def print(*values, sep="", end = "\n"):
#     pass

print ("-"*30)

# 키워드 가변 인수: 키워드 인수를 가변 개수 입력받기 위한 문법
def calc(*nums, **op): # 키워드 가변 인수는 맨 뒤에 1개만 작성 가능
    result=0
    if op["operator"] == "+":   # 키워드 가변 인수는 함수 본문에서 사전(dict)처럼 다룰 수 있음
        for num in nums:
            result += num
    elif op["operator"] == "-":
        for num in nums:
            result -= num
    else:
        pass
    if op.get("setting") == "half":
        result /= 2
    elif op.get("setting") =="double":
        result *= 2
    else:
        pass
    return result

print(calc(10, 20, operator="+"))
print(calc(10, 20, operator= "-"))
print(calc(10, 20, 30, operator="+", setting="half"))
print(calc(10, 20, 30, operator="-", setting="double"))

print("=" * 30)

# docstring: 일종의 도움말, 함수 사용 방법(지침)을 함수에 기록하는 문법
def hi():
    """docstring 테스트용 함수입니다.""" # 함수 본문 블록 첫 번째 줄에 문자열로 작성
    pass

help(hi)
print(hi.__doc__)