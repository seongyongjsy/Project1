from textwrap import shorten
import pymysql

# 데이터베이스 접속 정보.
HOST = 'localhost'
USER = 'kim'
PASSWORD = '1234'
DATABASE = 'python_app'
PORT = 3306

# 데이터베이스 연동을 위한 객체
CONNECTION = None;
CURSOR = None;

# 데이터베이스 관련 작업 시 사용할 쿼리.
WRITE_BOARD_QUERY = "INSERT INTO board (title, writer, content) VALUES (%s, %s, %s)"
READ_BOARD_QUERY = "SELECT board_id, title, writer, date FROM board ORDER BY board_id DESC"
READ_DETAIL_QUERY = "SELECT * FROM board WHERE board_id = %s"

def main():
    """프로그램의 실행 부분을 담당하는 주요 함수."""
    init()

    while True:
        print_main_menu()

        menu_num = -1
        try:
            menu_num = int(input())
        except:
            pass

            match menu_num:
                case 1:
                    write_board()
                case 2:
                    read_board()
                case 0:
                    print("프로그램을 종료합니다.")
                    break
                case _:
                    print("다시 입력해 주세요.")
                    continue

    shutdown_database()

def shutdown_database():
    """데이터베이스 연동을 종료하는 함수."""
    try:
        global CONNECTION
        if CONNECTION is not None:
            CONNECTION.close()
    except Exception as e:
        print(e)


def read_board():
    """게시글 조회 기능."""
    print()
    print("[ 게시글 조회 ]")
    try:
        if CURSOR is not None:
            # walrus operator: assignment expression, 대입 표현식
            # 조건식에서 변수를 선언하고 함수 등의 실행 결과로 초기화한 후,
            # 조건문 본문에서 변수를 사용할 때 쓰는 연산자
            if (i := CURSOR.execute(READ_BOARD_QUERY)) > 0:
                # 전체 게시글 조회
                print(f"{i} 건의 게시글이 존재합니다.")
                result = CURSOR.fetchall()
                print("번호\t제목\t\t작성자\t작성일")
                print("-" * 50)
                for record in result:
                 print(f"{record[0]}\t{shorten(record[1], 8, placeholder=''):8}\t{record[2]}\t{record[3]:%Y-%m-%d}")
                
                # 상세 게시글 조회
                board_id = int(input("상세 조회할 게시글의 번호를 입력하세요:"))
                if (j := CURSOR.execute(READ_DETAIL_QUERY, (board_id,))) > 0:
                    print(CURSOR.fetchone())
                else:
                    print("등록된 게시글이 없습니다.")
    except Exception as e:
            print(e)


def write_board():
    """게시글 작성 기능."""
    print()
    print("[ 게시글 작성 ]")
    title = input("제목을 입력하세요:")
    writer = input("이름을 입력하세요:")
    content = input("내용을 입력하세요:")
    try:
        if CURSOR is not None:
            if CURSOR.execute(WRITE_BOARD_QUERY, (title, writer, content)) > 0:
                print("작성을 완료했습니다.")
            else:
                print("작성에 실패했습니다.")
    except Exception as e:
        print(e)


def print_main_menu():
    """메인 메뉴를 출력하는 함수."""
    print()
    print("[ 자유게시판 ]")
    print("1. 게시글 작성")
    print("2. 게시글 조회")
    print("-" * 30)
    print("메뉴 번호를 입력해 주세요: ", end="")


def init():
    """프로그램 동작을 위해 필요한 데이터들을 초기화하는 함수"""
    try: 
        global CONNECTION, CURSOR  
        CONNECTIOM = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT,
            charset='utf8',
            autocommit=True
            )
        CURSOR = CONNECTION.cursor()  
    except Exception as e:
        print("데이터베이스 연동 오류")
        print(e)


class Board:
    """게시글을 나타내는 클래스."""

    def __init__(self, board_id, title, writer, content, date) -> None:
        self.board_id = board_id
        self.title = title
        self.writer = writer
        self.content = content
        self.date = date 

        def __repr__(self):
            return f"{self.board_id=}\t{self.board_title=}"



if __name__ == "__main__":
    main()


