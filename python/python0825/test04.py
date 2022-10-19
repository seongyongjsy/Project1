# eval("코드"): 코드를 평가하는 함수
# 문자열 형태로 코드를 입력받아서 코드가 올바른 문법으로 작성되어 있으면 실행해줌
print(eval("10 + 20"))
eval("print(10+20)")
a = 10
# eval("a = 30")    # eval() 함수는 함수의 값을 변경하는 건 불가능
eval("print(a+20)") 

# exec("코드"): 코드를 실행하는 함수
exec("a = 30")  # exec() 함수는 변수의 값을 변경하는 게 가능
exec("print(a+20)")

# repr(값): 값을 표현해주는 함수
# print(repr([1, 2, 3]))
num_list = [1, 2, 3]
num_str = repr(num_list)    # 코드(목록)을 문자열로 표현
print(num_str, type(num_str)) # class str
num_result = eval(num_str)  # 문자열을 코드(목록)로 표현
print(num_result, type(num_result)) # class list

print(eval("hello"))    # print(hello) => hello 변수를 호출하는 코드로 인식
print(eval("'hello'"))  # print('hello') => 'hello' 문자열을 출력하는 코드로 인식
print(repr("hello"))    # 문자열을 입력하면 따옴표를 추가해줌 => eval() 함수와 연계 가능

