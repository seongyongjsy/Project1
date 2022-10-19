#사전 연산
test_dict = {}
print(test_dict)

test_dict[1] = "one" # 새로운 키-값 쌍 추가
print(test_dict)

print(test_dict[1]) # 키를 이용해서 값 조회

test_dict[1] = "first" #지정한 키에 해당하는 값 변경
print(test_dict)

del test_dict[1] # 지정한 키에 해당하는 값 삭제
print(test_dict)

print("-" * 30)

num_dict = {
    "one":1,
    "two":2,
    "three":3,
}

print("one" in num_dict) # 멤버십 연산자는 키에 대해서만 검사
print(1 in num_dict) # False

print(min(num_dict), max(num_dict)) #min(), max() 함수는 키에 대해서만 검사

print(len(num_dict)) # len() 함수는 요소의 개수(키-값 쌍의 개수)를 구함

print("-" * 30)

print(num_dict.get("one")) # get(키) : 키를 이용해서 값을 꺼내오는 함수
print(num_dict.get("four")) # 없는 키도 오류가 발생하지 않음 (None 출력)
#print(num_dict["four"]) #없는 키는 오류가 발생

num_dict.update({
    "three":3.0,
    "four":4,
    "five":5,
}) # update(): 기존의 사전에 입력받은 사전을 병합시킴
print(num_dict)

output = num_dict.pop("three") #pop(키): 키에 해당하는 값을 꺼내옴
print(num_dict)
print(output)