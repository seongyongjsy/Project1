"""프로그램을 실행하고 제어하는 주요 기능을 담당하는 파일."""
from re import search
import re
import time
from unittest import result
import product

import order
def main():
    """프로그램을 실행하는 함수."""
    init()
    while True:
        print_main_menu()
        match input_num():
            case 1:  # 상품 조회 및 주문
                print_product_list()
            case 2: # 주문 조회
                print_order_detail()
            case 0:
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못 입력하셨습니다.")
                continue

def init():
    """프로그램의 기본 설정을 초기화 하는 함수."""
    print("상품 목록 로딩 중")
    start = time.time()
    product.save_product()  # 상품 목록을 생성, 상품 데이터를 초기화
    order.load_order() # 저장된 파일로부터 주문 내역을 가져와서 세팅함
    end = time.time()
    print("상품 목록을 불러오는데 성공했습니다.")
    print("소요 시간:", end-start, "초")
    print("="*50)

def print_main_menu():
    """메인 메뉴를 출력하는 함수."""
    print()
    print("<< K-Digital 쇼핑물 >>")
    print("1. 상품 조회 및 주문")
    print("2. 주문 조회")
    print("0. 프로그램 종료")
    print("-"*30)
    print("메뉴 번호를 입력해 주세요: ", end="")


def input_num():
        """숫자를 입력받아서 반환하는 함수."""
        result = -1
        try:
            result = int(input())
        except:
            pass
        return result 


def print_product_list():
    """상품 목록을 출력하는 함수."""
    print()
    print("< 상품 목록>")
    product_list = product.get_product_list()
    if product_list:
        print(f"{'상품ID':8^}\t{'상품명':8^}\t{'가격':8^}\t{'수량':8^}")
        print("-"*50)
        for item in product_list:
            print(f'{item.id:8^}{item.name:8^}\t{item.price:8^}\t{item.amount:8^}')
    else:
        print("등록된 상품이 없습니다.")


def order_product():
    """상품ID를 입력받아서 주문을 진행하는 함수."""
    basket = {}
    while True:
        print("주문할 상품ID를 입력하세요(0을 입력하면 중단합니다.): ", end="")
        product_id = input()
        if product_id == "0":
            break
        search_result = product.check_id(product_id)
        if search_result is None:
            print("상품ID를 다시 입력해주세요.")
            continue
        print("구매할 수량을 입력하세요: ", end="")
        amount = input_num()
        if amount > search_result.amount:
            print("남아있는 수량보다 더 많이 입력하셨습니다.")
            continue
        basket[product_id] = amount
    
    print("장바구니:", basket)
    if input("정말 구매하시겠습니까? [y/N]") == "y":
        order.save_order(basket)
        print("-구매 처리 중-")
    else:
        print("주문을 취소했습니다.")


def print_order_list():
    """전체 주문 목록을 출력하는 함수"""
    print()
    print("< 주문 조회>")
    order_list = order.get_order_list()
    if order_list:
        print(f"{'주문ID'}\t{'주문일'}")
        print("-"*50)
        for item in order_list:
            print(f"{item.id}\t{item.date}")
    else:
        print("주문 내역이 없습니다.")


def print_order_detail():
    """주문ID를 입력받아서 상세 조회를 실행하는 함수."""
    print("상세 조회할 주문ID를 입력하세요 : ", end="")
    order_id = input()
    result = order.search_order(order_id)
    if result:
        for item in result.order_list.items():
            if item[0] in goods:
                pr = goods

        print(item[0], pr.name, item[1], pr.price * item[1])
    else:
        print("주문ID를 확인해주세요.")

def shutdown_program():
    """프로그램을 종료하기 전 처리할 내용을 작성하는 함수."""
    print("주문 내역을 파일로 저장하는 중입니다.")
    order.save_file()
    print("주문 내역을 저장했습니다.")
    print("=" * 50)
    print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()



