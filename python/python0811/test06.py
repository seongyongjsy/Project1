#불변 데이터 (immutable)

# a = 10
# print(a, id(a))

# a += 20
# print(a, id(a))

# a -= 20
# print(a, id(a))

from datetime import datetime


b= "hello"
c = "hi"
d = "hellohi"
print(b, id(b))
print(c, id(c))
print(d, id(d))

e = "hello"
f = "hi"
g = "hello" + "hi"
print(e, id(e))
print(f, id(f))
print(g, id(g))

print('='*10)
#아스키 코드 지원
print(ord("A")) # a => 97
print(chr(97)) #65 => A, 66 => B , 67 => C, .... 97 => a