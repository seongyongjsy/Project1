# 3. 2 이상의 정수를 입력받아서 소수 여부 판별

# ex) 2 이상의 정수를 입력하세요: 11
# 11 은(는) 소수입니다.

# ex) 2 이상의 정수를 입력하세요: 20
# 20 은(는) 소수가 아닙니다.

# ex) 2 이상의 정수를 입력하세요: 1
# 잘못 입력하셨습니다.

num = int(input("정수를 입력하세요"))

if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # if is_prime:
    #     print(num, "은(는) 소수입니다.")
    # else:
    #     print(num, "은(는) 소수가 아닙니다.")
    print(num, "은(는)", "소수입니다." if is_prime else "소수가 아닙니다.")
else:
    print("잘못 입력하셨습니다.")

 