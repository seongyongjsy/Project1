# from member import regist
# from member.regist import member_list, regist_member, validate_member
from board.write import board_list, write_board, Board

def main():
    print("프로그램 실행")
    # regist.regist_member()
    # regist.validate_member()
    # print("등록된 회원 목록:", member_list)
    # regist_member()
    # validate_member()
    new_board1 = Board(1, "게시글 테스트1", "admin")
    write_board(new_board1)
    new_board2 = Board(2, "게시글 테스트2", "admin")
    write_board(new_board2)
    print(board_list)

if __name__ == "__main__":
    main()