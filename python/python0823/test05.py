# 클래스 메소드(class method) : 
#    해당 클래스로 만들어진 모든 인스턴스가 공유하는 메소드
#    보통 클래스 변수를 조작하기 위해 사용.
# 인스턴스 메소드(instance method) : 객체 고유의 메소드, 일반적으로 만든 메소드
#    인스턴스마다 서로 다르게 동작할 수 있는 메소드, 일반적으로 만든 메소드.
#    보통 인스턴스 변수를 조작하기 위해서 일반적으로 사용.
# 인스턴스(instance) : 클래스를 통해 만들어진 물리적 실체. 객체와 가리키는 대상이 같음
# 정적 메소드(static method): 클래스와 상관없는 유틸리티 메소드

class Car:
    count = 0   # 클래스 변수: 해당 클래스가 만들어진 모든 인스턴스가 공유하는 변수

    def __init__(self, color):
        self.color = color  # 인스턴스 변수: 각각의 인스턴스에 종속되는 변수
        Car.count += 1

    @classmethod    # 데코레이터 : 메소드 위에 작성해서 메소드에 추가 역할, 기능을 부여하는 문법
    def get_count(cls): # 클래스 메소드의 첫 번째 인수는 보통 cls
        return cls.count
    
    @staticmethod
    def engine_start():
        print("안전 운전 하세요.")

car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, car2.color) # 인스턴스 변수는 객체마다 서로 다른 값을 가질 수 있음
print(car1.count, car2.count) # 클래스 변수는 모든 객체가 똑같은 값을 가짐
print(Car.count)

print(Car.get_count())
car3 = Car("Green")
print(Car.get_count())

Car.engine_start()