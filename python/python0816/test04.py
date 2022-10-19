# 문자열 메소드
# 정렬 관련
from cgi import print_arguments


s = "python"
print("#", s.center(10), "#", sep="") #center(폭): 주어진 폭에서 문자열을 가운데 정렬
print("#", s.ljust(10), "#", sep="") #ljust(폭): 주어진 폭에서 문자열을 왼쪽 정렬
print("#", s.rjust(10), "#", sep="") #rjust(폭): 주어진 폭에서 문자열을 오른쪽 정렬
print("=" * 20)
#검사관련
s1 = "abcd"
s2 = "ABCD"
print(s1.islower()) # islower(): 문자열이 모두 소문자로 이루어져 있는지 검사
print(s1.isupper()) # isupper(): 문자열이 모두 대문자로 이루어져 있는지 검사
print(s2.islower())
print(s2.isupper())

print("=" * 20)
s3 = "1234"
print(s1.isalpha()) # isalpha(): 문자열이 모두 알파벳으로 이루어져 있는지 검사
print(s2.isalpha())
print(s3.isalpha())
print(s1.isnumeric()) # isnumeric(): 문자열이 모두 숫자로 이루어져 있는지 검사
print(s2.isnumeric())
print(s3.isnumeric())

print("=" * 20)

s4 = "  "
print(s1.isspace()) # isspace(): 문자열이 모두 공백으로 이루어져 있는지 검사
print(s2.isspace())
print(s3.isspace())
print(s4.isspace())

print("="*20)

print(s1.startswith("a")) #startswith("문자열"): 원본 문자열이 제시된 문자열로 시작하는지 검사
print(s1.startswith("a")) #endswith("문자열"): 원본 문자열이 제시된 문자열로 끝나는지 검사