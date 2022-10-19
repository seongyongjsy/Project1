-- 기타 함수
-- IF(표현식, 참일 때의 값, 거짓일 때의 값): 표현식을 판별해서 값을 선택하는 함수.
SELECT
	IF(10 > 0, '참입니다!', '거짓입니다...'),
    IF(10 > 100, '참입니다!', '거짓입니다...'),
    IF(TRUE, '참입니다!', '거짓입니다...'),
    IF(1, '참입니다!', '거짓입니다...'),
    IF(FALSE, '참입니다!', '거짓입니다...'),
    IF(0, '참입니다!', '거짓입니다...'),
    IF('1', '참입니다!', '거짓입니다...'),
    IF('0', '참입니다!', '거짓입니다...'),
    IF('TRUE', '참입니다!', '거짓입니다...'),
    IF('FALSE', '참입니다!', '거짓입니다...'),
    IF('hello', '참입니다!', '거짓입니다...')
;

SELECT
	return_date,
	IF(
		return_date > '2005-06-01 00:00:00',
		'아직 반납 기한이 남았습니다.',
        '반납 기한이 지났습니다!'
	) AS 'is_expired'
FROM rental
WHERE return_date is not null
ORDER BY return_date;

SELECT
	rental_date, return_date,
    IF(rental_date < '2005-06-01 00:00:00',
		IF(return_date < '2005-06-01 00:00:00',
			'이미 반납일이 지난 건입니다.',
            '대여는 시작되었지만 아직 반납 기한이 남았습니다.'
        ),
        '아직 대여 예정일이 도래하지 않았습니다.'
    ) AS 'judge'
FROM rental
WHERE return_date IS NOT NULL
ORDER BY rental_date;

-- IFNULL(검사대상, null일 경우 선택할 값): null 여부 검사 함수.
SELECT IF(return_date IS NULL, '-', return_date) FROM rental;
SELECT IFNULL(return_date, '-') FROM rental;

-- NULLIF(표현식1, 표현식2): 표현식1=표현식2면 null을 반환. 아니면 표현식1 반환.
SELECT NULLIF(10, 20), NULLIF(30, 30);

-- ISNULL(값): null 여부 검사 함수.
SELECT return_date, ISNULL(return_date) FROM rental;


-- CAST(값 AS 자료형), CONVERT(값, 자료형): 자료형 변환 함수.
-- 자료형 => SIGNED, UNSIGNED, DECIMAL, CHAR, DATE, TIME, DATETIME
SELECT CAST(1234 AS CHAR), CONVERT(1234, CHAR);  -- 정수=>문자열 변환
SELECT CAST(1234 AS DECIMAL(5, 1)), CONVERT(1234, DECIMAL(5, 1));  -- 정수=>실수 변환
SELECT CAST(12.34 AS SIGNED), CONVERT(12.34, SIGNED);  -- 실수=>정수 변환

-- overflow/underflow: 값 표현 범위를 벗어나서 가장 작은/큰 값부터 다시 표현하는 것.
SELECT CAST(-12.34 AS SIGNED), CAST(-12.34 AS UNSIGNED);
SELECT
	CAST(2 AS UNSIGNED), CAST(1 AS UNSIGNED), CAST(0 AS UNSIGNED),
    CAST(-1 AS UNSIGNED), CAST(-2 AS UNSIGNED), CAST(-3 AS UNSIGNED);
SELECT CONVERT('안녕하세요?' USING utf8);  -- 문자열 인코딩 방식 변환 시 사용


-- 집계 함수(Aggregate function): 통계와 관련된 계산을 하는 함수들.
-- COUNT(* 또는 열 이름): 레코드 수 구하는 함수.
SELECT COUNT(*) FROM country;  -- 전체 테이블의 레코드 수 구하기
SELECT COUNT(country) FROM country; -- country 열의 레코드 수 구하기
SELECT COUNT(*), COUNT(return_date) FROM rental;  -- null 레코드는 집계 제외
SELECT COUNT(DISTINCT customer_id) FROM rental;  -- 중복 레코드 제외

