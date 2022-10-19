score_list = [] # 점수를 저장할 목록

def main():
    load_score()    # 프로그램 실행 시, 파일을 읽어서 목록을 초기화하는 함수를 실행
    while True:
        print_main_menu()
        match input_num():
            case 1:
                record_score()
            case 2:
                check_score()
            case 0:
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못 입력하셨습니다.")
                continue
    save_score()  # 반복문이 종료되면, 목록을 파일로 저장하는 함수를 실행

def print_main_menu():
    print("\n<< 점수 기록 프로그램 >>")
    print("1. 점수 기록")
    print("2. 점수 확인")
    print("0. 프로그램 종료")
    print("메뉴 번호를 입력하세요: ", end="")

def input_num():
    result = -1
    try:
        result = int(input())
    except:
        pass
    return result

def record_score():
    print("< 점수기록 >")
    print("점수(0~100)를 입력하세요: ", end="")
    score = input_num()
    if score < 0 or score > 100:
        print("잘못 입력하셨습니다.")
    else:
        score_list.append(score)
        print("기록을 완료했습니다.")

def check_score():
    print("< 점수 확인 >")
    print(score_list)

def load_score():
    """파일에 저장된 점수를 목록에 초기화하는 함수"""
    f= None
    try:
        f = open(r"c:\Workspace\python0824\files.\ex.bin", "rb")
        global score_list
        score_list = list(f.read())
        print("파일을 성공적으로 불러왔습니다.")
    except:
            print("파일 불러오기 오류.")
    finally:
        if f is not None:   # open()은 성공했지만 write() 도중 실패한 경우
            f.close()   # 열린 파일을 닫아서 자원을 반납함


def save_score():
    """기록된 점수 목록을 파일로 저장하는 함수"""
    f= None
    try:
        f = open(r"c:\Workspace\python0824\files.\ex.bin", "wb")
        f.write(bytes(score_list))
        print("기록된 점수를 파일에 저장했습니다.")
    except:
        print("파일 작성 오류.")
    finally:
        if f is not None:   # open()은 성공했지만 write() 도중 실패한 경우
            f.close()   # 열린 파일을 닫아서 자원을 반납함


if __name__ == "__main__":
    main()
