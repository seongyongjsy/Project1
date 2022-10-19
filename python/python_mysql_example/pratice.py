# 파이썬에서 MYSQL 연동하기
# 0.모듈 불러오기
from unittest import result
import pymysql

# print(pymysql)
# print(dir(pymysql)) # dir(): 모듈에 작성된 요소들을 확인하는 함수

# 1. Connection 객체 생성
# 데이터베이스 접속 정보를 가지고 접속을 시도하는 단계
con = pymysql.connect(
    host='localhost',
    user='kim',
    password='1234',
    database='python_app',
    port=3306,
    charset='utf8')
# print(con)

# 2. Cursor 객체 생성
# 데이터베이스 접속 후 작업 관리를 위한 객체를 생성하는 단계.
cur = con.cursor()
# print(cur)

# 3. 쿼리 실행
# 위에서 생성한 Cursor 객체를 사용해서 쿼리를 실행하는 단계.
query = """
CREATE TABLE con_test (
    a INT,
    b CHAR(10)
)
"""
query = "INSERT INTO con_test VALUES (1,'hello');"
# cur.execute(query)    # execute() 함수를 사용해서 지정된 쿼리를 실행.
query = "SELECT * FROM con_test"
cur.execute(query)
# fetchall(), fetchmany(n), fetchone() 함수를 사용해서 SELECT 실행 결과를 꺼냄
# result = cur.fetchall() # fetchall() 함수를 사용해서 SELECT 실행 결과를 꺼냄.
# result = cur.fetchmany(2) # fetchmany(n): n개의 결과물을 꺼냄.
# result = cur.fetchone() # fetchone(): 1개의 결과물을 꺼냄.
# print(result)   # 각 레코드를 튜플로 묶은 중첩 튜플 형태로 반환.
print("a\tb")
print("-" * 30)
for record in cur.fetchall():
    print(f"{record[0]}\t{record[1]}")

# query = "UPDATE con_test SET b = 'goodbye' WHERE a = 3;"
# query = "UPDATE con_test SET b = 'goodbye';"
# query = "DELETE FROM con_test WHERE a IN (1,2);"
query = "DELETE FROM con_test;"
i = cur.execute(query)  # execute() 실행 결과 영향을 받은 행의 개수를 반환
print(i)

# 3-2. COMMIT 또는 ROLLBACK 실행
# INSERT, UPDATE, DELETE 쿼리 실행 후 commit 실행할 것.
# con.commit()    # Connection 객체를 사용해서 commit 실행
# con.rollback()

# 4. 자원 반납
# 데이터베이스 작업을 완료하고 사용한 자원을 반납하는 단계.
con.close()
# cur.execute(query)    # 접속이 끊어진 후 작업 불가.



