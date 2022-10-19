# 컬렉션 고급 문법
# 시퀀스 언패킹

# 목록에서 인덱싱 문법으로 하나씩 변수 초기화
num_list = [10, 20]
a = num_list[0]
b = num_list[1]

# 언패킹 문법으로 일괄적으로 변수 초기화
a, b =[10, 20]
print(f"{a=}, {b=}")

# 두 변수의 값을 교환하는 고전적인 방법
temp = a
a = b
b = temp
print(f"{a=}, {b=}")

# 두 변수의 값을 교환하는 pythonic한 방법
a, b = b, a
print(f"{a=}, {b=}")
