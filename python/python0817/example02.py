menus = ("파스타", "리조또", "피자", "스테이크", "플래터")
prices = (10000, 10500, 9500, 20000, 14500)
print("가장 저렴한 메뉴 가격: ", min(prices))
print("가장 비싼 메뉴 가격 : ", max(prices))

total_price = 0
print("메뉴판")
print("-"*30)
print(menus)
print(prices)
print("-"*30)
while True:
    menu_num = int(input("메뉴판을 보시고 주문할 메뉴 번호를 입력해주세요(0을 입력하면 종료합니다): "))
    if menu_num == 0:
        break
    else:
        total_price += prices[menu_num -1 ]
    print("총 주문 가격: ", total_price)