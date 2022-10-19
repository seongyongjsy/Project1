# 튜플(Tuple) - 순서(index)를 매겨서 여러 개의 데이터를 묶어서 표현하는 방식, 자료형
# 튜플은 불변 자료형이기 때문에 한 번 만들어지면 수정 불가능 
num_tuple = (1, 2, 3, 4, 5)
print(num_tuple)
print(type(num_tuple))

something_tuple = (1, 2, 3, 0.1, 9.99, "hello", "hi", True, False)
print(something_tuple)
print(type(something_tuple))

for elem in something_tuple:
    print(f"{elem=}, {type(elem)=}")

print(num_tuple[0]) # 인덱싱 결과는 요소 => 인덱싱 결과의 자료형은 요소 자체의 자료형
print(num_tuple[1:4]) # 슬라싱 결과는 튜플 => 슬라이싱 결과의 자료형은 튜플

print("-"* 30)

print((1, 2, 3))
print(tuple("hello"))
print(tuple()) # 빈 튜플
print(()) # 빈 튜플
str_tuple = "hello", "hi", "goodbye" # 소괄호 생략 가능
print(str_tuple, type(str_tuple))   

print( "-" * 30 )

# t = 10 # tuple이 아님!
t= 10 , #요소가 1개 있는 튜플 표현 방법
print(t, type(t))