-- MIN, MAX(열): 해당 열의 레코드 중 가장 작은/큰 값을 구하는 함수
SELECT MIN(rental_duration), MAX(rental_duration) FROM film;
SELECT MIN(rental_date), MAX(rental_date) FROM rental;

-- SUM(열): 해당 열의 레코드의 합계를 구하는 함수.
SELECT SUM(rental_rate) FROM film;

-- AVG(열): 해당 열의 레코드의 평균을 구하는 함수.
SELECT AVG(rental_rate) FROM film;

-- GROUP_CONCAT(열): 해당 열의 레코드를 하나로 묶어서 출력하는 함수.
SELECT GROUP_CONCAT(inventory_id) FROM rental
WHERE customer_id = 1;
SELECT GROUP_CONCAT(inventory_id SEPARATOR '|' ) FROM rental
WHERE customer_id = 1;  -- 기본 분리자는 ','이지만 다른 분리자 문자열 설정 가능
SELECT GROUP_CONCAT(inventory_id ORDER BY inventory_id) FROM rental
WHERE customer_id = 1;  -- 정렬 후 레코드 데이터 묶기 가능
SELECT GROUP_CONCAT(inventory_id ORDER BY inventory_id SEPARATOR '|' ) FROM rental
WHERE customer_id = 1;  -- 혼합 사용 가능
SELECT GROUP_CONCAT(DISTINCT store_id) FROM inventory
WHERE film_id = 4;  -- 중복 제거 후 하나로 묶음


-- 그룹화: 특정 열을 기준으로 그룹을 묶는 것. 그룹 별로 추가 동작을 할 수 있음 ex) 그룹 별 평균, 그룹 별 합계, ...
-- 집계 함수는 그룹화와 함께 자주 사용되어 그룹 함수로도 불림

-- 고객 별로 대여한 횟수 구하는 쿼리
SELECT customer_id, COUNT(inventory_id) FROM rental GROUP BY customer_id;

-- 고객 별로 얼마나 지불했는지, 총 지불 금액을 구하는 쿼리.
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id;

-- 고객 별로 가장 작은/큰 대여일, 즉 첫 대여일과 마지막 대여일을 구하는 쿼리.
SELECT customer_id, MIN(rental_date), MAX(rental_date) FROM rental GROUP BY customer_id;

-- 가계 별 상품 총 재고량 구하는 쿼리.
SELECT COUNT(*) FROM inventory WHERE store_id = 1;  # 2270
SELECT COUNT(*) FROM inventory WHERE store_id = 2;  # 2311
SELECT store_id, COUNT(*) FROM inventory GROUP BY store_id;

-- 배우 별 출연한 영화 수
SELECT actor_id, count(film_id) FROM film_actor GROUP BY actor_id;

-- 영화 별 출연한 배우 수
SELECT film_id, count(actor_id) FROM film_actor GROUP BY film_id;

-- 여러 개의 열을 기준으로 그룹화 지정 가능.
-- 고객 별로, 각 지점에서 얼마만큼 지불했는지 구하는 쿼리.
SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY customer_id, staff_id;

-- 가게 별로, 활성화 및 비활성화된 고객 수 구하는 쿼리.
SELECT store_id, active, COUNT(*) FROM customer GROUP BY store_id, active
ORDER BY store_id, active DESC;

-- HAVING 키워드로 그룹 함수에 대한 조건을 작성할 수 있음.
-- 각 지점별로 50불 이상 지불한 고객들을 대상으로 각각 얼마만큼 지불했는지 구하는 쿼리.
SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY customer_id, staff_id HAVING SUM(amount) > 50.00;

-- HAVING에 여러 조건 작성 가능
-- 1~10번 고객 중, 각 지점에서 50불 이상 지불한 고객들을 대상으로 각각 얼마만큼 지불했는지 구하는 쿼리.
SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY customer_id, staff_id
HAVING SUM(amount) > 50.00 AND (customer_id BETWEEN 1 AND 10);

