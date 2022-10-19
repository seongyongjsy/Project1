from unittest import result
import pymysql

# DB 접속 정보
HOST = 'localhost'
USER = 'kim'
PASSWORD = '1234'
DATABASE = 'python_app'
PORT = 3306

# DB 접속 시도
with pymysql.connect(host=HOST,user=USER, password=PASSWORD, db=DATABASE, port=PORT, 
    charset='utf8', autocommit=True) as con:
    # 커서 객체 생성
    cur = con.cursor()
    
    # 쿼리 실행
    print("1. INSERT / 2. ")
    match int(input()):
        case 1:
            query1 = "INSERT INTO con_test VALUES (%s, %s)"
            query2 = "INSERT INTO con_test VALUES (%s, %s)"
            query3 = "INSERT INTO con_test VALUES (%(a)s, %(b)s)"
            i1 = cur.execute(query1, [7, '손오공'])
            i2 = cur.execute(query2, (8, '사오정'))
            i3 = cur.execute(query3, {'a':9, 'b': '저팔계'})
            print("실행 결과:", i1, i2, i3)

            if i1 == i2 == i3 == 1:
                con.commit()
                print("입력 완료.")
        case 2:
            query = "SELECT * FROM con_test WHERE a BETWEEN %s AND %s"
            cur.execute(query, [4,6])
            # result = cur.fetchall()
            # print(result)

            while True:
                result = cur.fetchone()
                if result is None:
                    print("모든 데이터를 출력했습니다.")
                    break
                else:
                    print(result)
                    input("아무 키나 입력하여 다음 데이터 확인.")
        case 3:
            i = int(input("삭제할 데이터의 ID를 입력하세요: "))
            query = "DELETE FROM con_test WHERE a = %s;"
            result = cur.execute(query, [i])    # 영향을 받은(=삭제된) 행의 개수
            if result > 0:
                print("삭제 성공.") # 삭제된 행이 있는 경우
            else:
                print("삭제 실패.") # 삭제된 행의 개수가 0인 경우 = 삭제 실패
                



