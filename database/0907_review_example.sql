-- 1~번 문제는 어제 작성한 university 데이터베이스를 사용하세요.
USE university;
SELECT * FROM student;


-- 1. SELECT 절에서의 서브쿼리
# 4개의 전공에 대해서, 전공 별 최저 학점을 출력하세요.
SELECT major, MIN(score) FROM student GROUP BY major;
# 4개의 전공에 대해서, 전공 별 최고 학점을 출력하세요.
SELECT major, MAX(score) FROM student GROUP BY major;
# 8명의 학생들에 대해서,
# 이름, 전공, 학점, 해당 학생과 같은 전공의 최저, 최고 학점을 출력하세요.
# 전공의 최저, 최고 학점은 위 두 쿼리를 각각 이용하되,
# 위 쿼리들은 결과 행이 여러 개이므로 하나의 결과만 선택할 수 있도록 전공이 일치하는 경우를 검사하는 조건절을 위 쿼리들에 추가하세요.
SELECT 
	name, major, score,
	(SELECT major, MIN(score) FROM student WHERE s1.major LIKE s2.major GROUP BY major) AS'min_score_in_major',
    (SELECT major, MAX(score) FROM student WHERE s1.major LIKE s2.major GROUP BY major) AS'max_score_in_major'
FROM 
	student s1

# 4개의 학년에 대해서, 학년 별 최저 학점을 출력하세요.

# 4개의 학년에 대해서, 학년 별 최고 학점을 출력하세요.

# 8명의 학생들에 대해서,
# 이름, 학년, 학점, 해당 학생과 같은 학년의 최저, 최고 학점을 출력하세요.
# 학년의 최저, 최고 학점은 위 두 쿼리를 각각 이용하되,
# 위 쿼리들은 결과 행이 여러 개이므로 하나의 결과만 선택할 수 있도록 학년이 일치하는 경우를 검사하는 조건절을 위 쿼리들에 추가하세요.



-- 2. FROM 절에서의 서브쿼리
# 전공 별 전공, 최고 학점을 출력하세요.
# 이 때, 최고 학점 열에는 'score' 별칭을 추가하세요.
SELECT major, MAX(score) AS 'score' FROM student GROUP BY major;
# student 테이블에서 이름, 전공, 학점을 출력하세요.
# 이 때, FROM 절에 student, 위 서브쿼리 두 테이블을 작성해서 각각 별칭을 적절히 추가하고,
# WHERE 절에 두 테이블의 전공이 같고, 두 테이블의 학점이 같은 경우의 조건을 추가하세요.
# (A)
SELECT
	name, major, score
FROM student s1, (SELECT major, MAX(score) AS 'score' FROM student GROUP BY major) s2
WHERE s1.major LIKE s2.major AND s1.score= s2.score;

SELECT name, major, score
FROM student
WHERE (major, score) IN (SELECT major, MAX(score) AS 'score' FROM student GROUP BY major);

# 학년 별 학년, 최고 학점을 출력하세요.
# 이 때, 최고 학점 열에는 'score' 별칭을 추가하세요.
SELECT grade, MAX(score) AS 'score' FROM student GROUP BY grade;
# student 테이블에서 이름, 학년, 학점을 출력하세요.
# 이 때, FROM 절에 student, 위 서브쿼리 두 테이블을 작성해서 각각 별칭을 적절히 추가하고,
# WHERE 절에 두 테이블의 학년이 같고, 두 테이블의 학점이 같은 경우의 조건을 추가하세요.
# (B)
SELECT name, grade, score
FROM student s1, (SELECT grade, MAX(score) AS 'score' FROM student GROUP BY grade) s2
WHERE s1.grade = s2.grade AND s1.score = s2.score;

SELECT name, grade, score
FROM student
WHERE (grade, score) IN (SELECT grade, MAX(score) AS 'score' FROM student GROUP BY grade);
# FROM 절에 (A), (B) 두 테이블을 작성해서 각각 별칭을 적절히 추가하고,
# 이름, 전공, 학년, 학점을 출력하세요.
# 이 때, 두 테이블에서 이름이 같은 경우의 조건을 추가하세요.
SELECT name, major, grade, score
FROM
	(SELECT s1.name, s1.major, s1.score
	FROM student s1, (SELECT major, MAX(score) AS 'score' FROM student GROUP BY major) s2
    WHERE s1.major LIKE s2.major AND s1.score = s2.score) A,
	(SELECT s1.name, s1.major, s1.score
	FROM student s1, (SELECT major, MAX(score) AS 'score' FROM student GROUP BY major) s2
    WHERE s1.major = s2.major AND s1.score = s2.score) B
# WHERE A.name LIKE B.name;
WHERE A.score = B.score;

-- 3. WHERE 절에서의 서브쿼리
# 8명의 학생들의 평균 학점을 출력하세요.
SELECT AVG(score) FROM student;
# 학생들의 이름, 학점을 출력하세요.
# 이 때, 8명의 평균 학점보다 낮은 학점을 취득한 학생들만 출력하세요.
# (A)
SELECT name, score FROM student WHERE score < (SELECT AVG(score) FROM student);
# 학생들의 이름, 학점을 출력하세요.
# 이 때, 8명의 평균 학점보다 높은 학점을 취득한 학생들만 출력하세요.
# (B)
SELECT name, score FROM student WHERE score > (SELECT AVG(score) FROM student);
	
# (A) 서브쿼리를 FROM 절에 위치시키고 별칭을 적당히 추가한 후 평균 점수를 출력하는 쿼리를 작성하세요.
# (C)

# (B) 서브쿼리를 FROM 절에 위치시키고 별칭을 적당히 추가한 후 평균 점수를 출력하는 쿼리를 작성하세요.
# (D)

# student 테이블에서 이름, 학점을 출력하세요.
# 이 때, 학점이 (B) 이상 (C) 이하인 학생들만 출력하세요.
SELECT name, score
FROM student
WHERE
	score >=
		(SELECT AVG(score) FROM
			(SELECT name, score FROM student WHERE score <
				(SELECT AVG(score) FROM student)) C)
	AND
    score <=
		(SELECT AVG(score) FROM
			(SELECT name, score FROM student WHERE score >
				(SELECT AVG(score) FROM studemt)) D);
                