#제어문(control statement)
# 프로그램의 실행 흐름을 제어하는 문장

# 1. 조건문(conditional statement)
# 주어진 값 또는 조건식을 판단해서 선택적으로 실행하는 문장

# 1-1. if문
#if(bool값 또는 조건식):
    #True일 경우 실행할 코드
    #...
    #...

# num = int(input("0을 제외한 숫자를 입력하세요: "))
# if num != 0:
#     # if True 인 경우 실행할 코드 블록
#     # 블록: 코드 뭉치. 공백 4개로 표현
#     print("잘 입력하셨습니다.")
#     print("당신이 입력한 값은", num,"입니다.")
# else:
#     #if False인 경우 실행할 코드 블록
#     print("왜 0을 입력했나요?")
# num = int(input("아무 정수나 입력하세요: "))

# if num > 100:
#     print("큰 수를 입력하셨군요?")
# elif num > 10:
#     print("적당한 수를 입력하셨네요.")
# elif num > 0:
#     print("작은 수를 입력하셨네요.")
# else:
#     print("0 이하를 입력하셨나요?")
    
# print("프로그램 종료.")

# if 문 예제 - 홀짝 판별
# num = int(input("정수를 입력하세요: "))
# if num % 2 == 0:
#     print(num,"은(는) 짝수입니다.")
# else:
#     print(num, "은(는) 홀수입니다.")

# if문 예제2 - FizzBuzz 테스트
# 양의 정수를 입력받아서, 3의 배수면 Fizz, 5의 배수면 Buzz, 3과 5의 공배수면 FizzBuzz를 출력하세요.
# num = int(input("정수를 입력하세요: "))
# if num % 3 == 0 and num % 5 == 0: # 3과 5의 공배수
#     print("FizzBuzz")
# elif num % 3 == 0: # 3의배수는 아니지만 5의 배수인경우
#     print("Fizz")
# elif num % 5 == 0: # 5의 배수는 아니지만 3의 배수인 경우
#     print("Buzz") 

# else: = # 3의 배수도 5의 배수도 아닌경우
#     print("...")

#if 문 예제 3 - 윤년 판별
#윤년 기준
# 1. 년도(숫자)를 4로 나누었을 때 나누어 떨어지고,
# 2. 100으로 나누었을 떄 나누어 떨어지지 않아야 함.
# 3. 400으로 나누었을 때 나누어 떨어지면 윤년.

# year = int(input("년도를 입력하세요:"))

# if ( year % 4 == 0 ) and (year % 100 != 0) or (year % 400 == 0):
#     print(year,"년은 윤년입니다.")
# else:
#     print(year,"년은 평년입니다.")

#if문 예제 4 - 등급 판별
#학점을 입력받아서 4.0 이상이면 A, 3.0이상이면 B, 2.0이상이면 C, 1.0이상이면 D, 그밖에 F로 출력
# num=float(input('점수를 입력하세요'))
# grade = None

# if (num >= 4.0):
#     grade = "A"
# elif(num >= 3.0):
#     grade = "B"
# elif(num >= 2.0):
#     grade = "C"
# elif(num >= 1.0):
#     grade = "D"
# else:
#     grade = "F"
# print(grade, "등급 입니다.")

# match case
# match 변수 :
#     case 값:
#        # 변수와 값이 일치할 경우 실행할 블록
#     case 값2:
#         # 변수와 값2가 일치할 경우 실행할 블록
#         ...

#  a = 7
#  match a:
#      case 10: # a가 10인 경우
#          print("a는 10입니다.")
#      case 9: # a가 9인 경우
#          print("a는 9였군요")
#      case 8 | 7 | 6: # a가 8인 경우
#          print("a는 8, 7, 6이네요.")
#      case _: # 기타 나머지 경우
#          print("a는 뭘까요..?")

# score = int(float(input("학점을 입력하세요: ")))
# grade = None
# match score:
#     case 4:
#         grade = "A"
#     case 3:
#         grade = "B"
#     case 2:
#         grade = "C"
#     case 1:
#         grade = "D"
#     case _:
#         grade = "F"
# print(grade, "등급입니다.")
# month = int(input("월(1~12)을 입력하세요 :"))
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(month,"월은 31일까지 있습니다.")
#     case 4 | 6 | 9 | 11:
#         print(month, "월은 30일 까지 있습니다.")
#     case 2:
#         print(month,"월은 28 또는 29일 까지 있습니다.")
#     case _:
#         print("입력한 값을 확인해주세요.")

# match~case 예제3
# print("========")
# print('1. 회원 등록')
# print('2. 회원 정보 수정')
# print('3. 회원 탈퇴')
# print('0. 프로그램 종료')
# print('========')
# menu_num = int(input("메뉴 번호를 입력하세요: "))
# match menu_num:
#     case 1:
#         print("회원 등록 기능 실행.")
#     case 2:
#         print("회원 정보 수정 기능 실행.")
#     case 3:
#         print("회원 탈퇴 기능 실행.")
#     case 0:
#         print("프로그램을 종료합니다.")
#     case _:
#         print("다시 입력해주세요.")
    
    # 조건 표현식(삼항 연산자)
    # 조건문을 한 줄에 쓰는 문법
time_now = 5
location = "집" if time_now >= 5 else "교실"
print("어디 있니?")
print(location, "이요.")
# location = None
# if time_now >= 5:
#     location = "집"
# else:
#     locatin = "교실"

