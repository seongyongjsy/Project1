-- CHECK 제약조건: 데이터를 입력할 때 CHECK 조건을 만족하는지 검사하는 제약조건.
USE school;
DROP TABLE student_physical_test;
CREATE TABLE student_physical_test (
	test_id INT UNSIGNED,
    student_id INT UNSIGNED,
    height DECIMAL(5, 2) CHECK (height > 0 AND height < 500.00),
    weight DECIMAL(5, 2) CHECK (weight > 0 AND weight < 500.00)
);

INSERT INTO student_physical_test VALUES(1, 1, 175.01, 66.66);
INSERT INTO student_physical_test VALUES(1, 1, 177.77, 77.77);
INSERT INTO student_physical_test VALUES (2, 2, 0, -1.23);
SELECT * FROM student_physical_test;

# 제약조건 확인
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME LIKE 'student_physical_test';
# 제약조건 이름을 이용해서 CHECK 제약조건 제거
ALTER TABLE student_physical_test DROP CONSTRAINT student_physical_test_chk_1;
ALTER TABLE student_physical_test DROP CONSTRAINT student_physical_test_chk_2;


-- AUTO_INCREMENT: 데이터를 입력할 때 자동으로 증가하도록 설정하는 문법.
-- 주로 PK와 같이 사용함
-- 정수 자료형에 대해서 적용 가능.
CREATE TABLE qna_board(
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(30) NOT NULL,
    student_id INT UNSIGNED
);
INSERT INTO qna_board (title, student_id) VALUES ('1등', 1);
INSERT INTO qna_board (title, student_id) VALUES ('2등', 2);
INSERT INTO qna_board (title, student_id) VALUES ('게시글 제목', 2);
SELECT * FROM qna_board;

-- 테이블 상태 조회 쿼리. 테이블 행 개수, 데이터 길이(크기), AUTO_INCREMENT 값 등을 조회 가능.
SHOW TABLE STATUS; # 현재 DB 내 모든 테이블의 상태를 조회하는 쿼리.
SHOW TABLE STATUS FROM school; # school DB 내 모든 테이블의 상태를 조회하는 쿼리.
SHOW TABLE STATUS LIKE 'qna_board'; # 현재 DB 내 'qna_board' 테이블의 상태를 조회하는 쿼리.
SHOW TABLE STATUS FROM school LIKE 'qna_board'; # school DB 내 'qna_board' 테이블의 상태를 조회하는 쿼리.

DELETE FROM qna_board WHERE id = 2;
INSERT INTO qna_board (title, student_id) VALUES ('2등 어디감', 1);
DELETE FROM qna_board WHERE id = 4;
INSERT INTO qna_board (title, student_id) VALUES ('내 글 어디감?', 1);
DELETE FROM qna_board;
INSERT INTO qna_board (title, student_id) VALUES ('게시판 왜이럼?', 1);

ALTER TABLE qna_board AUTO_INCREMENT = 1;
INSERT INTO qna_board (title, student_id) VALUES ('?', 1);
SELECT * FROM qna_board;

/*
SQL 문법
초급
- DDL: CREATE, DROP
- DML: SELECT, INSERT, UPDATE, DELETE
- 테이블 구조: 데이터베이스(스키마), 테이블, 열(필드), 행(레코드)
- 자료형: 정수, 실수, 문자열, 날짜
- 연산자: 산술, 비교, 논리, ...
- 함수: 기초 자료형 관련 함수, 기타 함수
중급
- DOL: ALTER
- 그룹 함수, 그룹화
- 제약 조건
고급
- 조인
- 서브쿼리
- 트랜잭션 관리
- 사용자 계정 관리
- 파이썬 프로그램 연동 */


-- 조인(JOIN): 두 개 이상의 테이블을 묶어서 데이터를 조회하는 문법.
USE test_db;
CREATE TABLE A(
	A_a INT,
    A_b CHAR(20)
);
CREATE TABLE B(
	B_a INT,
    B_b CHAR(20)
);
INSERT INTO A VALUES (1, 'A 1번 행');
INSERT INTO A VALUES (2, 'A 2번 행');
INSERT INTO B VALUES (1, 'B 1번 행');
INSERT INTO B VALUES (3, 'B 2번 행');
SELECT * FROM A;
SELECT * FROM B;

