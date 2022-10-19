# 스코프(Scope): 코드가 작성된 영역
a = 10  # 전역(global) 스코프
b = 20
c = 30

def hello():
    # 지역(local) 스코프
    print(f"{a=}") # 지역 스코프에서, 전역 스코프의 변수를 참조(호출) 가능
    b = 200 # 전역 변수 b를 200으로 바꾸는 게 아닌, 지역 변수 b를 선언 및 초기화 하는 코드
    print(f"{b=}")
    global c # 이 코드 이하의 모든 코드에서 변수 c는 전역 변수 c를 가르키도록 설정
    c = 300
    print(f"{c=}")
    # d = 40 # 지역 변수는 함수 실행 종료 후 메모리에서 제거

print(f"{a=}, {b=}, {c=}" )    # 전역 스코프에서 전역 스코프의 변수를 참조(호출) 가능
hello()
# print(f"{d=}") # 전역 스코프에서 지역 스코프 변수 절대 참조 불가

print("=" * 30)

def outer():
    # outer 지역 scope
    a=100 # outer scope의 지역 변수 선언 및 초기화
    b = 200 # 지역 변수
    print(f"{a=},{b=}")

    def inner(): # 내재 함수
        # inner 지역 scope
        a = 1000    # inner scope의 지역 변수 선언 및 초기화
        nonlocal b  # 전역 변수가 아닌, 바깥쪽 scope의 지역 변수 선택하는 코드
        b = 2000
        print(f"{a=}, {b=}")

    inner()
    print(f"{a=}, {b=}") # outer scope의 지역 변수 호출

outer()

print("=" * 30 )

class Outer:
    a = -10
    b = -20

    class Inner:
        a = -100

print(Outer.a)
print(Outer.Inner.a)
    