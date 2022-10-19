-- 그룹화
-- 특정 테이블의 모든 레코드 수 구하기
SELECT COUNT(*) FROM rental;
-- 특정 열의 레코드 수 구하기(null 제외)
SELECT COUNT(rental_date), COUNT(return_date) FROM rental;
-- 특정 열의 최소, 최대, 총합, 평균 데이터 구하기
SELECT MIN(amount), MAX(amount), SUM(amount), AVG(amount) FROM payment;
-- 특정 열을 지정해서 그룹으로 묶고, 각 그룹 별 총합 데이터 구하기
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id;
SELECT customer_id, staff_id, SUM(amount) FROM payment GROUP BY customer_id, staff_id;
-- 일반 조건은 WHERE절에, 그룹 조건은 HAVING절에 작성
SELECT customer_id, SUM(amount) FROM payment WHERE customer_id < 10 GROUP BY customer_id;
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id HAVING SUM(amount) > 100.0;

-- DDL: 데이터 정의어, 데이터베이스 또는 테이블 등을 정의할 때 사용하는 쿼리. CREATE, ALTER, DROP 등
CREATE DATABASE test_db; -- 데이터베이스 생성 쿼리.
CREATE DATABASE IF NOT EXISTS test_db; -- 데이터베이스 생성 시 추가 제한 옵션 가능
SHOW DATABASES; -- 현재 계정에서 접속할 수 있는 모든 데이터베이스를 조회하는 쿼리.
SHOW DATABASES LIKE '%a%'; -- 데이터베이스 조회 시 추가 옵션 가능.
USE test_db; -- 작업을 위한 기본 데이터베이스 설정 쿼리. Set ad Default Schema 기능과 동일

CREATE TABLE test_tb (
	a INT,
    b DECIMAL(3, 1),
    c CHAR(10),
    d DATETIME
); -- 테이블 생성 쿼리
CREATE TABLE IF NOT EXISTS test_tb (
	a INT,
    b DECIMAL(3, 1),
    c CHAR(10),
    d DATETIME
); -- 테이블 생성 시 추가 제한 옵션 가능.
SHOW TABLES; -- 현재 지정한 데이터베이스 내 모든 테이블을 조회하는 쿼리.
SHOW TABLES LIKE '%t%'; -- 테이블 조회 시 추가 검색 옵션 가능.
SHOW TABLES FROM sakila; -- 테이블 조회 시 데이터베이스 지정 가능.
SHOW COLUMNS FROM sakila.rental; -- 지정한 테이블에 대한 열 정보를 조회하는 쿼리.

DROP TABLE test_tb; -- 테이블 삭제 쿼리
DROP TABLE IF EXISTS test_db; -- 테이블 삭제 시 추가 제한 옵션 가능.

DROP DATABASE test_db; -- 데이터베이스 삭제 쿼리.
DROP DATABASE IF EXISTS test_db; -- 데이터베이스 삭제 시 추가 제한 옵션 가능.

-- DML: 데이터 조작어. 데이터를 직접 조작하는 쿼리. SELECT, INSERT, UPDATE, DELETE 등.
INSERT INTO test_tb (a, b, c, d) VALUES (111, 2.1, 'HELLO', NOW());
INSERT INTO test_tb (b, d, a, c) VALUES (12.3, NOW(), 123, 'hi');
INSERT INTO test_tb (a, c) VALUES (9999, 'BYE');
INSERT INTO test_tb VALUES (-1, 0.1, 'how are you', NOW());

UPDATE test_tb SET a = 0;
UPDATE test_tb SET a = 1 WHERE b = 2.1;
UPDATE test_tb SET a = 3, c = LOWER(c) WHERE b IS NULL;

DELETE FROM test_tb;
DELETE FROM test_tb WHERE a = 0;

SELECT * FROM test_tb;

-- 제약조건(Constraint): 테이블의 데이터에 대해서 제한을 적용하는 문법.
-- 테이블 생성 시 특정 열을 지정해서 설정함.
-- NOT NULL: null을 허용하지 않음.
-- UNIQUE: 중복 값을 허용하지 않음.
-- PRIMARY KEY(PK) : 기본 키
-- FOREIGN KEY(FK) : 외래 키
-- DEFAULT: 기본 값 설정.

CREATE TABLE test_const (
	a CHAR(100) NOT NULL,
    b INT UNIQUE,
    c INT UNIQUE NOT NULL 
);
INSERT INTO test_const (a, b, c) VALUES ('hello', 1, 1);
INSERT INTO test_const (b, c) VALUES (2, 2); -- a열의 NOT NULL 제약조건 위반.
INSERT INTO test_const (a, b) VALUES ('hello', 2);-- c열의 NOT NULL 제약조건 위반.
INSERT INTO test_const (a, c) VALUES ('hello', 2);
INSERT INTO test_const (a, c) VALUES ('hello', 3);
INSERT INTO test_const (a, b, c) VALUES ('hello', 1, 4); -- b열의 UNIQUE 제약조건 위반.
INSERT INTO test_const (a, b, c) VALUES ('hello', 2, 4); 
INSERT INTO test_const (a, b, c) VALUES ('hello', 3, 4); -- c열의 UNIQUE 제약조건 위반.
SELECT * FROM test_const;

