from member import * # *(와일드 카드): 전부 선택
# from member import join, login
# from member.join import member_join
# from member.login import member_login

def main():
    print("프로그램 실행")
    join.member_join()
    login.member_login()
    # member_join()
    # member_login()

if __name__ == "__main__":
    main()
