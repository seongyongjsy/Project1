# 인덱스 : 순번 , 특정 문자가 몇 번째 있는지 그 번호를 의미
# 인덱싱 : 인덱스를 사용하여 부문 문자를 추출하는 문법
# 슬라이싱 : 인덱스를 사용하여 부문 문자열을 추출하는 문법

s = "Hello, Students. I`m teacher."
print(s)

print("=" * 50)

# 인덱싱
print(s[0]) # 0번 인덱스의 문자(=첫 번째 문자) 추출
print(s[1]) # 1번 인덱스의 문자(=두 번째 문자) 추출
print(s[2]) # 2번 인덱스의 문자(=세 번째 문자) 추출
print(s[28]) # 28번 인덱스의 문자(=마지막 문자) 추출
#print(s[29]) # 29번 인덱스의 문자 추출 => 존재하지 않으므로 오류 발생
print(s[-1]) # -1번 인덱스의 문자(=마지막 문자) 추출

print("=" * 50)

# 슬라이싱
print(s[0:5]) # 0~4번 인덱스의 문자열 추출
print(s[7:15]) # 7~14번 인덱스의 문자열 추출
print(s[21:29]) # 21~29번 인덱스의 문자열 추출 => 범위를 벗어난 인덱스도 처리 가능
print(s[-8:-1]) # -8~-2번 인덱스의 문자열 추출
print("-" * 20)
print(s[:16]) # 처음부터 15번 인덱스 까지 문자열 추출
print(s[17:]) # 17번 인덱스부터 끝까지 문자열 추출
print(s[:]) # 처음부터 끝까지 문자열 추출
print("-"* 20)
print(s[5:23:2]) # 5~22번 인덱스의 문자열을 2개씩 건너뛰어가며 추출
print(s[::3]) # 처음부터 끝까지 문자열을 3개씩 건너뛰어가며 추출