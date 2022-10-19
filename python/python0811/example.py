# 제어문 예제1. 10이하의 소수 출력.

# num = 2
# while num <= 10:
#     is_prime = True # 소수 여부를 저장할 변수
    
#     # 2부터 num-1 까지 숫자들을 이용해서 소수 여부 판별
#     div = 2
#     while div <= num-1:
#         if num % div == 0:
#             #나누어 떨어지는 경우 => 소수가 아님!
#             is_prime = False
#         div += 1
    
#     if is_prime == True:
#         #num이 소수로 판별된 경우 => 출력
#         print(num)
    
#     num += 1
    
    #제어문 에제 1-2 . 2 이상의 정수를 입력받아서 해당 숫자가 소수인지 판별해서 출력.
    # num = int(input("2이상의 정수를 입력하세요:"))
    # is_prime = True
    # div = 2 
    # while div < num:
    #     if num % div ==0:
    #          is_prime = False
    #     div += 1 
    # if is_prime:
    #     print(num, "은(는) 소수입니다.")
    # else:
    #     print(num,"은(는) 소수가 아닙니다.")
    