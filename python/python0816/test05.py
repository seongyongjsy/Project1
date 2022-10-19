# 문자열 메소드
# 변경
s1 = "Hello, World!"
print(s1.replace("Hello", "Hi"))
s2 = s1.replace("Hello", "Hi").replace("World","Students")
print(s2)
s3 = s1.replace("Hello", "Hi").replace("World","Students").replace("!","?")
print(s3)

print("-" * 20)

s4 = " Hello  World  "
print("#", s4.lstrip(),"#", sep = "") #lstrip(): 왼쪽의 공백을 제거
print("#", s4.rstrip(),"#", sep= "") # rstrip(): 오른쪽의 공백을 제거
print("#",)

# 분할 / 접합
s5 = "Hello, World! Hi, Students!"
print(s5.split()) #split("기준"): 문자열을 제시된 기준으로 잘라서 목록으로 만듦
for substr in s5.split():
    print(substr)
print(s5.split("!"))

print("-"*20)

substr_list = s5.split()
print("&nbsp;".join(substr_list)) # "붙일 사이 문자열". join([붙일 대상 목록]): 문자열을 접합시킴
print("\n".join(substr_list))