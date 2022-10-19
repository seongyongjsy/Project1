#반복문 - for 문
# 목록을 이용해서, 목록의 요소(정수 값)을 하나씩 꺼내오며 반복
for i in [1, 2, 3, 4, 5]:
    print(i, "번째 반복 중...")

# 목록을 이용해서, 목록의 요소(문자열 값)를 하나씩 꺼내오며 반복
for s in ["hello", "hi", "good bye"]:
    print(s)

# 문자열(string)을 이용해서, 문자(character)를 하나씩 꺼내오며 반복
for c in "Hello, Python!":
    print(c)

# range(n) 함수를 이용해서 , 0~ n-1 까지 숫자를 생성해서 하나씩 꺼내오며 반복
for i in range(100):
    print(i)

# range(a,b) 함수를 이용해서, a부터 b-1 까지 숫자를 생성해서 하나씩 꺼내오며 반복
for i in range(10, 20):
    print(i)

# range(a, b, c)함수를 이용해서, a부터 b-1까지 c 씩 증가하는 숫자를 생성해서 하나씩 꺼내오며 반복
for i in range(100, 1000, 200):
    print(i)
