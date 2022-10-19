# 생산자(init) : 객체 생성 시, 주요 변수들의 초기값을 설정해주는 문법
class Car:
    # 생성자 메소드: 객체 생성 시 호출되는 함수
    def __init__(self, color, type):
        print("생성자  메소드 호출!")
        self.color = color  # 이 클래스로 만들어지는 car 객체에,
        self.type = type    # color/type 속성(변수)을 생성해서 매개변수 color/type 으로 초기화

    # setter 메소드: 값을 전달받아서 기존의 속성에 초기화해주는 함수
    def set_color(self, color):
        self.color = color

    # getter 메소드: 객체에 저장된 속성 값을 반환해주는 함수
    def get_color(self):
        return self.color

first_car = Car("Red", "Truck")   # 객체 생성 시 생성자 메소드를 호출하게 됨
print(first_car.color, first_car.type)

second_car = Car("Yellow", "Bus")
print(second_car.color, second_car.type)

second_car.color = "Blue" # 기존에 저장된 값을 바꾸는 코드
print(second_car.color, second_car.type) # 속성 값을 직접 꺼내는 코드

second_car.set_color("Green") # setter 메소드를 이용해서 속성 값을 바꾸는 코드
print(second_car.get_color(), second_car.type) # getter 메소드를 이용해서 속성 값을 꺼내는 코드
