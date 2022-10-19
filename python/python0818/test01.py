# 사전 연산
sample_dict = {
    'name' : '홍길동',
    'age' : 25,
    'height' : 177.7,
    'is_graduated' : True,
    'address' : {
        'city' : '광주광역시',
        'post_code' : 12345,
    }, 
    'hobby' : ['음악 감상','영화 감상', '축구', '게임']
}
print(sample_dict)

print(sample_dict['name'])
print(sample_dict['age'])
print(sample_dict['height']>175)
print(sample_dict['address']['city'])
print(sample_dict['hobby'][1:3])

# sample_dict.clear()
# print(sample_dict)

copy_dict = sample_dict.copy()
print(copy_dict)

print('-' * 50)

stocks = {
    'apple': 50,
    'banana': 70,
    'egg' : 30,
    'bacon' : 100,
}
# 사전 반복 시 키만 추출해서 반복
for key in stocks:
    print(f"품목명: {key}\t|\t 수량: {stocks[key]}")

#print(stocks.keys())     #keys(): 키만 모아서 추출, 목록과 유사한 dict_keys 자료형으로 만듦
for key in stocks.keys():
    print(f"품목명: {key}\t|\t 수량: {stocks[key]}")

# print(stocks.values()) # values(): 값만 모아서 추출, 목록과 유사한 dict_values 자료형으로 만듦
print(stocks.values())
total_stock = 0
for value in stocks.values():
    total_stock += value
print("총 수량: ", total_stock)

#print(stocks.items()) # items(): 키-값 쌍을 튜플로 묶어서 추출, 중첩 목록과 유사한 dict_items 자료형으로 만듦
for item in stocks.items():
    print(f'품목명: {item[0]}\t| 수량: {item[1]}')