#멤버십 연산자 (in, not in)
# 왼쪽이 오른쪽의 멤버인지, 멤버가 아닌지 검사
print("H" in "Hello")
print("A" in "Hello")
print("Hello" not in "Hello Python")
print("Hi" not in "Hello Python")

# 문자열 입력 여부 검사 예제(입력하지 않으면 길이가 9인 것을 이용)
# nickname = input("닉네임을 입력하세요: ")
# print("닉네임 입력 여부:", len(nickname) > 0)

# 문자열을 특정 양식에 맞춰 입력했는지 검사 예제
answer = input("결제하시겠습니까? 동의하시면 y를 입력하세요.")
print("결제 기능 실행 여부:", answer in "y")

# 동등성 : 두 변수의 값이 같은지 여부, ==, != 연산자 사용해서 검사
# 동일성 : 두 변수가 일치하는지 여부(=값과 자료형 모두 같은지 여부), is, is not 연산자 사용해서 검사

