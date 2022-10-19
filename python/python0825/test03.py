# 일급 함수(First-class function)
# 일급 시민(First-class citizen)
# 함수를 값처럼 다룰 수 있으면 일급 함수를 지원한다고 표현함
from turtle import position


a = 10
b = 3.14
c = "hello"
def hi():
    print("hi")
d = hi  # 함수도 여타 다른 값처럼 변수에 저장 가능
print(d, type(d))   # function 자료형
d()     # 변수를 실행하면 변수에 저장된 함수가 실행됨

def execute_function(other_function):
    other_function()
execute_function(hi)  # 함수를 인수로 전달 가능

print("-" * 30)

# 클로저(Closure): 일급 함수 분법을 응용한 코드 작성 방법
# 내부 함수의 상태를 저장해서 외부에서 사용하기 위함
def outer():
    def inner():
        return 10
    return inner    # 외부 함수에서 내부 함수를 값처럼 통째로 반환
inner_func = outer()
print(inner_func())

def set_x(x):
    def set_y(y):
        return(x,y)
    return set_y

# temp = set_x(10)
# position = temp(20)
position = set_x(10)(20)
print(position)



