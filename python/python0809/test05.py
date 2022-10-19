# 산술 연산자(+, -, *, **, /, //, %)
# print(2 ** 3) # 거듭 제곱 연산자
# print(9 ** 0.5)

# print(10 / 30) # 나누기 연산자
# print(10 // 3) # 몫 구하기 연산자
# print( 10 % 3) # 나머지 구하기 연산자

# 증분(복합) 대입 연산자(+=, -=, *=, **=, /=, //=, %=)

#비교 연산자( >, <, >=, <=, ==, !=)
# print(10>3) #True
# print(10 < 10) # False
# print(10 >= 10) #True
# print(10 <= 1) # False

# a= 10
# b= 10 -1
# print (a == b) # False
# print( a!= b) # True


#관계 연산자(and, or, not)\
# and : 둘 다 True 면 결과도 True, 둘 중 하나라도 False면 결과도 False
print(True and True) #True
print(True and False) # False
print( False and True) # False
print (False and False) # False

#or: 둘 다 False면 결과도 False, 둘 중 하나라도 True면 결과도 True
# print(True or True) # True
# print(True or False) # True
# print(False or True ) # True
# print(False or False) # False

# age = 10
# height = 150.0

# if age > 10 and height > 150.0:
#     print("놀이기구 탑승이 가능합니다.") # if True인 경우 실행할 코드
# else:
#     print("놀이기구 탑승이 불가능합니다.") # if False인 경우 실행할 코드

# kor_score = 91
# eng_score = 89

# if kor_score > 90 or eng_score > 90:
#     print("용돈 올려줄게")
# else:
#     print("공부 더 열심히 하렴.")
#print(not True) #False
#print(not False) #True

time_now = 12
if time_now > 10:
    print("언제 들어와")
