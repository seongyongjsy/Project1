# 검색어를 입력받아서 주어진 텍스트에서 검색을 시도한다.

# 검색 결과, 일치하는 단어가 없으면 
# 일치하는 결과가 없다고 안내메세지를 출력하고 다시 검색할지 여부를 묻기
# y를 입력하면 다시 검색어를 입력받고, 다른 값을 입력하면 그대로 프로그램 종료

# 검색 결과, 일치하는 단어가 있으면, 일치하는 결과가 몇 개 있는지 출력하고 교체할 단어를 입력받음
# 몇 번째 단어를 교체할지 입력
# 교체 결과 출력하고 프로그램 종료

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

while True:
    print("<<본문>>")
    print("-"*50)
    print(text)
    print("-"*50)
    search_word = input("검색어를 입력하세요: ")

    #if text.find(search_word) > -1:
    if search_word in text:
        #본문에 검색어가 있는경우
        print(f"일치하는 검색 결과를{text.count(search_word)}건 찾았습니다.")
        change_word = input("교체할 단어를 입력하세요: ")
        num = int(input("교체할 순번을 입력하세요:")) # 교체할 순번
        
        re_text = "" # 교체된 텍스트
        i = 1 # 현재 순번
        for subtext in text.split(search_word):
            re_text += subtext # 교체된 텍스트에 기존 텍스트 덩어리를 붙임
            if i == num:    # 현재 반복 중인 순번이 교체할 순번이 맞는지 확인
                re_text += change_word  # 일치하면 교체할 단어를 붙임
            else:
                re_text += search_word  # 일치하지 않으면 기존 단어를 붙임
            i += 1
        re_text = re_text[:-len(search_word)]    #맨 마지막 추가된 필요없는 검색어 덩어리를 제거
        
        print("<< 교체 결과 >>")
        print("-"*50)
        print(re_text)
        print("-"*50)
        # 프로그램 강제 종료 코드
        import sys
        sys.exit(0) 
    else:
        #본문에 검색어가 없는경우
        selection = input("검색 결과가 없습니다. 다시 검색하시겠습니까? (y/N): ")
        if selection == "y":
            print()
            continue
        else:
            print("프로그램을 종료합니다.")
            break
# 프로그램 강제 종료 코드
import sys
sys.exit(0)