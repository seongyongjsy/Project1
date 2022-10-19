/*
DDL: CREATE, ALTER, DROP
DML: SELECT, INSERT, UPDATE, DELETE
DCL: GRANT, REVOKE, COMMIT, ROLLBACK

데이터 제어어(Data Control Language, DCL): 사용자 권한 제어 또는 트랜잭션 제어 등에 사용하는 쿼리.
ㄴ트랜잭션 제어어(Transaction Control Language, TCL): COMMIT, ROLLBACK
ㄴ트랜잭션: 작업의 단위. commit과 rollback의 대상.
여러 쿼리를 실행해서 데이터베이스의 테이블의 데이터에 영향을 줬을 때, 일련의 쿼리들을 묶어서 나타내는 단위.
일련의 쿼리 작업들을 확정하거나 되돌리거나 할 때 사용하는 개념.
*/

# autocommit: INSERT, UPDATE, DELETE 등 트랜잭션을 발생시키는 쿼리 작업 시, 자동으로 확정하는 기능.
# 이 기능이 활성화되어 있으면, INSERT, UPDATE, DELETE 등 쿼리 실행 시 즉시 테이블에 데이터 조작을 확정함.
SET @@autocommit = 1;  # autocommit 기능 활성화
SET @@autocommit = 0;  # autocommit 기능 비활성화
SELECT @@autocommit;  # 설정된 autocommit 값 확인

USE test_db;
CREATE TABLE example_tb (
	a INT
);
SELECT * FROM example_tb;

INSERT INTO example_tb VALUES (10);  # 데이터 입력 => 트랜잭션 발생 => 이후의 작업 내역을 기록함.
SELECT * FROM example_tb;  # 10 입력 확인 => 임시 상태이므로 취소 가능.
ROLLBACK;  # 트랜잭션 취소 => 트랜잭션 종료 => 일련의 작업들을 없던 것으로 되돌림.
SELECT * FROM example_tb;  # 10 없어진 것 확인.

INSERT INTO example_tb VALUES (20);  # 데이터 입력 => 트랜잭션 발생 => 이후의 작업 내역을 기록함.
SELECT * FROM example_tb;  # 20 입력 확인.
COMMIT;  # 트랜잭션 확정 => 트랜잭션 종료 => 일련의 작업들을 확정해서 테이블에 기록함.
SELECT * FROM example_tb;  # 20 입력 확인 => 확정된 상태이므로 다음 트랜잭션에서도 확인 가능.

INSERT INTO example_tb VALUES (30);  # 데이터 입력 => 트랜잭션 발생 => 이후의 작업 내역을 기록함.
INSERT INTO example_tb VALUES (100);  # 앞서 발생한 트랜잭션에 기록되는 작업.
UPDATE example_tb SET a = a + 1;  # 앞서 발생한 트랜잭션에 기록되는 작업.
DELETE FROM example_tb WHERE a = 21;  # 앞서 발생한 트랜잭션에 기록되는 작업.
SELECT * FROM example_tb;  # 31, 101 입력 확인.
ROLLBACK;  # 트랜잭션 취소 => 트랜잭션 종료 => 일련의 작업들을 없던 것으로 되돌림.
SELECT * FROM example_tb;  # 20 입력 확인.

# COMMIT;  # 트랜잭션을 확정하는 명령어.
# ROLLBACK;  # 트랜잭션을 취소하는 명령어.

# START TRANSACTION;  # 트랜잭션을 강제로 시작하는 명령어.

# SAVEPOINT: 한 트랜잭션을 쪼개서 작업을 소단위로 표현할 때 사용. 마찬가지로 되돌리거나 확정할 수 있음.
SELECT * FROM example_tb;

INSERT INTO example_tb VALUES (30);  # 트랜잭션 시작.
SELECT * FROM example_tb;  # 20, 30

SAVEPOINT A;  # 세이브포인트 생성
UPDATE example_tb SET a = a * 10;
DELETE FROM example_tb WHERE a = 200;
SELECT * FROM example_tb;  # 300

ROLLBACK TO SAVEPOINT A;  # 세이브포인트 A 생성 시점으로 되돌림
SELECT * FROM example_tb;  # 20, 30

COMMIT;  # 트랜잭션 확정, 종료
SELECT * FROM example_tb;  # 20, 30


INSERT INTO example_tb VALUES (10);  # 트랜잭션 시작.
SELECT * FROM example_tb;  # 20, 30, 10

SAVEPOINT B;  # 세이브포인트 B 생성.
UPDATE example_tb SET a = a + 1;
SELECT * FROM example_tb;  # 21, 31, 11
SAVEPOINT C;  # 세이브포인트 C 생성.
DELETE FROM example_tb WHERE a = 21;
SELECT * FROM example_tb;  # 31, 11

ROLLBACK TO SAVEPOINT C;  # 세이브포인트 C 생성 시점으로 되돌림.
SELECT * FROM example_tb;  # 21, 31, 11
ROLLBACK TO SAVEPOINT B;  # 세이브포인트 B 생성 시점으로 되돌림.
SELECT * FROM example_tb;  # 20, 30, 10

ROLLBACK;  # 트랜잭션 취소, 종료
SELECT * FROM example_tb;  # 20, 30


-- 사용자 계정 관리
SHOW DATABASES;
USE mysql;
SHOW TABLES;
SELECT * FROM user;  # mysql에서 사용할 수 있는 사용자에 대한 데이터를 저장하는 테이블.

CREATE USER 'hong'@'localhost' IDENTIFIED BY '1111';  # 사용자 계정 생성 명령어. 계정명@호스트명, 비밀번호 입력.
DROP USER 'hong'@'localhost';  # 사용자 계정 제거 명령어.

CREATE DATABASE hong;
-- GRANT: 권한 부여 명령어.
GRANT ALL PRIVILEGES ON hong.* TO 'hong'@'localhost';
# GRANT ALL PRIVILEGES ON hong.* TO 'hong'@'localhost' IDENTIFIED BY '1111';

-- REVOKE: 권한 철회 명령어.
REVOKE ALL PRIVILEGES ON hong.* FROM 'hong'@'localhost';

FLUSH PRIVILEGES;  # 권한 부여/철회 후 한 번 실행해줄 것.

SHOW GRANTS FOR 'hong'@'localhost';  # 특정 계정의 권한 확인 명령어.

ALTER USER 'hong'@'localhost' IDENTIFIED BY '2222';  # 비밀번호 변경 명령어.
