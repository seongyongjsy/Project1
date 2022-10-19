"""상품과 관련된 처리를 하는 모듈."""
product_list = [] # 상품 목록을 저장할 list 변수

class Product:
    """상품 관련 데이터를 저장할 때 사용할 클래스."""
    pass
    def __init__(self, id, name, price, amount) -> None:
        self.id = id # 상품 ID
        self.name = name # 상품명
        self.price = price # 가격
        self.amount = amount # 수량

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"

    # in 연산자와 함꼐 사용 시, 상품ID값을 검사하도록 동작시킴
    def __contains__(self, product_id):
        return self.id == product_id


def get_product_list():
    """상품 목록을 반환하는 함수"""
    return product_list

def save_product():
    """쇼핑몰에서 판매하는 상품 데이터를 생성, 저장하는 함수."""
    # 하드 코딩: 값을 입력할 때 직접 작성하는 방식 <-> 동적 할당

    product_list.append(Product("0001", "가방", 30000, 10))
    product_list.append(Product("0001", "신발", 40000, 20))
    product_list.append(Product("0001", "모자", 10000, 5))
    product_list.append(Product("0001", "자켓", 50000, 30))



def check_id(product_id):
    """전달받은 상품ID가 실존하는 상품ID인지 검사하는 함수."""
    for item in product_id:
        if product_id == item.id:
            return item
    return None