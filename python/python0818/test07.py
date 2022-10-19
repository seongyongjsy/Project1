# 컬렉션 관련 함수
# enumerate() : 컬렉션 내 요소들을 인덱스와 묶어서 표현하는 함수
# 주로 사전으로 변환해서 사용하는데, 인덱스가 키로 설정됨
# 한 번 생성된 enumerate object는 한 번 변환 후 재사용 불가
import imp


function_list = ['학생 정보 입력', '학생 정보 조회', '학생 정보 수정', '학생 정보 삭제', '프로그램 종료']
result = enumerate(function_list) 
print(result)

# menu_list = list(result) #중첩된 목록으로 변환
# print(menu_list) 

menu_dict = dict(result) # 인덱스를 키로, 요소를 값으로 하는 사전으로 변환
print(menu_dict)

menu_num = int(input("메뉴 번호를 입력하세요: "))
print(menu_dict[menu_num], "실행") # 입력받은 번호를 키로 문자열을 꺼내오는 예제

print("-"*50)

#zip() - 두 개 이상의 컬렉션의 요소들을 서로 순차적으로 묶음
time_list = ["아침", "점심", "저녁"]
food_list = ['토스트', '제육볶음', '치킨', '씨리얼', '짜장면', '햄버거']
from random import shuffle
shuffle(food_list) # shuffle(): 시퀀스의 순서를 섞는 함수
zip_result = zip(time_list, food_list) # zip object 로 변환
#print(zip_result)

# zip_list = list(zip_result) # zip object를 list 로 변환
# print(zip_list) # 중첩된 목록[(a, b),(c,d),...] 생성

zip_dict= dict(zip_result) # zip object를 dict로 변환 - 이미 사용된 zip object는 재사용 불가
print(zip_dict) # 사전 생성{k:v, k:v,...}생성

print("-"*30)

# all() - 입력받은 컬렉션의 모든 요소가 참이면 True 로 계산하는 함수
# any() - 입력받은 컬렉션의 요소 중 하나라도 참이면 True로 계산하는 함수
print(all([1, 2, 3, 4, 5]))  # 0이 아닌 값은 True로 취급 => 모든 요소가 0이 아니기 때문에 결과도 True
print(all([0,1])) # 0은 False로 취급 => all() 함수 계산 결과 False
print(any([1, 2, 3, 4,5])) # 모두 0이 아니기 때문에 계산 결과 True
print(any([0, 1])) # 0이 아닌 값이 있기 때문에 계산 결과 True
print(any([0, 0, 0])) # 모두 0이기 때문에 False

prime_set = {i for i in range(2, 30) if all(i % j != 0 for j in range(2, i))}
print(prime_set)


#map(function, iterable) - 컬렉션 내 모든 요소에 대해서 함수를 적용한 결과를 만듦
#filter(function, iterable) - 컬렉션 내 모든 요소에 대해서 함수를 적용하고 True인 요소만 선택

map_result = map(type,[0, 0.1, "hello", True , False])
print(list(map_result))

map_result2 = map(id, ["hi", "hi", "hi", "hi", "hi"])
print(list(map_result2))

def multiple(i):
    return i * 2

map_result3 = map(multiple, [1, 3, 11, 33])
print(list(map_result3))

def divide_by_two(i):
    return i % 2 == 0 

filter_result = filter(divide_by_two, [2, 3, 4, 5,6])
print(list(filter_result))