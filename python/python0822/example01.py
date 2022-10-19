# 함수 예제 - 레스토랑 주문 프로그램
menu_list = "파스타", "리조또", "피자", "스테이크", "콜라"
price_list = 8000, 8000, 14000, 22000, 3000
order_list = [] # 주문 내역을 저장할 목록 변수

from datetime import datetime
order_str = f"{datetime.now():%Y%m%d}" # 프로그램 실행 시점의 년월일을 문자열로 구성
order_idx = 0 # 주문 번호를 설정할 때 사용할 변수

def main():
    """이 스크립트를 실행했을 때, 실행될 함수.
    프로그램의 주 기능을 담당한다."""
    while True: # 무한 반복문을 통해서 프로그램을 지속적으로 실행한다.
        print_main_menu() # 주 메뉴를 출력한다
        match int(input()): # 메뉴 번호를 입력받는다.
            case 1: # 주문 입력
                insert_order()
            case 2: # 주문 조회
                print_all_order()
            case 0: # 프로그램 종료
                print("프로그램을 종료합니다.")
                break
            case _: # 잘못 입력한 경우
                print("다시 입력해주세요.")
                continue                


def print_main_menu():
    """주 메뉴를 출력하는 함수."""
    print("=" * 30)
    print("레스토랑 주문 관리 프로그램")
    print("=" * 30)
    print("1. 주문 입력")
    print("2. 주문 조희")
    print("0. 프로그램 종료")
    print("=" * 30)
    print("메뉴 번호를 입력해 주세요:", end="")

def insert_order():
    """주문 입력 기능"""
    print()
    print("<< 주문 입력 >>")
    print_restaurant_menu()  #메뉴판 출력

    # 메뉴 번호를 이용해서 주문을 입력받음
    order_menu = {} # 주문 내역을 저장할 사전. 메뉴번호: 수량 형식으로 저장함
    while True:
        menu_num = int(input("주문할 메뉴 번호를 입력해주세요(0을 입력하면 중단합니다): "))
        if menu_num == 0: # 주문할 메뉴 번호 입력을 중단하는 경우
            break
        elif menu_num < 1 or menu_num > 5: # 없는 메뉴 번호를 입력한 경우
            print("다시 입력해주세요.")
        else:
            if menu_num in order_menu:  # 이미 주문한 적 있는 메뉴인 경우
                order_menu[menu_num] += 1 #기존 값 +1 누적 
            else: # 처음 주문한 메뉴인 경우
                order_menu[menu_num] = 1 # 새 값 1 추가

    
   
    result_order = print_order(order_menu)  # 주문한 내역을 출력하고 최종 주문 내역 사전 변수를 반환받음
    order_list.append(result_order) # 최종 주문 내역을 저장
    print("주문을 입력했습니다.")

def print_restaurant_menu():
    """주문 입력 시 사용할 메뉴판 출력 기능"""
    print()
    print("<< 주문 입력>>")
    print("   메뉴\t\t가격")
    print("-"*30)
    print("1. 파스타\t8000")
    print("2. 리조또\t8000")
    print("3. 피자\t\t14000")
    print("4. 스테이크\t22000")
    print("5. 콜라\t\t3000")
    print("-"*30)

     
def print_order(order_menu):
    """주문 내역을 저장한 사전 변수를 전달받아 출력하는 함수."""
    print("주문 내역")
    print("메뉴명\t수량\t가격")
    print("-"*30)
    total_price = 0 # 총 주문 금액을 누적할 변수
    for item in order_menu.items():    # 반복문을 통해 메뉴명, 수량, 가격을 출력하며 금액을 누적 
        print(f"{menu_list[item[0] - 1]:8}\t{item[1]}\t{item[1] * price_list[item[0]]-1}")
        total_price += item[1] * price_list[item[0] - 1] # 총 주문 금액을 누적
    print("총 주문 금액:", total_price)
    
    global order_idx # 함수 본문에서 order_idx 변수를 조작하기 위한 코드 추가.
    result_order = {}   # 최종 주문 내역을 저장할 사전 변수.
    result_order["order_num"] = order_str + f"{order_idx:02}"   # 주문 번호를 추가
    result_order["order_list"] = order_menu # 주문 내역을 추기
    result_order["total_price"] = total_price   # 총 주문 금액을 추가
    
    order_idx += 1 # 주문 번호 1 증가

    return result_order # 최종 주문 내역 사전을 반환.

def print_all_order():
    """입력받은 모든 주문 내역을 요약 출력하는 함수."""
    print()
    print("<<주문 내역 조회>>")
    if order_list: # order_list의 요소가 있는 경우
        print("주문번호\t총주문금액")
        print("-"* 30)        
        for order in order_list:    # 반복문을 통해 모든 주문 데이터를 요약해서 출력
            print(f"{order['order_num']}\t{order['total_price']}")
        order_num = input("상세 조회할 주문 번호를 입력하세요: ")
        search_result = search_order(order_num) # 입력받은 주문 번호에 해당하는 데이터 검색
        if search_result: # 해당 데이터가 있는 경우
            print(f"주문 번호: {search_result['order_num']}")
            for item in search_result["order_list"].items():
                print(f"{menu_list[item[0]-1]:8}\t{item[1]}")
            print("총 주문 금액:", search_result['total_price'])
        else:   # 데이터를 찾지 못한 경우
            print("입력하신 주문 번호와 일치하는 데이터를 찾지 못했습니다.")
    else: # order_list의 요소가 없는 경우.
        print("주문 내역이 없습니다.")


def search_order(order_num):
    """주문 번호를 전달받아 해당 번호의 데이터를 찾아서 반환하는 함수."""
    for order in order_list:
        if order_num == order["order_num"]:   
        # 입력받은 주문 번호와 저장된 주문 데이터의 번호가 일치하는 경우
            return order # 찾은 주문 데이터를 반환
    return None     # 주문 데이터를 못 찾은 경우

main() # 스크립트 파일이 실행되면  main() 함수를 실행