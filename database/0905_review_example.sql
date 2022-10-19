-- 9월 5일 예제(9월 1일 수업 내용 관련)

-- 1. 데이터베이스 생성
-- school 데이터베이스를 생성하는 쿼리를 작성하세요.
CREATE DATABASE school;
CREATE SCHEMA school;
CREATE DATABASE IF NOT EXISTS school;
CREATE SCHEMA IF NOT EXISTS school;

-- 2. 데이터베이스 조회
-- 2-1. 모든 데이터베이스를 조회하는 쿼리를 작성하세요.
SHOW DATABASES;
SHOW SCHEMAS;

-- 2-2. 이름에 'oo' 문자가 포함된 데이터베이스를 조회하는 쿼리를 작성하세요.
SHOW DATABASES LIKE '%oo%';
SHOW SCHEMAS LIKE '%oo%';

-- 3. school 데이터베이스를 기본 작업 데이터베이스로 설정하는 쿼리를 작성하세요.
USE school;

-- 4. 테이블 생성
-- 4-1. 다음과 같은 열을 가지는 student 테이블을 생성하는 쿼리를 작성하세요.
--   > 정수 자료형에 기본 키가 적용된 student_id 열
--   > 최대 5글자 문자열에 중복을 허용하지 않는 student_name 열
CREATE TABLE student (
	student_id INT UNSIGNED,
    student_name CHAR(5),
    PRIMARY KEY(student_id),
    UNIQUE(student_name)
);

-- 4-2. 다음과 같은 열을 가지는 exam_score 테이블을 생성하는 쿼리를 작성하세요.
--   > 정수 자료형에 기본 키가 적용된 exam_id 열
--   > 정수 자료형에 student 테이블의 student_id 열을 참조하는 외래 키가 적용된 student_id 열
--   > 총 5자리 및 소수점 2자리의 실수 자료형에 NULL을 허용하지 않는 score 열
CREATE TABLE exam_score (
	exam_id INT UNSIGNED PRIMARY KEY,
    student_id INT UNSIGNED,
    score DECIMAL(5, 2) NOT NULL,
	FOREIGN KEY(student_id) REFERENCES student(student_id)
);


-- 5. 테이블 조회
-- 5-1. school 데이터베이스에 존재하는 모든 테이블을 조회하는 쿼리를 작성하세요.
SHOW TABLES;  -- 현재 기본 작업 데이터베이스로 지정된 데이터베이스 내 모든 테이블 조회
SHOW TABLES FROM school;  -- 특정 데이터베이스 내 모든 테이블 조회

-- 5-2. school 데이터베이스에 존재하는 테이블 중 이름에 's' 문자가 포함된 테이블을 조회하는 쿼리를 작성하세요.
SHOW TABLES LIKE '%s%';
SHOW TABLES FROM school LIKE '%s%';

-- 6. 열 조회
-- 6-1. student 테이블에 존재하는 모든 열을 조회하는 쿼리를 작성하세요.
SHOW COLUMNS FROM student;

-- 6-2. exam_score 테이블에 존재하는 열 중 이름에 'e' 문자가 포함된 열을 조회하는 쿼리를 작성하세요.
SHOW COLUMNS FROM exam_score LIKE '%e%';

-- 참고: exam_score 테이블에서 null을 허용하지 않는 모든 열 조회 쿼리
SHOW COLUMNS FROM exam_score WHERE `Null` LIKE 'NO';


-- 테이블 생성 후 다음의 쿼리들을 차례대로 실행하여 데이터를 입력하세요.
INSERT INTO student VALUES (1, '홍길동');
INSERT INTO student VALUES (2, '김철수');
INSERT INTO exam_score VALUES (1, 1, 100.00);
INSERT INTO exam_score VALUES (2, 2, 12.34);

-- 입력된 데이터 조회 쿼리.
SELECT * FROM student;
SELECT * FROM exam_score;

-- 7. UNIQUE 제약조건
-- 7-1. student 테이블에 학생 ID가 3이고 학생 이름이 '홍길동'인 데이터를 입력하는 쿼리를 작성하세요.
INSERT INTO student (student_id, student_name) VALUES (3, '홍길동');
INSERT INTO student VALUES (3, '홍길동');
-- 7-2. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# student_name 열에 대해 UNIQUE 제약조건 위반

-- 8. NOT NULL 제약조건
-- 8-1. exam_score 테이블에 시험 ID가 3이고 학생 ID가 2인 데이터를 입력하는 쿼리를 작성하세요.
INSERT INTO exam_score (exam_id, student_id) VALUES (3, 2);
-- 8-2. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# score 열에 대해 NOT NULL 제약조건 위반

