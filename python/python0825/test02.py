# 이터레이터(iterator)
num_list = [1, 10 , 100, 1000]  # 이터러블-시퀀스
it = iter(num_list) # iter(): 이터러블에서 이터레이터 객체를 생성하는 함수
# print(it,type(it))
print(next(it))  # next(): 이터레이터에서 요소를 꺼내오는 함수
print(next(it))  # 첫 요소부터 순차적으로 꺼낼수 있음
print(next(it))
print(next(it))
# print(next(it))  # 모든 요소를 반복한 뒤 다시 호출하면 StopIteration 예외 발생

# for num in num_list:
#     print(num)

it = iter(num_list)  # 목록의 이터레이터 객체 생성
while True:
    try:
        print(next(it)) # 이터레이터 객체에서 요소를 하나씩 꺼내옴
    except StopIteration:   # 더이상 꺼내올 요소가 없으면 예외를 발생시키고 반복을 중단
        break

    print("-" * 30)

#   사용자 정의 이터러블 클래스 작성 방법
    class MenuIterable:
        def __init__(self) -> None:
            self.menu = ["회원 등록", "회원 조회", "회원 정보 검색", "회원 정보 수정", "회원 탈퇴"]

        def __iter__(self): 
            #__iter__(): iter() 함수에 의해 호출되는 특수 메소드
            # 반복문을 만나면 가장 먼저 실행되는 함수
            self.index = -1 # 반복문에서 사용하기 위해 인덱스를 설정
            return self

        def __next__(self): 
            #__next__(): next() 함수에 의해 호출되는 특수 메소드
            # 매 반복마다 호출되는 메소드
            self.index += 1
            if self.index >= len(self.menu): # 모든 요소를 반복한 경우    # 모든 요소를 반복한 경우
                raise StopIteration    # 반복을 중단하도록 예외를 발생시킴
            return self.menu[self.index]  # 매 반복에서 반환할 요소를 작성
    
    for menu in MenuIterable():
        print(menu)

print("-" * 50)

# 제네레이터(Generator) : 반복할 수 있는 함수
# 이터러블 객체를 만드는 대신 간단하게 같은 기능을 만들 수 있는 문법
def menu_generator():
    menu = ["회원 등록", "회원 조회", "회원 정보 검색", "회원 정보 수정", "회원 탈퇴"]
    yield menu[0]   # yield 매 반복마다 반환할 요소를 작성
    yield menu[1]   # 반복할 때마다 yield가 하나씩 실행됨
    yield menu[2]   # 머지막으로 실행한 yield의 위치를 기억해서
    yield menu[3]   # 다음 반복으로 넘어가면 다음 yield가 실행
    yield menu[4]
gen = menu_generator()  
print(gen, type(gen))
print(next(gen))    # 이터러블과 마찬가지로 next() 함수를 통해 강제로 반복 가능
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))    # 더이상 반복할 요소가 없으면 StopIteration 예외 발생
for menu in menu_generator():   # for문 등을 통해 자동으로 반복 가능
    print(menu)

print("-" * 30)

# 제네레이터 표현식(generator expression)
# 제네레이터를 만드는 간단한 문법
ge = (i for i in range(10))
print(ge, type(ge))
for i in ge:
    print(i)

prime_gen = (i for i in range(30) if all(i % j != 0 for j in range(2, i)))

while True:
    input("아무거나 입력하시면 반복해서 소수를 출력합니다: ")
    try:
        print(next(prime_gen))
    except StopIteration:
        break
print("출력 끝.")