CREATE TABLE test_default(
	a INT DEFAULT 1,
    b INT NOT NULL DEFAULT 2,
    c INT UNIQUE DEFAULT 3
);
INSERT INTO	test_default (a, b, c) VALUES (1, 2, 3);
INSERT INTO	test_default (b, c) VALUES (3, 4);  -- a열에 default value 자동 입력.
INSERT INTO test_default (a, c) VALUES (1, 5);  -- b열에 default value 자동 입력.
INSERT INTO test_default (a, b) VALUES (1, 2);  -- c열에 기본 값 입력 시도했으나 제약조건 위반으로 실패.
SELECT * FROM test_default;

-- PRIMARY KEY: 기본 키. NOT NULL + UNIQUE 제약조건을 합친 제약조건.
-- PK가 적용된 열은, 해당 테이블을 대표하는 열을 나타냄.
-- 다른 테이블에서 FK로 사용됨
-- PK 제약조건은 한 테이블에서 오직 한 열만 설정할 수 있음.
-- NOT NULL, UNIQUE 제약조건을 위반하지 않는 한 데이터 입력에 제한 없음.

-- FOREIGN KEY(FK): 외래 키.
-- 다른 테이블의 PK 열의 데이터를 기록하기 위함.
-- 다른 테이블의 PK와 같이 사용됨.
-- FK 제약조건은 한 테이블에서 여러 열에 설정할 수 있음.
-- 원본 PK 열에 없는 데이터는 FK 열에 입력할 수 없음.
CREATE TABLE parent (
	parent_id INT,	-- 부모 테이블을 대표하는 고유의 ID 값을 저장할 열
    parent_name CHAR(10), -- 부모의 이름을 저장할 열
    PRIMARY KEY(parent_id) -- parent_id 열을 PK로 지정
);

CREATE TABLE child(
	child_id INT,	-- 자식 테이블을 대표하는 고유의 ID 값을 저장할 열
    parent_id INT,	-- 레코드 입력 시, 부모 데이터가 무엇인지 기록할 열
    child_name CHAR(10), -- 자식의 이름을 저장할 열
	PRIMARY KEY(child_id), -- child_id 열을 PK로 지정
    FOREIGN KEY(parent_id) REFERENCES parent(parent_id) -- parent_id 열을 FK로 지정
);

INSERT INTO parent (parent_id, parent_name) VALUES (1, '홍길동 엄마');
INSERT INTO child (child_id, parent_id, child_name) VALUES (1, 1, '홍길동');
INSERT INTO parent (parent_id, parent_name) VALUES (1, 1, '김철수 아빠');	-- PK UQ 위반
INSERT INTO child (child_id, parent_id, child_name) VALUES (1, 1, '김철수'); -- PK 중복 위반
INSERT INTO parent (parent_id) VALUES ('김철수 아빠'); -- PK-NN 위반
INSERT INTO child (parent_id, child_name) VALUES (1, '김철수'); -- PK-NN 위반

INSERT INTO child (child_id, parent_id, child_name) VALUES (2, 2, '김철수'); -- FK 위반 
INSERT INTO parent (parent_id, parent_name) VALUES (2, '김철수 아빠'); 
INSERT INTO child (child_id, parent_id, child_name) VALUES (2, 2,)


SELECT * FROM parent;
SELECT * FROM child;

-- ALTER: DDL의 일종으로써, 이미 만들어진 데이터베이스 또는 테이블 등을 수정하는 쿼리.
테이블 이름 변경 : 				ALTER TABLE 테이블명 RENAME 새테이블이름
새 열 추가:					ALTER TABLE 테이블명 ADD COLUMN 새열이름 [제약조건]
새 제약조건 추가:				ALTER TABLE 테이블명 ADD CONSTRAINT [제약조건명] 종류(열이름)
열 이름 변경: 					ALTER TABLE 테이블명 CHANGE 기존열이름 새열이름 자료형
열 자료형 변경 또는 새 제약조건 추가: ALTER TABLE 테이블명 MODIFY 열이름 자료형 [제약조건]
열 제거 : 					ALTER TABLE 테이블명 DROP COLUMN 열이름
제약조건 제거: 					ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건이름;
외래키 제약조건 제거:				ALTER TABLE 테이블명 DROP FOREIGN KEY 제약조건명
