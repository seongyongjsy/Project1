# 예외(Exception) 처리
num  = 0
try:
    # 오류가 발생할 만한 코드를 작성하는 블록
    num = int(input("정수를 입력하세요: ")) # ValueError 발생 가능
    print("10을 입력한 값으로 나누는 중입니다...") # 오류가 발생하면 이하의 코드는 무시
    print(10 / num) # ZeroDivisionError 발생 가능
    int([1, 3, 5]) #TypeError
except (ValueError, TypeError):
    # ValueError, TypeError가 발생한 경우 실행할 블록
    print("ValueError 또는 TypeError 오류 발생!")
except ZeroDivisionError as e:
    # ZeroDivisionError 발생한 경우 실행할 블록
    print("ZeroDivisonError 오류 발생!")
    print(e)  # 오류 정보를 담은 객체, 출력 시 오류 메시지 출력
except:
    # 기타 오류가 발생한 경우 실행할 블록
    print("알 수 없는 오류 발생")
print("입력하신 값은", num, "입니다.")





