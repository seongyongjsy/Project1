# 튜플 컴프리헨션은 반드시 tuple() 함수에 작성해야 함
num_tuple = tuple(i for i in range(10))
print(num_tuple)

# 사전 컴프리헨션
num_dict = {i: i**2 for i in range(10)}
print(num_dict)

# 집합 컴프리헨션
num_set = {i for i in range(10)}
print(num_set)