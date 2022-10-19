# for문 예제1 - 카운트다운
# i = 0
# while i < 10:
#     print(10 - i)
#     i +=1

# for i in range(10):
#     print(10 - i)

# for i in range(10, 0 , -1):
#     print(i)

#for문 예제2 - 숫자 합계 구하기
# total = 0
# i = 0 
# while i < 10:
#     total += i+1
#     i += 1 
# print(total)

# total = 0
# for i in range(10):
#     total += i+1
# print(total)

#for문 예제3 - 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(i,"*", j, "=", i*j, end="\t")
        if j % 3 == 0:
            print()
    print()
# i = 2
# while i <= 9:
#     j = 1
#     while j <= 0:
#         print(1,"*",j,"=", i*j)
#         j +=1
#     i += 1