-- 9. PK-FK 제약조건
-- 9-1-1. exam_score 테이블에서 홍길동의 점수를 0점으로 수정하는 쿼리를 작성하세요.
UPDATE exam_score SET score = 0 WHERE student_id = 1;
-- 9-1-2. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# 실행 잘 됨.
-- 9-1-3. student 테이블에서 김철수의 ID를 20으로 수정하는 쿼리를 작성하세요.
UPDATE student SET student_id = 20 WHERE student_name LIKE '김철수';
UPDATE student SET student_id = 20 WHERE student_id = 2;
-- 9-1-4. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# exam_score 테이블의 student_id 열이, student 테이블의 student_id 열을 참조하고 있기 때문에,
# PK-FK 관계에 의해, 참조 데이터가 있는 상황에서 원본 데이터는 수정할 수 없음.
-- 9-2-1. exam_score 테이블에서 김철수의 레코드를 삭제하는 쿼리를 작성하세요.
DELETE FROM exam_score WHERE student_id = 2;
-- 9-2-2. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# 실행 잘 됨.
-- 9-2-3. student 테이블에서 홍길동의 레코드를 삭제하는 쿼리를 작성하세요.
DELETE FROM student WHERE student_name LIKE '홍길동';
DELETE FROM student WHERE student_id = 1;
-- 9-2-4. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# exam_score 테이블의 student_id 열이, student 테이블의 student_id 열을 참조하고 있기 때문에,
# PK-FK 관계에 의해, 참조 데이터가 있는 상황에서 원본 데이터는 수정할 수 없음.
-- 9-3-1. student 테이블을 제거하는 쿼리를 작성하세요.
DROP TABLE student;
DROP TABLE IF EXISTS student;
-- 9-3-2. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# student 테이블을 참조하는 exam_score 테이블이 존재하기 때문에,
# 원본 테이블인 student 테이블을 제거할 수 없음.
-- 9-3-3. exam_score 테이블을 제거하는 쿼리를 작성하세요.
DROP TABLE exam_score;
DROP TABLE IF EXISTS exam_score;
-- 9-3-4. 위 쿼리를 실행해보고, 만약 실행되지 않는다면 그 이유는 무엇인지 서술하세요.
# 실행 잘 됨.

-- 다음의 쿼리를 실행해서 테이블을 생성하세요.
CREATE TABLE student_infp (
	info_id INT,
	student_is INT
);

-- 10. 테이블 이름 변경
-- student_infp 테이블의 이름을 student_info로 변경하는 쿼리를 작성하세요.
ALTER TABLE student_infp RENAME student_info;

-- 11. 열 이름 변경
-- student_is 열의 이름을 student_id로 변경하는 쿼리를 작성하세요.
ALTER TABLE student_info CHANGE COLUMN student_is student_id INT;

-- 12. 새 열 추가
-- 12-1. 정수 자료형인 address 열을 추가하는 쿼리를 작성하세요.
ALTER TABLE student_info ADD COLUMN address INT;
-- 12-2. 최대 11자리 문자열에 NULL을 허용하지 않는 phone 열을 추가하는 쿼리를 작성하세요.
ALTER TABLE student_info ADD COLUMN phone CHAR(11) NOT NULL;

-- 13. 열 자료형 변경
-- address 열의 자료형을 최대 100글자 문자열로 변경하는 쿼리를 작성하세요.
ALTER TABLE student_info MODIFY COLUMN address VARCHAR(100);

-- 14. 열 제거
-- phone 열을 제거하는 쿼리를 작성하세요.
ALTER TABLE student_info DROP COLUMN phone;


-- 15. 제약조건 적용
-- 15-1. info_id 열에 기본 키를 적용하는 쿼리를 작성하세요.
	# PK 제약조건 적용 전, 다음과 같이 PK 제약조건을 위반하는 데이터가 앞서 저장되어 있으면 PK 적용 불가.
	INSERT INTO student_info (info_id, student_id) VALUES (1, 1);
	INSERT INTO student_info (info_id, student_id) VALUES (1, 1);
	INSERT INTO student_info (student_id, address) VALUES (1, '대한민국');
    
	ALTER TABLE student_info ADD CONSTRAINT info_id_pk PRIMARY KEY(info_id);  # 기본 문법
	ALTER TABLE student_info ADD CONSTRAINT PRIMARY KEY(info_id);  # 제약조건 이름 생략
	ALTER TABLE student_info ADD PRIMARY KEY(info_id);  # 키워드 생략
