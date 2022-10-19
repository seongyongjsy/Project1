#제어문 예제 2 - 별 찍기
# row = 1
# while row <= 5:
#     col = 1
#     while col <= 5:
#         print("*",end="")
#         col += 1
    
#     print()
#     row += 1 
# row = 1
# while row <= 5:
#     col = 1
#     while col <= 5:
#         if col <= row:
#             print("*",end="")
#         col += 1
    
#     print()
#     row += 1 
# row = 1
# while row <= 5:
#     col = 1
#     while col <= 5:
#         if row >= col:
#             print("*", end="")
#         col += 1
#     print()
#     row += 1

# 별 찍기 3-2
# row = 1
# while row <= 5:
#     col = 1
#     while col <= 5:
#         print("*" if row + col > 5 else " ", end="")
#         col += 1
#     print()
#     row +=1


row = 1
while row <= 5:
    col = 1
    while col <= 5:
        print("*" if row + col <= 6 else " ", end="")
        col += 1
    print()
    row +=1