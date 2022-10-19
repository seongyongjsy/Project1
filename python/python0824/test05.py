def calc_division(a, b):
    # if b == 0:
        # return 0
        # raise ZeroDivisionError # 오류를 강제로 발생시키는 코드
    assert b != 0   # 표현식을 검사해서 False면 AssertionError를 발생시킴
    return a / b

try:
    calc_division(10, 0)
except:
    print("오류발생")
finally:
    # 마지막에 항상 실행하는 코드 블록
    print("프로그램 종료.")

