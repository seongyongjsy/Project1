def input_number():
    result = 0
    try:
        result = int(input())
    except:
        pass
    return result


print("학번을 입력하세요: ", end="")
student_num = input_number()

if student_num == 0:
    print("잘못 입력하셨습니다.")
else:
    print(student_num, "학번에 대해 검색을 시도합니다...")
print("...")
