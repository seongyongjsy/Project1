# 함수(Function)
# 일련의 코드들의 묶음
# 1. 코드의 재사용성을 높임
# 2. 유지보수를 용이하게 하기 위함

# 함수 정의(define): 함수를 사용하기 위해 일련의 코드들을 작성하고 이름을 붙이는 것
def hello(): 
    print("hello")
    print("hi")
    print("bye")

hello() # 함수 호출(call): 함수의 이름을 이용해서 작성된 일련의 코드들을 실행하는 것
print('-'*30)
hello()

# 매개변수(parameter): 함수를 정의할 때 소괄호에 작성하는 변수
# 함수를 호출할 때 입력한 값을 받아서 함수 본문에서 사용할 수 있게 해줌
def calc_double(input_num):
    result = input_num * 2
    return result # 반환값(return value): 함수 실행 결과, 함수를 호출한 곳으로 되돌려줄 값

# 전이인수, 전달인자(argument) : 함수를 호출할 때 입력해줄 값
a = calc_double(10)
print(a)
print(calc_double(20))