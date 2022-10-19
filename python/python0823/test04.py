# 상속(Inheritance) : 상위(부모) 클래스의 속성을 하위(자식) 클래스에서 물려받아 사용하는 것
class Car:
    def start(self):
        print("부르릉")

    def stop(self):
        print("끼이익")

class Bus(Car):     # 클래스 작성 시, 클래스명 뒤에 부모 클래스명을 작성하면 상속
    def stop(self): # 오버라이드(override): 부모 클래스의 속성을 자식 클래스에서 재정의하는 것
        super().stop() # super(): 부모 클래스의 객체를 호출
        print("쾅!")
#        print("끼이이이이익")

new_car = Car()
new_car.start()
new_car.stop()

new_bus = Bus()
new_bus.start()
Car.start(new_car)