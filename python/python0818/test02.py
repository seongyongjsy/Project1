#집합(Set) - 순서가 없고 중복을 허용하지 않는 자료형

# 중괄호{} 를 이용해서 값을 하나씩 쉼표로 구분지어서 표현
num_set = {1, 2, 3, 4, 5}
print(num_set)
print(type(num_set))

# 순서가 없음
str_set = {'hello', 'world', 'hi', 'students', 'bye', 'teacher'}
print(str_set)

# 서로 다른 자료형 저장 가능
somethig_set = {0, 1, 1.1, -0.1, 'hello', True, False, None}
print(somethig_set)

# 목록을 집합으로 변환하여 중복된 요소 제거
num_list = [1, 1, 2, 2, 3]
print(num_list)
result_set = set(num_list) # 목록 => 집합 변환
print(result_set)
result_list = list(result_set) # 집합 =>목록 변환
print(result_list)

# 빈 집합 표현 방식 - set() 함수로만 표현 가능
print({}) # 빈 사전
print(type({})) # 빈 사전
print(set()) # 빈 집합
print(type(set())) #빈 집합
