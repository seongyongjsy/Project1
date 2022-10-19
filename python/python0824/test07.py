num_list = [1, 2, 3, 4, 5]
# print(bytes(num_list))
# print(bytearray(num_list))

# f = open(r"c:\Workspace\python0824\files\test02.txt","wb")
# f.write(bytes(num_list))  #bytes: 불변 바이너리 시퀀스
# f.write(bytes(num_list))    #bytearray: 가변 바이너리 시퀀스
# f.close()

f = open(r"c:\Workspace\python0824\files\test02.txt", "rb")
# print(f.read())    # bytes 자료형으로 가져옴
print(list(f.read()))
f.close()