# 사전(Dictionary) - 저장할 데이터에 이름표(key)를 붙여서 함께 저장하는 방식
student = {"student_number": 20001111, "name": "홍길동", "major_code": "0001"}
print(student)
print(type(student))

print(dict([[1, "hello"],[10, "hi"],[100,"bye"]]))

print({}) # 빈 사전
print(dict()) # 빈 사전

print("-" * 30)

something_dict = {
    10: 10,
    "aaa" : "aaa",
    (10, 20, 30): "what",
   # [123, 456]: [111, 222], #key => 불변 자료형만 가능, value => 제한 없음
}
print(something_dict)

print("-"* 30)

num_dict = {
    1: "one",
    2: "two",
    3: "three",
    0: "zero",
    0: "o", # 키는 중복 불가, 나중에 작성한 키 -값이 기존에 작성한 키 - 값이 덮어씌워짐
    "3": "three", # 값은 중복 가능, 이미 존재하는 값도 또 저장 가능
}
print(num_dict)