-- 1. 크로스 조인(CROSS JOIN) : 각 테이블 내 레코드들의 모든 조합을 구하는 쿼리.
SELECT * FROM A CROSS JOIN B ORDER BY A_a, B_a;
SELECT * FROM A CROSS JOIN B ORDER BY B_a, A_a;
SELECT * FROM A, B ORDER BY A_a, B_a;  # 크로스 조인 간단 표현 방식
SELECT * FROM B, A ORDER BY B_a, A_a;  
SELECT A_a, B_a FROM A CROSS JOIN B ORDER BY A_a, B_a;
SELECT B_a, A_a FROM B CROSS JOIN A ORDER BY B_a, A_a;

-- 2. 내부 조인(INNER JOIN): 지정한 열들의 값이 일치하는 경우만 선택하는 방식.
SELECT * FROM A INNER JOIN B ON A.A_a = B.B_a;
SELECT * FROM B INNER JOIN A ON B.B_a = A.A_a;
SELECT * FROM A, B WHERE A.A_a = B.B_a; # 이너 조인 간단 표현 방식
SELECT * FROM B, A WHERE B.B_a = A.A_a; # EQUI-JOIN 

-- 3. 외부 조인(OUTER JOIN)
-- 3-1. 좌측 조인(LEFT JOIN): 두 테이블 간에 일치하는 레코드와, 좌측 테이블의 레코드를 출력하는 방식.
SELECT * FROM A LEFT OUTER JOIN B ON A.A_a = B.B_a;
SELECT * FROM B LEFT OUTER JOIN A ON B.B_a = A.A_a;
-- 3-2. 우측 조인(RIGHT JOIN): 두 테이블 간에 일치하는 레코드와, 우측 테이블의 모든 레코드를 출력하는 방식.
SELECT * FROM A RIGHT OUTER JOIN B ON A.A_a = B.B_a;
SELECT * FROM B RIGHT OUTER JOIN A ON B.B_a = A.A_a;
-- 3-3. 전체 조인(FULL JOIN)
SELECT * FROM A FULL JOIN B ON A.A_a = B.B_a;
SELECT * FROM A LEFT OUTER JOIN B ON A.A_a = B.B_a
UNION
SELECT * FROM A RIGHT OUTER JOIN B ON A.A_a = B.B_a;
SELECT * FROM B LEFT OUTER JOIN A ON B.B_a = A.A_a
UNION
SELECT * FROM B RIGHT OUTER JOIN A ON B.B_a = A.A_a;

-- 조인 예제
CREATE TABLE shopping_user(
	user_num INT PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(20) NOT NULL,
    user_pw VARCHAR(20) NOT NULL
);
CREATE TABLE user_detail (
	user_num INT,
    user_name VARCHAR(5),
    email VARCHAR(20),
    phone VARCHAR(20),
    address VARCHAR(100),
    FOREIGN KEY(user_num) REFERENCES shopping_user(user_num)
);
INSERT INTO shopping_user (user_id, user_pw) VALUES ('hong123', '1234');
INSERT INTO shopping_user (user_id, user_pw) VALUES ('soo456', '5678');
INSERT INTO shopping_user (user_id, user_pw) VALUES ('hee789', '11111');
INSERT INTO user_detail (user_num, user_name, email) VALUES (1, '홍길동', 'hong123@naver.com');
INSERT INTO user_detail (user_num, user_name, phone) VALUES (2, '김철수', '010-1234-5678');
INSERT INTO user_detail (user_name, address) VALUES ('김영희', '대한민국 어딘가');
SELECT * FROM shopping_user;
SELECT * FROM user_detail;

-- 로그인 기능 제작 시 사용할 만한 쿼리 예제
SELECT * FROM shopping_user WHERE user_id = 'hong123' AND user_pw = '1234';
SELECT * FROM shopping_user WHERE user_id = 'kim456' AND user_pw = '5678';
SELECT * FROM shopping_user WHERE user_id = 'hee789' AND user_pw = '0000';

