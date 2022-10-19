# 집합 연산
from random import sample


num_set = {2, 3, 5, 7, 11}

# 반복문 사용 가능
for num in num_set:
    print(num)

print(f"{len(num_set)=}")
print(f"{min(num_set)=},{max(num_set)=}")

# 멤버십 연산자 적용 가능
print(f"{( 2 in num_set)=}, {(10 in num_set)=}")

# 컬렉션 주요 함수 사용 가능
print(f"{len(num_set)=}")
print(f"{min(num_set)=}, {max(num_set)=}")

print("-" * 50)

two = {2, 4, 6, 8, 10, 12}
three = {3, 6, 9, 12}

print("교집합:", two & three)
print("합집합:", two | three)
print("차집합1:", two - three)
print("차집합2:", three - two)
print("배타적 차집합:", two ^ three) # 합집합 - 차집합

print(two > (two - three))
print((two & three) <= three)

print("-" * 50)

sample_set = set()
print(sample_set)

sample_set.add(100) # add(요소) : 집합에 요소 추가
sample_set.add(200)
sample_set.add(333)
print(sample_set)

sample_set.remove(100) #remove(요소) : 집합에서 요소 제거
#sample_set.remove(-1) #없는 요소 제거 시도 시 오류발생
print(sample_set)

sample_set.discard(220) # discard(요소): 집합에서 요소 제거
sample_set.discard(-1) #없는 요소 제거 시도 시 아무 동작도 하지 않음
print(sample_set)

print(sample_set.pop()) # pop(): 임의의 요소 하나를 꺼내옴
print(sample_set)

sample_set.clear() # clear(): 모든 요소 제거
print(sample_set)

copy_set = sample_set.copy() # copy(): 같은 값을 가지는 사본 생성
print(copy_set)