from unittest import result


num_list = [1, 2, 3]

result = num_list[0]
result = 10

# 목록에 int, float, str, bool과 같은 기본적인 자료형이 저장되어 있을 경우,
# 변수를 통해서 간접적으로 변경 불가
print(num_list)
print(result)

student_list = [
    {
        "name" : "홍길동",
        "age" : 20,
    }
]
student = student_list[0]
student["age"] += 1
# 목록에 사전 등 다른 컬렉션 또는 객체를 통해서 값이 간접적으로 저장되어 있을 경우,
# 변수를 통해서 간접적으로 변경 가능
print(student_list)
print(student)