def hello():
    print("hello")

hello()

class Student:
    def __init__(self, name, grade, _class) -> None:
        self.name = name
        self.grade = grade
        self._class = _class
    
    def get_name(self):
        return self.name

hong = Student("홍길동", 1, 2)
print(hong.get_name())