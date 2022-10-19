#반복문
#일정 횟수만큼 또는 조건식을 만족하는 동안 블록을 반복 실행하는 문장

#1.while
# 조건식을 만족하는 동안 반복하는 문장
# num = 0
# while num < 10:
#       print(num)
#       num += 1

# while 예제1
# num = 10
# while num != 0:
#     print(num)
#     num -= 1

# while문 예제1 - 1 이상 100 이하의 숫자 중 짝수만 출력.
# num = 0
# while num < 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# while문 예제2 - 200 이상 300 이하의 숫자 중 3의 배수만 출력
# num = 200
# while  num <= 300:
#     if num % 3 == 0:
#         print(num)
#     num += 1

# while문 예제 3 - 구구단 출력
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# ...
# 3 * 1 = 3 
# 3 * 2 = 6
# ...
# 9 * 9 = 81

i = 2 # 단수
j = 1 # 곱하는 수
 
while i <= 9: # 중첩(이중)반복문
    while j <= 9:
        print(i, "*", j, "=", i*j, end = " / ")
        j +=1
        if j % 3 == 0:
            print()
    print()
    j = 1
    i += 1