-- 두 테이블의 모든 데이터의 조합을 구하는 쿼리
SELECT * FROM shopping_user CROSS JOIN user_detail;
SELECT * FROM shopping_user, user_detail;

-- 두 테이블에서 사용자 필수 정보와 상세 정보를 모두 구하는 쿼리
SELECT * FROM shopping_user su INNER JOIN user_detail ud ON su.user_num = ud.user_num;
SELECT * FROM shopping_user su, user_detail ud WHERE su.user_num = ud.user_num;
SELECT su.*, ud.user_name, ud.email, ud.phone, ud.address
FROM shopping_user su, user_detail ud WHERE su.user_num = ud.user_num;

-- 기본 정보 테이블에 저장된 모든 데이터를 출력하고, 추가로 상세 정보도 최대한 출력할 때 쓰는 쿼리
SELECT * FROM shopping_user su LEFT OUTER JOIN user_detail ud ON su.user_num = ud.user_num;
-- 상세 정보 테이블에 저장된 모든 데이터를 출력하고, 추가로 기본 정보도 최대한 출력할 때 쓰는 쿼리.
SELECT * FROM shopping_user su RIGHT OUTER JOIN user_detail ud ON su.user_num = ud.user_num;


-- 상세 정보 테이블에 이메일을 입력한 사용자만 조회하는 쿼리.
SELECT * FROM shopping_user su LEFT OUTER JOIN user_detail ud ON su.user_num = ud.user_num
WHERE email IS NOT NULL;
-- 상세 정보 테이블에 전화번호를 입력한 사용자만 조회하는 쿼리.
SELECT * FROM shopping_user su LEFT OUTER JOIN user_detail ud ON su.user_num = ud.user_num
WHERE phone IS NOT NULL;
-- 상세 정보 테이블에 이메일 또는 전화번호를 입력한 사용자만 조회하는 쿼리.
SELECT * FROM shopping_user su LEFT OUTER JOIN user_detail ud ON su.user_num = ud.user_num
WHERE email IS NOT NULL OR phone IS NOT NULL; 

INSERT INTO shopping_user (user_id, user_pw) VALUES ('gil1111', '2222');
INSERT INTO user_detail VALUES (4, '홍길동', 'gil@gmail.com', '010-1122-3344', '어디게');

-- 상세 정보 테이블에서, 이름이 '홍길동'인 데이터를 모두 조회하는 쿼리
SELECT * FROM shopping_user su LEFT OUTER JOIN user_detail ud ON su.user_num = ud. user_num
WHERE ud.user_name LIKE '홍길동';
-- 상세 정보 테이블에서, 이름이 '김'으로 시작하는 데이터를 모두 조회하는 쿼리
SELECT * FROM shopping_user su RIGHT OUTER JOIN user_detail ud ON su.user_num = ud.user_num
WHERE ud.user_name LIKE '김%';

CREATE TABLE login_info (
	user_num INT,
    last_login DATETIME DEFAULT NOW(),
    FOREIGN KEY(user_num) REFERENCES shopping_user(user_num)
);
INSERT INTO login_info (user_num, last_login) VALUES (1, '2022-09-01');
INSERT INTO login_info (user_num, last_login) VALUES (1, '2022-09-03');
INSERT INTO login_info (user_num, last_login) VALUES (1, '2022-09-05');

-- 기본 정보 테이블과 마지막 로그인 정보 테이블의 데이터를 출력하는 쿼리
SELECT * FROM shopping_user su, login_info li WHERE su.user_num = li.user_num;

-- 기본 정보 테이블의 id와, 상세 정보 테이블의 이름과, 로그인 정보 테이블의 마지막 로그인 날짜를 출력하는 쿼리
SELECT su.user_id, ud.user_name, li.last_login
FROM shopping_user su, user_detail ud, login_info li
WHERE
	su.user_num = ud.user_num
    AND
    su.user_num = li.user_num;
    