-- 세 테이블을 사용한 조인
USE test_db;
SELECT * FROM A;
SELECT * FROM B;

DROP TABLE C;
CREATE TABLE C (
	C_a INT,
    C_b CHAR(10)
);
INSERT INTO C VALUES (1, 'C 1번 행');
INSERT INTO C VALUES (4, 'C 2번 행');
SELECT * FROM C;

-- 크로스 조인
SELECT * FROM A CROSS JOIN B CROSS JOIN C ORDER BY A_a, B_a, C_a;
SELECT * FROM A, B, C ORDER BY A_a, B_a, C_a;

-- 내부 조인(INNER 키워드 생략)
SELECT * FROM A JOIN B ON A.A_a = B.B_a JOIN C ON B.B_a = C.C_a;  # B를 중심으로 A-B-C 조인
SELECT * FROM B JOIN C ON B.B_a = C.C_a JOIN A ON C.C_a = A.A_a;  # C를 중심으로 B-C-A 조인
SELECT * FROM C JOIN A ON C.C_a = A.A_a JOIN B ON A.A_a = B.B_a;  # A를 중심으로 C-A-B 조인
SELECT * FROM A, B, C WHERE A.A_a = B.B_a AND B.B_a = C.C_a;
SELECT * FROM A, B, C WHERE B.B_a = C.C_a AND C.C_a = A.A_a;
SELECT * FROM A, B, C WHERE C.C_a = A.A_a AND A.A_a = B.B_a;

-- 외부 조인(OUTER 키워드 생략)
SELECT * FROM A LEFT JOIN B ON A.A_a = B.B_a LEFT JOIN C ON B.B_a = C.C_a;
SELECT * FROM A RIGHT JOIN B ON A.A_a = B.B_a RIGHT JOIN C ON B.B_a = C.C_a;
SELECT * FROM A LEFT JOIN B ON A.A_a = B.B_a RIGHT JOIN C ON B.B_a = C.C_a;
SELECT * FROM A RIGHT JOIN B ON A.A_a = B.B_a LEFT JOIN C ON B.B_a = C.C_a;


-- 서브쿼리(Sub-query)
CREATE DATABASE university;
USE university;
CREATE TABLE student (
	student_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name CHAR(10) NOT NULL,  -- 이름
    major CHAR(10) NOT NULL,  -- 전공
    grade TINYINT CHECK (grade IN (1, 2, 3, 4)),  -- 학년
    score DECIMAL(3, 2) CHECK (score >= 0.00 AND score <= 4.50)  -- 학점
);
INSERT INTO student (name, major, grade, score) VALUES ('홍길동', '컴퓨터공학', 1, 1.5);
INSERT INTO student (name, major, grade, score) VALUES ('김철수', '경영학', 1, 2.0);
INSERT INTO student (name, major, grade, score) VALUES ('김영희', '국문학', 2, 2.2);
INSERT INTO student (name, major, grade, score) VALUES ('바둑이', '영문학', 2, 2.5);
INSERT INTO student (name, major, grade, score) VALUES ('손오공', '컴퓨터공학', 3, 3.3);
INSERT INTO student (name, major, grade, score) VALUES ('사오정', '경영학', 3, 3.5);
INSERT INTO student (name, major, grade, score) VALUES ('저팔계', '국문학', 4, 4.4);
INSERT INTO student (name, major, grade, score) VALUES ('삼장', '영문학', 4, 4.5);
SELECT * FROM student;

-- 서브쿼리: SELECT를 통해 데이터를 조회한 결과를 임시 테이블로 여기고, 그 테이블에서 다시 한 번 조회하는 문법.
-- SELECT, FROM, WHERE, HAVING, ORDER BY ... 사용 가능.
SELECT s.name, s.score
FROM
	(SELECT * FROM student WHERE score > 2.0) s;

-- ex) 학사 경고(2.0 이하)를 면한 학생들의 평균 학점을 구하고, 그 평균 학점보다 높은 학점을 취득한 학생 데이터 출력.
SELECT name, score
FROM student
WHERE score > (SELECT AVG(score) FROM student WHERE score > 2.0);  -- 서브쿼리 결과 1열 1행 총 데이터 개수 1개 확인할 것
-- ex) A 등급(4.0 이상)을 취득한 학생들의 학과를 구하고, 같은 학과에 속하는 학생 데이터 출력.
SELECT name, major
FROM student
WHERE major IN (SELECT major FROM student WHERE score >= 4.0);  -- 서브쿼리 실행 결과 1열 2행 총 데이터 개수 2개 확인할 것
-- ex) 학과별 최고 학점을 구하고, 같은 학점 및 학과에 속하는 학생 데이터 출력.
SELECT name, major, score
FROM student
WHERE (major, score) IN (SELECT major, MAX(score) FROM student GROUP BY major);  -- 서브쿼리 실행 결과 2열 4행 총 데이터 개수 8개 확인할 것
-- ex) 전체 학생들의 이름, 학년, 학점과, 해당 학생이 속한 학년의 평균까지 출력하는 쿼리.
SELECT
	name, grade, score, (
		SELECT AVG(score)
        FROM student s1
        WHERE s1.grade = s2.grade
        GROUP BY grade
    ) AS 'grade_avg_score'
FROM
	student s2;
# WHERE
	# s2.name LIKE '김영희';
    # s2.grade IN (3, 4);
-- ex) 전체 학생들의 이름, 학년, 학점과, 해당 학생이 속한 학과의 평균까지 출력하는 쿼리.
SELECT
	name, major, score, (
		SELECT AVG(score)
        FROM student s1
        WHERE s1.major = s2.major
        GROUP BY major
    ) AS 'major_avg_score'
FROM
	student s2;
-- ex) 홍길동이 속한 학과와 학년을 구하고, 학과가 일치하거나 학년이 일치하는 학생 데이터 출력.
SELECT s1.name, s1.major, s1.grade
FROM student s1, (
	SELECT major, grade
    FROM student
    WHERE name LIKE '홍길동'
) s2
WHERE s1.major LIKE s2.major OR s1.grade = s2.grade;
-- ex) 학과 별 최고 점수, 학년 별 최고 점수 출력하는 쿼리.
SELECT *
FROM
(
	SELECT major, MAX(score)
	FROM student
	GROUP BY major
) t1,
(
	SELECT grade, MAX(score)
    FROM student
    GROUP BY grade
) t2;


USE world;
-- 지역 별로, 해당 지역에 위치한 나라들의 평균 기대 수명 구하기.
SELECT region, AVG(lifeexpectancy)
FROM country
GROUP BY region;

-- 지역 별 국가들의 평균 기대 수명을 구하고, 각 국가들에 대해 해당 국가가 위치한 지역의 평균 기대 수명보다 높은 국가들만 출력하기
SELECT c.name, c.region, c.lifeexpectancy, t.avg_lifeexp
FROM country c, (
	SELECT region, AVG(lifeexpectancy) AS avg_lifeexp
	FROM country
	GROUP BY region
) t
WHERE c.region LIKE t.region AND c.lifeexpectancy > t.avg_lifeexp;



















