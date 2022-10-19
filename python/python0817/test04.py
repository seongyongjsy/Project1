from pkgutil import extend_path


num_tuple = 10, 20, 30

# 튜플은 불변 자료형이기 때문에 기존 튜플을 수정하는 조작은 불가능
# num_tuple.append(40)
# num_tuple.insert(40)
# num_tuple.extend((40,50))

# num_tuple[1] = 200
# num_tuple[1:3] = (200, 300)

##################################

extend_tuple = (10, 20) + (30, 40) # 새로운 튜플 생성
print(extend_tuple)
multiple_tuple = (10,) * 3 # 새로운 튜플 생성
print()
