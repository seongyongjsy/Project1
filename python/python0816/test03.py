# 문자열 메소드
# 철자 관련
s1 = "Hello, World! Hi, Students!"
print(s1.lower())# lower(): 모든 알파벳을 소문자로 변환
print(s1.upper())# upper(): 모든 알파벳을 대문자로 변환
print(s1.title())# title(): 각 단어의 첫 글자를 대문자로 , 나머지는 소문자로 변환
print(s1.capitalize()) # capitalize(): 맨 첫 글자를 대문자로, 나머지는 소문자로 변환

print("=" * 30)

# 탐색 관련
s2 = "apple banana orange apple orange orange"
print(s2.find("apple"))     # find(): 문자열을 찾을 때 사용하는 함수
print(s2.find("banana"))
print(s2.find("orange"))
print(s2.rfind("apple"))
print(s2.rfind("banana"))
print(s2.rfind("orange"))
print(s2.find("orange", 14))    # 어디서부터 찾을지 시작 인덱스 설정 가능
print(s2[14:].find("orange")+14)
print(s2.find("orange",14 , 26)) # 어디서부터 어디까지 찾을 지 시작 및 끝 인덱스 설정 가능
print(s2.find("melon")) # 못찾으면 -1

print(s2.index("apple"))  # index(): 문자열을 찾을 때 사용하는 함수. 찾은 문자열의 위치를 인덱스로 계산
#print(s2.index("melon")) # 못찾으면 오류

print(s2.count("apple")) # count(): 문자열이 몇 개 있는지 찾을 때 사용하는 함수
print(s2.count("banana"))
print(s2.count("orange"))
print(s2.count("melon"))