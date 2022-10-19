"""주문 관련 기능을 작성하는 파일."""
import os
import datetime
import pickle
from tabnanny import check

index = 0 

class Order:
    """주문 정보를 저장하는 클래스."""

    def __init__(self, order_list) -> None:
        self.id = self.generate_order_id()   #주문ID
        self.order_list = order_list    #주문 상품 목록
        self.date = self.get_order_date() #주문일

    def generate_order_id(self):
        """객체 생성 시, 주문ID를 자동으로 생성해주는 메소드."""
        global index
        index += 1
        while True:
            checked = False
            # 반복문을 통해 현재 설정하고자 하는 인덱스가 이미 사용 중인지 검사
            for item in order_list:
                if f"{index:02}" == item.id.split("-")[1]:
                    checked = True
            if checked: # 이미 사용 중인 인덱스라면,
                index += 1  # 인덱스를 1 증가시키고 다시 검사
            else:   #사용할 수 인덱스의 경우
                break   # 반복문을 중단하고 검사 종료
        return f"{datetime.datetime.now():%Y%}"

    def get_order_date(self):
        """실시간 주문 날짜시간을 구하는 함수."""
        return f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"

    def __repr__(self):
        return f"{self.id} - {self.date}"

def load_order():
    """프로그램 종료 시, 주문 내역을 파일로 저장하는 함수."""
    file_path = r"C:\Workspace\shopping_project\files"
    today_str = f"{datetime.datetime.now():%m%d}"
    # file_path += "\\" + today_str + ".bin"
    file_path += "\\" + "test" + ".bin"

    # 파일이 없는 경우 새 파일을 생성해서 빈 목록을 저장.
    # 파일이 있으면 파일을 읽어서 주문 내역을 초기화.
    if not os.path.exists(file_path):
        with open(file_path, "wb") as f:
            pickle.dump([],f)
    else:
        with open("file_path","rb") as f: 
          global order_list
          order_list = pickle.load(f)

def save_order(new_order_list):
    """새 주문 목록을 전달받아서 저장하는 함수."""
    order_list.append(Order(new_order_list))

def get_order_list():
    """주문 목록을 입력받아서 """
    
def search_order(order_id):
    """전달받은 주문ID와 일치하는 주문 데이터를 찾아서 반환하는 함수."""
    for item in order_list:
        if order_id == item.id:
            return item
    return None


def save_file():
    """프로그램 종료 시, 주문 내역을 파일로 저장하는 함수."""
    file_path = r"C:\Workspace\shopping_project\files"
    today_str = f"{datetime.datetime.now():%m%d}"
    file_path += "\\" + today_str + ".bin"

    with open("file_path","wb") as f: 
        pickle.dump(order_list, f)


