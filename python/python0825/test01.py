# 객체 입출력
# int, float, str, bool, sequence => 기본적으로 저장가능
# dict, set, class => 기본적으로 저장 불가

num_dict = {1: "one", 2:"two", 3:"three"}
# f = open(r"C:Workspace\python0825\test01.bin","wb")
# f.write(bytes(num_dict))
# f.close()
# f = open(r"C:Workspace\python0825\test01.bin","rb")
# print(dict(f.read()))
# f.close()

import pickle
from unicodedata import name # pickle: 객체의 직렬화(serialization)를 도와주는 모듈
# f = open(r"C:Workspace\python0825\test01.bin","wb")
# pickle.dump(num_dict, f)  # dump(): 파일 쓰기 시 사용하는 함수
# f.close()
# f = open(r"C:Workspace\python0825\test01.bin","rb")
# print(pickle.load(f))   # load(): 파일 읽기 시 사용하는 함수
# f.close()

student_list = []
# student_list.append({
#     "num" : "2022082401",
#     "name": "hong",
#     "grade": 1,
# })
# student_list.append({
#     "num" : "2022082402",
#     "name": "kim",
#     "grade": 2,
# })
class Student:
    def __init__(self, num, name, grade) -> None: # -> 반환 값의 자료형에 대한 형 힌트(type hinting)
        self.num = num
        self.name = name
        self.grade = grade
    def __repr__(self) -> str:
        return f"{self.num}, {self.name}, {self.grade}"
student_list.append(Student("2022082401", "hong", 1))
student_list.append(Student("2022082402", "kim", 2))
# f = open(r"C:Workspace\python0825\test01.bin","wb")
# pickle.dump(student_list, f)
# f.close()
# f = open(r"C:Workspace\python0825\test01.bin","rb")
# print(pickle.load(f))
# f.close()


