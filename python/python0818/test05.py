# 컬렉션 고급 문법
# 컴프리헨션

num_list = []
for i in range(100):
    num_list.append(i)
print(num_list)

num_list = [i for i in range(100)]
print(num_list)

# 0 이상 100이하의 정수 중 2의 배수로 이루어진 목록(0도 포함)
two_list = []
for i in range(0, 101, 2):
    two_list.append(i)
print(two_list)

two_list = [i for i in range (0, 101, 2)]
print(two_list)    
# 0 -1 2 -3 4 -5, ...., 99 로 이루어진 목록
switch_list = []
for i in range(100):
    switch_list.append(i * ((-1) ** i))
print(switch_list)

switch_list = [i * ((-1)**i) for i in range(100)]
print(switch_list)

print("-" * 50)

# 조건문이 있는 컴프리헨션
three_list = []
for i in range(50):
    if i % 3 == 0:
        three_list.append(i)
print(three_list)

three_list = [i for i in range(50) if i % 3 == 0]
print(three_list)

# 중첩 반복문이 있는 컴프리헨션
gugudan = []
for i in range(2, 10):
    for j in range(1, 10):
        gugudan = (f"{i}*{j} = {i*j}")
print(gugudan)

gugudan = [f"{i}*{j} = {i*j}" for i in range(2, 10) for j in range(1, 10) ]
print(gugudan)

# 2 이상 50 미만의 숫자 중 소수로 이루어진 목록
all_set = set(range(2,50)) # 2 이상 50 미만의 수로 이루어진 집합
comp_set = set() # 소수가 아닌 수로 이루어진 집합
for i in range(2, 50): 
    for j in range(2, i):
        if i % j == 0:
            comp_set.add(i)
prime_set= all_set - comp_set # 전체 수 집합에서 합성수 집합을 빼서 소수 집합을 만듦
prime_list = list(prime_set) # 소수 집합을 목록으로 변환
prime_list.sort() # 목록을 정렬
print(prime_list)

all_set = set(range(2, 50))
comp_set = {i for i in range(2, 50) for j in range(2, i) if i % j ==0}
prime_set = all_set - comp_set
prime_list = list(prime_set)
prime_list.sort()
print(prime_list)
