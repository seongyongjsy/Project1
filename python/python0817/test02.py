# 목록 메소드(method)
from copy import copy


num_list = []
print(num_list)

num_list.append(10) #append(): 맨뒤에 새로운 요소 추가
print(num_list)
num_list.append(20)
print(num_list)

num_list.insert(1, 15) # insert(위치, 요소): 특정 위치에 새로운 요소 추가
print(num_list) #[10, 15, 20]

num_list.extend([30, 35]) # extend(목록): 목록의 요소들을 병합(확장)
print(num_list) # [10, 15, 20, 25, 30]

print(num_list + [40, 45, 50]) # 목록 + 목록: 목록의 요소들을 병합, 새 목록 생성

print("-" * 50)

num_list.remove(15) # remove(요소): 지정한 요소를 목록에서 제거
print(num_list) # [10, 20, 25, 30]

output = num_list.pop() #pop(): 맨 뒤의 요소를 꺼내옴
print(num_list, output) #[10, 20, 25], 30

output = num_list.pop(1) # pop(i): 특정 인덱스에 위치한 요소를 꺼내옴
print(num_list, output) # [10, 25], 20

num_list.clear() # clear(): 모든 요소를 제거
print(num_list) # []

print("-"* 50)

# 요소 기타 연산
num_list = [1, 2, 3] * 2 # * 연산을 통해 요소를 반복해서 구성할 수 있음
print(num_list)

num_list[1] = 200 # 인덱싱을 통해 요소를 변경할 수 있음
print(num_list)

num_list[2:4] = [300, 100] # 슬라이싱을 통해 요소들을 변경할 수 있음
print(num_list)

num_list[::3] = [-1, -10] # 슬라이싱을 통해 연속적이지 않은 요소들도 변경할 수 있음
print(num_list)

del num_list[4] # del 키워드를 통해 변수를 메모리에서 지우거나 요소를 삭제할 수 있음
print(num_list)

print("-"* 50)

# 검색, 정렬 등 기타 유용한 메소드 관련
str_list = ["hello", "world", "hi", "students", "goodbye", "teacher"]

print("hello" in str_list)
print("good morning" in str_list)

print(str_list.index("students")) # index(요소) : 요소가 몇 번 인덱스에 있는지 검사
# print(str_list.idex("good afternoon")) # 없는 요소를 시도하면 오류 발생

print(str_list.count("hi")) # count(요소): 요소가 몇 개 있는지 검사
print(str_list.count("good evening")) # 없는 요소를 시도하면 0

str_list.sort(reverse=True) # sort(): 요소를 오름차순(작은 값부터 큰 값으로) 정렬
print(str_list) # reverse = True => 내림차순 정렬

str_list.reverse() #reverse(): 요소의 순서를 뒤집음
print(str_list)

copy_list = str_list.copy() # copy(): 사본을 만듬
copy_list.reverse()
print(str_list)
print(copy_list)

print(sorted(str_list)) # sorted(): 사본을 만들고 그 사본을 정렬함
print(list(reversed(str_list))) # reversed(): 사본을 만들고 그 사본의 순서를 뒤집음, 단독 사용 불가