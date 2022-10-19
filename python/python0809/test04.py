# 자료형 변환
# 서로 다른 자료형 간에 변환 가능
# int(), float(), str(), bool() 함수 사용
a = input("정수를 입력하세요:")
a = int(a)
print("입력한 값:", a, "/ 자료형:", type(a))

b = input("실수를 입력하세요")
b= float(b)
print("입력한 값:", b, "/ 자료형:", type(b))

#int, float => str
# a = 10
# print("변수 a의 값은 "+ str(a) + "입니다.")

#float => int
b = 10 / 3
print(int(b))

#int => float
c = 10 * 3
print(float(c))

#0, 0.0 , '', "", => False (내용이 없으면 False 로 취급)
#1, -1, 0.00001, 'hello', "False" => True (어떤 값이든 있으면 True 로 취급)
print(bool(10)) #True
print(bool(-1)) #True
print(bool(0)) #False

print(bool(9999999.9999999))#True
print(bool(0.00000000000000000001))#True
print(bool(0.0)) # False

print(bool("True")) #True
print(bool("False"))#True
print(bool("")) #False

# 변수 어노테이션(variable annotation, type hinting)
a:int = 10
print(a)
print(type(a))
print(a*10)