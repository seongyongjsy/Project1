# 1. 숫자 두 개를 입력받아서 두 숫자의 합을 출력하는 코드를 작성하세요.
# a = int(input('첫 번째 숫자를 입력하세요'))
# b = int(input('두 번째 숫자를 입력하세요'))
# print("두 숫자의 합은 :", a + b, "입니다.")

# 2. 정수 두 개를 입력받아서 두 값을 나눈 몫과 나머지를 구하는 코드를 작성하세요.
# num1 = int(input('첫 번째 정수를 입력하세요'))
# num2 = int(input('두 번째 정수를 입력하세요'))
# print(num1,"을/(를)",num2,"로 나눴을 때의 몫은", num1//num2, ", 나머지는", num1%num2,"입니다.")

# 3. 정수 한 개를 입력받아서 짝수면 True, 홀수면 False를 출력하는 코드를 작성하세요.
# num1 = int(input("정수 한 개를 입력하세요."))
# print(num1 % 2 == 0)

# 3-2 정수 한 개를 입력받아서 짝수면 False, 홀수면 True를 출력하는 코드를 작성하세요.
# num = int(input('정수를 입력하세요'))
# print(num %2 != 0)

# 4. 정수 한 개를 입력받아서 3의 배수이거나 또는 5의 배수이면 True, 아니면 False를 출력하는 코드를 작성하세요.
# num = int(input("정수를 입력하세요."))
# print(num % 3 == 0 or num % 5 == 0)

# 5. 수학, 영어, 국어 점수(정수)를 입력받아서 평균을 출력하고,
# 시험 통과 여부를 True, False로 출력하는 코드를 작성하세요.
# 평균 점수가 70점 이상이고,
# 한 과목도 40점 미만이 아니면 통과

math_score = int(input('수학 점수를 입력하세요:'))
eng_score = int(input('영어 점수를 입력하세요:'))
kor_score = int(input('국어 점수를 입력하세요:'))

avg_score = (math_score + eng_score + kor_score) / 3
print("평균 점수:", avg_score)

is_passed = (avg_score >= 70) and (math_score >= 40) and (eng_score >= 40) and (kor_score >= 40)
# print((math_score + eng_score + kor_score) / 3 > 70 and math_score > 40 and eng_score > 40 and kor_score > 40)
print("시험 통과 여부:", is_passed)

#자동 형 변환
print(10 / 5) # / 연산자의 경우, 정수와 정수 간의 연산 시 자동으로 실수형으로 변환
#print(2.5 /1.25)
print(10 + 5.0) # 대부분의 산술 연산자에서, 정수와 실수 간에 연산 시 자동으로 실수형으로 변환