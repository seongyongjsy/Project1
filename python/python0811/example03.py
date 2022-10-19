# 피보나치 수열
# 1 1 2 3 5 8 13 21 34 55

# num1 = 1 # 첫 번째 항
# num2 = 1 # 두 번째 항
# num3 = num1 + num2 # 세 번째 항

# i = 0
# while i < 10:
#     print(num3)

#     num1 = num2
#     num2 = num3
#     num3 = num1 + num2

#     i += 1

# 제어문 예제3 정수를 입력받아서 해당 번째 피보나치 수열을 출력하는 코드를 작성하세요.
# 정수를 입력하세요: 3 => 3번째 피보나치 수열 항의 값은 2입니다.
# 정수를 입력하세요: 10 => 10번째 피보나치 수열 항의 값은 55입니다.
# num = int(input("정수를 입력하세요"))
# ans = None
# match num:
#     case 1 | 2:
#         ans = 1
#     case _:
#         i  = 3 
#         num1 = 1
#         num2 = 1
#         while i <= num:
#             num3 = num1 + num2
#             num1 = num2 
#             num2 = num3
#             i += 1
#         ans = num3
# print(num, "번째 피보나치 수열 합의 값은", ans,"입니다.")

# 제어문 예제 3-2 - 정수를 입력받아서 해당 숫자보다 작은 피보나치 수열 항의 값을 모두 출력하세요
# num = int(input("정수를 입력하세요"))

# print("1 1 ", end=" ")

# num1 = 1
# num2 = 1
# num3 = num1 + num2
# while num3 < num:
#     print(num3, end=" ")
#     num1 = num2
#     num2 = num3
#     num3 = num1 + num2 

# 제어문 예제4 - 정수를 입력받아서 1부터 해당 숫자만큼 1씩 증가한 모든 숫자들의 합계 구하기

num = int(input("정수를 입력하세요: "))
total_value = 0
i = 0
while i < num:
    total_value += i
    i += 1
print(total_value)