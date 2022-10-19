# 2. 계산기 프로그램
# 숫자1, 연산자, 숫자2 를 차례대로 입력받아서 계산한 결과를 출력하기
# ex) 첫 번째 숫자를 입력하세요: 1.5
# 연산자를 입력하세요: *
# 두 번째 숫자를 입력하세요 : 10
# 계산 결과: 15.0

# ex) 첫 번째 숫자를 입력하세요: 27
# 연산자를 입력하세요: /
# 두 번째 숫자를 입력하세요 : 3
# 계산 결과: 9.0

from unittest import result


num1 = float(input("첫 번째 숫자를 입력하세요: "))
op = input("연산자를 입력하세요: ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

result = 0
# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     result = num1 / num2
# else:
#     print("잘못 입력하셨습니다.")

match op:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case _:
        print("잘못 입력하셨습니다.")


print("계산 결과:", result)