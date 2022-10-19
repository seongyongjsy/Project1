#문자열
#문자들의 나열, 문자들의 모음
# 작은 따옴표 또는 큰 따옴표로 표현

#확장열(escape sequence)
from turtle import Turtle


a = "I'm student."
print(a)

b = 'you\'re teacher' #확장열을 이용해서 작은 따옴표를 표현한 예제
print(b)

c = "he says, \"Python is fun\"."
print(c)

d = "today is tuesday.\nTomorrow is wednesday." #\n : 게헹문자를 표현
print(d)

e = "name\tage\n===========\nKim\t25\nLee\t30" #\t : 탭(tab)을 표현
print(e)

f = "C:\\Workspace\\myfiles\\newfiles" # \\: 백슬래시를 표현
print(f)

# raw string
# 확장열 적용 없이 원본 문자열 그대로 표현하는 문법
g = r"C:\workspace\myfiles\newfiles" 
print(g)

# 여러 줄 문자열
# 따옴표를 세 개 써서 표현하는 문법
h = '''
오늘은 화요일입니다.
오전에 자료형에 대해 공부했습니다.
오후에도 자료형에 대해 공부합니다.
5시에 수업이 끝납니다.
'''
print(h)

# len()함수
# 문자의 개수를 구하는 함수
str_num = len(h)
print("문자의 개수:", str_num)

# 논리형(bool)
i = True
j = False
print(i, j)
print(type(i), type(j))

#NoneType 자료형
k = None #  변수 k를 선언하고 일단 None으로 초기화
print(k, type(k))
k = 10 # 앞서 선언된 K 변수에 10을 재 초기화
print(k, type(k))