-- 15-2. student_id 열에 student 테이블의 student_id 열을 참조하는 외래 키를 적용하는 쿼리를 작성하세요.
	# FK 추가 전 실행할 것.
    ALTER TABLE student_info MODIFY COLUMN student_id INT UNSIGNED;
	
    # 기본 문법
	ALTER TABLE student_info ADD CONSTRAINT student_id_fk
	FOREIGN KEY(student_id) REFERENCES student(student_id);
	# 제약조건 이름 생략
	ALTER TABLE student_info ADD CONSTRAINT
	FOREIGN KEY(student_id) REFERENCES student(student_id);
	# 키워드 생략
	ALTER TABLE student_info ADD FOREIGN KEY(student_id) REFERENCES student(student_id);

-- 15-3. student_id 열에 중복을 허용하지 않는 제약조건을 적용하는 쿼리를 작성하세요.
	# UNIQUE 제약조건 적용 전, 테이블에 중복된 값이 존재하는 경우 제약조건이 적용될 수 없음.
	INSERT INTO student_info VALUES (1, 1, '길동네');
    INSERT INTO student_info VALUES (2, 1, '홍길동 집');

	# 기본 문법
	ALTER TABLE student_info ADD CONSTRAINT student_id_uq UNIQUE(student_id);
    # 제약조건 이름 생략
    ALTER TABLE student_info ADD CONSTRAINT UNIQUE(student_id);
    # 키워드 생략
	ALTER TABLE student_info ADD UNIQUE(student_id);

-- 15-4. address 열에 NULL을 허용하지 않는 제약조건을 적용하는 쿼리를 작성하세요.
	ALTER TABLE student_info MODIFY COLUMN address VARCHAR(100) NOT NULL;
-- 15-5. address 열에 기본 값으로 '대한민국 어딘가'를 설정하는 쿼리를 작성하세요.
	ALTER TABLE student_info MODIFY COLUMN address VARCHAR(100) DEFAULT '대한민국 어딘가';
    # => MODIFY COLUMN을 통해 수정한 경우, 기존에 설정된 자료형, 제약조건을 덮어씌움
-- 15-6. address 열에 NULL을 허용하지 않고 기본 값으로 '대한민국 어딘가'를 설정하는 쿼리를 작성하세요.
	ALTER TABLE student_info
    MODIFY COLUMN address VARCHAR(100)
    NOT NULL DEFAULT '대한민국 어딘가';

	# address 열을 지정하지 않고 데이터 입력 시 자동으로 기본 값이 입력됨(DEFAULT 제약조건에 의해).
	INSERT INTO student_info (info_id, student_id) VALUES (1, 1);
    # address 열을 지정하고 데이터 입력 시 해당 값이 입력됨.
	INSERT INTO student_info (info_id, student_id, address) VALUES (2, 2, '철수네 집');

-- 이하의 쿼리는 수업 시간에 다시 다룹니다.

-- 모든 제약조건 조회 쿼리.
	SELECT * FROM information_schema.table_constraints;
-- student_info 테이블 내 모든 제약조건 조회 쿼리
	SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME LIKE 'student_info';

-- 기본 키 제약조건 해제 쿼리.
	ALTER TABLE student_info DROP CONSTRAINT `PRIMARY`;
	# MYSQL에서는, PK 제약조건 지정 시 제약조건 이름을 설정해도 무시하고 `PRIMARY` 로 지정함.
	ALTER TABLE student_info ADD CONSTRAINT info_id_pk PRIMARY KEY(info_id);
-- 외래 키 제약조건 해제 쿼리.
	ALTER TABLE student_info DROP CONSTRAINT student_id_fk;
    ALTER TABLE student_info ADD CONSTRAINT student_id_fk
    FOREIGN KEY(student_id) REFERENCES student(student_id);
    # MYSQL에서는, FK 제약조건 지정 시 제약조건 이름을 설정하지 않으면 `테이블명_ibfk_1` 로 지정함.
    ALTER TABLE student_info ADD
    FOREIGN KEY(student_id) REFERENCES student(student_id);
    # 기본 설정된 제약조건명으로 제약조건 제거
    ALTER TABLE student_info DROP CONSTRAINT student_info_ibfk_1;

-- 중복을 허용하지 않음 제약조건 해제 쿼리.
	# UNIQUE 제약조건의 경우, 제약조건 이름을 설정하지 않으면 `열 이름`으로 자동으로 설정함.
	ALTER TABLE student_info DROP CONSTRAINT student_id;
    # 지정한 제약조건 이름이 있으면 해당 이름으로 제거할 수 있음.
    ALTER TABLE student_info ADD CONSTRAINT student_id_uq UNIQUE(student_id);
    ALTER TABLE student_info DROP CONSTRAINT student_id_uq;
-- NULL을 허용하지 않음, 기본 값 제약조건 해제 쿼리
	# NOT NULL, DEFAULT 제약조건의 경우, 이름을 부여할 수 없기 때문에 열 변경 쿼리로 덮어씌움.
	ALTER TABLE student_info MODIFY COLUMN address VARCHAR(100);
