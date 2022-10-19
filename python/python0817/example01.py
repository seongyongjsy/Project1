# 목록 예제 - 숫자를 반복적으로 입력받아서 목록에 저장하고,
# 입력받을 때 sum 을 입력하면 목록에 저장된 모든 요소들의 합계를 출력하기

while True:
    input_text = input("숫자를 입력하세요: ")
    if input_text == "sum":
        total_value = 0
        for num in num_list:
            total_value += num
        print("입력하신 숫자의 합계는 다음과 같습니다. : ", total_value)
        break

    input_num = float(input_text)
    num_list = []
    num_list.append(input_num)



   