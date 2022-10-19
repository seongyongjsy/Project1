# 상위 폴더를 모듈 지정 경로(sys.path)에 등록해서
# 하위 폴더(member, board, ...) 내 모듈 불러오기 가능

import sys
sys.path.append(r"C:\Workspace\python0823")
from member.regist import regist_member

def main():
    print("프로그램 실행")
    # print(sys.path)
    regist_member()

if __name__ == "__main__":
    main()