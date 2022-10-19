# 기타 제어문
# continue: 현재 반복을 건너뛰고 다음 반복으로 넘어간다.
# break: 진행 중인 반복을 중단한다.

# i = 0
# while i < 10:   
#     i += 1
#     if i == 3 or i == 5 or i == 7:
#         continue 
#     print(i)

# i = 0

# while i < 10:
#     i += 1 
#     if i == 5:
#         break
#     print(i)

i = 0
while i < 10:
    i += 1
    j = 0
    while j < 10:
        j += 1
        if j == 5:
            break
        print("i = ", i, "j =", j)