-- WHERE절과 그룹화 같이 사용 가능 - 일반 조건은 WHERE절에 작성 권장
-- 1~10번 고객 중, 각 지점에서 50불 이상 지불한 고객들을 대상으로 각각 얼마만큼 지불했는지 구하는 쿼리.
SELECT customer_id, staff_id, SUM(amount) FROM payment
WHERE customer_id BETWEEN 1 AND 10
GROUP BY customer_id, staff_id
HAVING SUM(amount) > 50.00;

/*
SELECT [DISTINCT] 열1 [, 열2 [, ...]]
[FROM 테이블]
[WHERE 일반조건]
[GROUP BY 열1 [, 열2 [, ...]] [HAVING 그룹조건] ]
[ORDER BY 열1 [, 열2 [, ...]]]
[LIMIT n]
*/

-- CASE문: SELECT절에서 사용,
-- CASE에 특정한 열의 값들을 확인해서, WHEN에 제시된 값과 일치하는지 판별하며, THEN의 값을 선택하는 문법
-- 일치하는 경우가 없으면 NULL 또는 ELSE의 값 선택.
SELECT
	customer_id,
	CASE customer_id
		WHEN 1 THEN '1번 고객님'
        WHEN 2 THEN '2번 고객님'
        WHEN 3 THEN '3번 고객님'
		ELSE '누구세요?'
	END AS 'customer name'
FROM customer
WHERE customer_id < 10;

SELECT
	rental_date, return_date,
    CASE
		WHEN rental_date < '2005-06-01' AND return_date < '2005-06-01' THEN '반납 완료 건'
        WHEN rental_date < '2005-06-01' AND return_date > '2005-06-01' THEN '대여 중인 건'
        WHEN rental_date > '2005-06-01' AND return_date > '2005-06-01' THEN '대여 예정 건'
	END AS 'judge'
FROM
	rental
ORDER BY rental_date;

/*
쿼리 분류
1. 데이터 정의어(Data Definition Language, DDL)
  - 데이터베이스 및 테이블을 정의하는 쿼리
    - CREATE: 데이터베이스 또는 테이블을 생성하는 쿼리
    - ALTER: 생성된 데이터베이스 또는 테이블에 대해 수정할 때 사용하는 쿼리
    - DROP: 데이테베이스 또는 테이블을 제거하는 쿼리

2. 데이터 조작어(Data Manipulate Language, DML)
  - 데이터 입력, 수정, 삭제, 조회 등 데이터를 직접적으로 다루는 쿼리
    - SELECT: 테이블에서 레코드 및 필드를 선택해서 조회할 때 사용하는 쿼리
    - INSERT: 새로운 레코드를 입력할 때 사용하는 쿼리
    - UPDATE: 레코드를 수정하는 쿼리
    - DELETE: 레코드를 삭제하는 쿼리

3. 데이터 통제어(Data Control Language, DCL)
  - 사용 권한, 트랜잭션 관리 등 데이터베이스에 관련된 동작을 통제하기 위한 쿼리
  - GRANT, REVOKE, COMMIT, ROLLBACK
*/

-- 데이터베이스 생성 쿼리
CREATE DATABASE student;
CREATE SCHEMA student;
-- 테이블 생성 쿼리
CREATE TABLE teacher (
	teacher_id INT,
    teacher_name VARCHAR(10),
    score DECIMAL(3, 2),
    reg_date DATETIME
);
-- 데이터 입력 쿼리
INSERT INTO teacher (teacher_id, teacher_name, score, reg_date)
VALUES (1, '홍길동', 0.00, NOW());
INSERT INTO teacher (reg_date, teacher_id, teacher_name)
VALUES (NOW(), 2, '김철수');

SELECT * FROM teacher;

-- 테이블 삭제 쿼리
DROP TABLE teacher;

-- 데이터베이스 삭제 쿼리
DROP DATABASE student;

-- 데이터 수정 쿼리
UPDATE teacher
SET score=5.00;
UPDATE teacher
SET score=2.50
WHERE teacher_name='김철수';
UPDATE teacher
SET teacher_name='황길동', score=4.99
WHERE teacher_name='홍길동';

-- 데이터 삭제 쿼리
DELETE FROM teacher;
DELETE FROM teacher
WHERE teacher_id=2;
