def main():
    while True:
        print_main_menu()
        
        menu_num = 0
        try:
            menu_num = int(input())
            break
        except:
            pass

        match menu_num:
            case 1:
                print("학생 정보 입력 기능 실행")
            case 2:
                print("학생 정보 조회 기능 실행")
            case 0:
                print("프로그램을 종료합니다.")
                break
            case _:
                print("다시 입력해주세요.")


def print_main_menu():
    print("\n학사 관리 프로그램")
    print("1. 학생 정보 입력")
    print("2. 학생 정보 조회")
    print("0. 프로그램 종료")
    print("메뉴 번호를 입력하세요: ", end="")


if __name__ == "__main__":
    main()