# 컬렉션 예제 - 학사 관리 프로그램
student_list = [] # 학생 정보를 저장할 목록

while True:
    print()
    print("<< 학사 관리 프로그램 >>")
    print("1. 학생 등록")
    print("2. 전체 조회")
    print("3. 학번 검색")
    print("4. 학생 수정")
    print("5. 학생 삭제")
    print("0. 종료")
    print("-"*20)

    # 메뉴 번호를 입력받아서 해당 기능 실행
    match int(input("메뉴 번호를 입력하세요: ")):
        case '1' : # 학생 등록
            print("<학생 등록>")
            num = int(input("학번을 입력하세요: "))
            name =    input("이름을 입력하세요")
            age =     input("나이를 입력하세요: ")
            grade = int(input("학년을 입력하세요: "))
            new_student = {
                "num" : num,
                "name" : name,
                "age" : age,
                "grade" : grade,
            }
            student_list.append(new_student)
            print("등록이 완료되었습니다.")
        case '2' : # 전체 조회
            print()
            print(" <전체조회> ")
            print("-" * 50)
            if student_list:   # 목록의 요소가 있으면 True , 빈 목록이면 False 로 취급 가능
                print(" 학번\t이름\t나이\t학년")
                print("-"*30)
                for student in student_list:
                    print(f"{student['num']}\t{student['name']}\t{student['age']}\t{student['grade']}")
            else:
                print("등록된 학생이 없습니다.")
        case '3' : # 학번 검색
            print()
            print('<학번 검색>')
            student_num = int(input("검색할 학생의 학번을 입력하세요: ")) # 검색할 학번

            result = None # 검색 결과를 저장할 변수
            for student in student_list: # 반복문을 통해서 모든 학생 정보를 하나씩 꺼내오며 검사
                if student_num == student["num"]: # 이번 반복에서 꺼내온 학생의 학번이 일치하는 경우
                    result = student # 검색 결과에 학생 정보를 저장
                    break # 결과를 찾아서 더이상 반복할 필요가 없으니 반복을 중단

            if result:
                # result가 사전 값인 경우, 검색 결과 일치하는 학생 정보를 찾은 경우
                print(" 학번\t이름\t나이\t학년")
                print("-"*30)
                print(f"{result['num']}\t{result['name']}\t{result['age']}\t{result['grade']}")
            else: 
                # result = None 인 경우, 검색 결과 일치하는 학생 정보를 찾지 못한 경우
                print("검색 결과를 찾지 못했습니다.")
        case '4' : # 학생 수정
            print()
            print('<학번 검색>')
            student_num = int(input("수정할 학생의 학번을 입력하세요: "))
            
            result = None
            for student in student_list:
                if student_num == student["num"]:
                    result = student
                    break

            if result:
                print("학번\t이름\t나이\t학년")
                print("="*30)
                print(f"{result['num']} {result['name']}\t{result['age']} {result['grade']} ")
                re_name =    (input("수정할 이름:"))
                re_age  = int(input("수정할 나이:"))
                re_grade= int(input("수정할 학년:"))
                result["name"] = re_name
                result["age"]  = re_age
                result["grade"]= re_grade
                print("수정이 완료되었습니다.")
            else:
                print("입력하신 학번에 일치하는 정보를 찾지 못했습니다.")
        case '5' : # 학생 삭제
            print()
            print('<학번 검색>')
            student_num = int(input("삭제할 학생의 학번을 입력하세요: "))
            
            result = False # 삭제 성공 여부를 저장할 변수
            i = 0 # 인덱스를 나타낼 변수
            while i < len(student_list): # 목록에 저장된 요소의 개수만큼 반복
                if student_num == student_list[i]["num"]: # 삭제할 학번이 이번 반복에서 꺼내온 학생의 학번과 일치하는
                    del student_list[i] # 저장된 정보 삭제 시도
                    result = True # 삭제 성공 여부를 True로 변경
                    break # 삭제한 후 더 이상 반복할 필요가 없으므로 break
                i += 1

            if result:
                print("학생 정보를 삭제하는데 성공했습니다.")
            else:
                print("일치하는 학생 정보를 찾지 못했습니다.")
        case '0' : # 종료
            print("프로그램을 종료합니다.")
            break
        case _: # 잘못 입력한 경우
            print("다시 입력해주세요.")
            continue