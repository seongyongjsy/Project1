# 문자열 메소드 예제
text = "apple banana orange" * 10
start_index = 0

while True:
    input_text = input("\n검색어를 입력하세요: ")
    result = text.find(input_text, start_index)

    if result < 0:
        print("해당 검색어를 찾을 수 없습니다...")
        break
    else:
        print(input_text,"을(를)", result+1, "번째 위치에서 찾았습니다!")
        if input("계속해서 다음 위치를 찾으시겠습니까? (y/n)") == "y":
            start_index += len(input_text) + result
        else:
            break