# 컬렉션(Collection) - 자료 구조를 지원하기 위한 자료형
# 자료 구조(Data Structure) - 대량의 데이터를 효율적으로 조작하기 위한 개념

# 목록(List) - 순서 (Index)를 매겨서 여러 개의 데이터를 묶어서 표현하는 방식, 자료형
from turtle import st


num_list = [1, 2, 3, 5, 10, 100, 0, -1] # 목록 생성 및 요소를 직접 지정
print(num_list)
print(type(num_list))

str_list = ["hello", "world", "hi", "students"]
print(str_list)
print(type(str_list))

# 서로 다른 자료형을 요소로 저장할 수 있음
something_list = [0, 9999, -1, 3.14159265245, "what", True, False, None]
print(something_list)
for elem in something_list:
    print(f"{elem=}, {type(elem)=}")

print("-"* 50)

# 인덱싱, 슬라이싱 적용 가능
print(num_list[0]) # 자료형이 int => 인덱싱 결과는 요소의 자료형
#print(num_list[8])
print(str_list[1:3]) # 자료형이 list => 슬라이싱 결과는 부분 목록
print(str_list[:1])
print(str_list[3:3])

for substr in str_list[1:3]:
    print(substr)

print("-"*50)

student_list = [[1, "홍길동"], [2, "김철수"], [3, "김영희"]] # 3개의 요소를 가진 list, 각각의 요소도 list
print(student_list)
print(student_list[0])
print(student_list[0][1])
for student in student_list:
    for info in student:
        print("학생 정보:", info)

print("-" * 50)

#list()
print(list("hello")) # 문자 하나하나를 요소로 갖는 목록 생성
print(list()) # 빈 목록 생성
print([]) # 빈 목록 생성