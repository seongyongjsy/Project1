# 객체 지향 프로그래밍(Object-oriented programming, OOP) 
#   객체를 이용해서 프로그램을 설계하는 방식
#   객체를 부품처럼 서로 연결하여 프로그램을 동작시킨다.
# 객체(Object):
# 클래스를 통해 만들어진 대상, 데이터
# 현실 세계의 사물에 빗대어서 코드를 표현하는 것
# 상태(변수)와 동작(함수)을 주로 표현한다.
# 클래스(class):
# 객체를 만들기 위한 설계도, 틀, 도면
# 개발자가 작성하는 코드.

# print(type(10))
# print(type(3.14))
# print(type("hello"))

#help(int)   # int()는 사실 함수가 아니라 클래스를 통해 정수 데이터(객체)를 생성하는 코드!
# 클래스를 이용해서 객체(데이터)를 생성하는 방법1 - 일부 클래스는 리터럴로 표현 가능
print(10) # 정수(십진수) 리터럴
print(0b10) # 정수(이진수) 리터럴
print(3.14) # 소수 리터럴
print(3e10) # 소수(지수표현식) 리터럴
print("hello") #문자열 리터럴
print("hi") #문자열 리터럴
print(True) #논리형 리터럴
print(False) # 논리형 리터럴

#클래스를 이용해서 객체(데이터)를 생성하는 방법2 - 클래스명(값)
print(int("10")) # 10의 값을 갖는 int 객체 성능
print(float("3.14")) # 3.14의 값을 갖는 float 객체 생성
print(str(1234)) #"1234"의 값을 갖는 str 객체 생성
print(bool([])) # True의 값을 갖는 bool 객체 생성

print("\n", "=" * 50, "\n")

#클래스 작성 방법
class Car: #클래스 명은 PascalCase를 사용
    color = "Red" # 상태를 나타내는 변수
    type = "Truck" # 클래스 변수로 부름

    def start(self):    # 메소드(클래스에 작성된 함수)는 self 인수를 반드시 작성!
        print("부르릉")

    def stop(self):     # self => Car 클래스로 만들어진 객체를 입력받는 매개변수
        print("끼이익")

new_car = Car() # 작성한 클래스를 사용해서 객체 생성
print(new_car.color)
print(new_car.type)
new_car.start() # 메소드 호출 방법1 - 객체변수명.메소드명()
new_car.stop()  # 객체가 자동으로 메소드의 첫 번째 인수(self)에 입력됨
Car.start(new_car)  # 메소드 호출 방법2 - 클래스명.메소드명(객체명)
Car.stop(new_car)   # 메소드의 첫 번째 인수(self)를 직접 설정하는 방식
# 클래스 변수 + 메소드를 묶어서 속성(property), 멤버(member) 라고 부름
