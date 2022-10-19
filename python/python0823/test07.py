# 특수 메소드(special method)
#   객체 생성 시 자동으로 만들어주는 특별한 메소드들
#   자동으로 만들진 않지만, 특별 동작을 수행하도록 제공해주는 메소드
#   생성자 메소드(__init__), __str__, 연산자 메소드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    # 이 클래스로 만든 객체에 대해서, == 연산자와 함께 사용되면 호출되는 메소드
    def __eq__(self, other):    
        return self.name == other.name and self.age == other.age
    # 이 클래스로 만든 객체에 대해서, < 연산자와 함께 사용되면 호출되는 메소드
    def __lt__(self, other):
        return self.age < other.age

hong = Person("홍길동", 20)
kim = Person("김철수", 22)
soo = Person("김철수", 22)
print(hong)
print(kim)
print(kim == soo)
print(hong < kim)