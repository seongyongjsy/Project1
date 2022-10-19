# 동일성 연산자

# 동등성(Equality) vs 동일성 (Identity)

# 동등성 : 두 변수의 값이 같은지 여부
# 동일성 : 두 변수가 일치하는지 여부(=값과 자료형 모두 같은지 여부)

# 동승성 : ==, != 연산자 사용해서 검사
# 동일성 : is, is not 연산자 사용해서 검사

# 0, 0.0, '', "", '''''', """""" => False로 취급할 수 있음
# 1, -1, 0.1, 'hello', "False" => True 로 취급할 수 있음

print(0 == 0) # 값이 같은지 비교 => True
print(0 == 0.0) # 값이 같은지 비교 => True
print(0 is 0.0) # 값과 자료형 모두 같은지 비교 => False
print(0 is 0) # 값과 자료형 모두 같은지 비교 => True

print("------------------")

print(0 == False) # True
print(1 == True) # True
print(0 is not False) # True
print(1 is not False) # True

ans = 1
if ans == True:
    print("실행")

# 표현식, 식(Expression)
# 문장 중에서 계산할 수 있는 코드
# print(10 + 20) print문 안에 계산식
# if num > 10: if문 뒤에 조건식

# 문장, 문(statement)
# 코드 한 줄
# print("Hello") print 문
# if True: