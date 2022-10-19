# MySQL 한 줄 주석
-- SQL 표준 한 줄 주석
/*
여러
줄
주석
*/
-- 쿼리 작성 후 반드시 마지막에 세미콜론(;) 작성할 것.
-- 예약어(Keyword): 사전에 약속되어 있는 단어, 특별한 동작을 수행.
-- 예약어는 일반적으로 대문자, 데이터베이스명, 테이블명은 소문자로 작성.

-- Workbench 조작 관련
-- 쿼리 작성 시 대소문자 구별하지 않음(Windows 운영체제 한정?)
-- ctrl+enter: 한 줄 실행 단축키
-- 데이터 조회 시, 데이터베이스명을 선택하지 않으면 sys 데이터베이스를 기본으로 설정.
-- 데이터베이스 우클릭 - Set as Default Schema 설정 시 조작을 위한 기본 데이터베이스로 설정.

-- SELECT문
-- 테이블에서 데이터를 조회하는 문장.

-- SELECT [선택할 열1], [선택할 열2], ... FROM [테이블명1], [테이블명2], ...
SELECT name, countrycode FROM city;
SELECT countrycode, region FROM city, country;  -- 여러 테이블에서 선택할 때
SELECT city.name, country.population from city, country;  -- 두 테이블에서 같은 이름을 가진 열 선택 시 주의
SELECT ct.name, co.population FROM city AS ct, country AS co;  -- 테이블명 별칭(alias)
SELECT ct.name AS '이름', co.population AS '인구수' FROM city AS ct, country AS co;  -- 열명 별칭

-- SELECT * FROM [테이블명1], [테이블명2], ...
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM city, country;

-- SELECT ... FROM ... WHERE [조건식]
SELECT name, population FROM city WHERE population > 8000000;
SELECT name, population FROM country WHERE population > 100000000;


-- 자료형
-- 데이터의 형태, 종류
-- 테이블 생성 시 주로 다룸

-- 정수형
-- TINYINT: 1byte(-128~127)의 크기를 가지는 정수 자료형
-- SMALLINT: 2bytes(-32768~32767)의 크기를 가지는 정수 자료형
-- MEDIUMINT: 3bytes의 크기를 가지는 정수 자료형
-- INT: 4bytes의 크기를 가지는 정수 자료형
-- BIGINT: 8bytes의 크기를 가지는 정수 자료형

-- 논리형: MySQL에서는 논리형을 1(TRUE), 0(FALSE)으로 표현(TINYINT 자료형으로 자동 변환됨)
-- BOOL
-- BOOLEAN
SELECT 1 = 1, 1 = 0, 0 != 1, 0 != 0;

-- 실수형
-- DECIMAL: 가변 크기를 가지는 고정 소수점 실수 자료형, DECIMAL(정밀도, 소수점자리수)
-- FLOAT: 4bytes의 크기를 가지는 부동 소수점 실수 자료형, deprecated
-- DOUBLE: 8bytes의 크기를 가지는 부동 소수점 실수 자료형, deprecated

-- 문자열
-- CHAR: 최대 255bytes의 크기를 가지는 문자열, CHAR(글자수), 255자까지 제한 가능
-- VARCHAR: 최대 65535bytes의 크기를 가지는 문자열, VARCHAR(글자수), 약 65535자까지 제한 가능
-- 한글 데이터는 한 글자당 2~3bytes를 할당하기 때문에 테이블 생성 시 한글 데이터 저장 유의할 것.
-- 작은 따옴표, 큰 따옴표 모두 사용 가능
-- 문자열 안에 따옴표 표현하려면 '', "", \', \" 사용
SELECT 'hello', "world", "I'm student.", 'He says, "I''m happy"';
-- 문자열과 숫자 값 비교 가능
SELECT '1' = 1, '123' = 123;
-- 문자열을 날짜형으로 취급 가능
SELECT * FROM sakila.rental WHERE rental_date = '2005-05-24 22:53:30';

-- 날짜형
-- DATE: 3bytes의 크기를 가지는 날짜 자료형.
-- TIME: 3bytes의 크기를 가지는 시간 자료형.
-- DATETIME: 8bytes의 크기를 가지는 날짜-시간 자료형.
-- TIMESTAMP: 4bytes의 크기를 가지는 epoch 시간 자료형.
SELECT '2022-08-29', '15:14:13', '2022-08-29 15:14:13';
SELECT NOW(), SYSDATE();  -- 현재 시간을 구하는 함수.
SELECT NOW(), SLEEP(3), NOW();  -- NOW()는 쿼리 실행 전 시간을 구함.
SELECT SYSDATE(), SLEEP(3), SYSDATE();  -- SYSDATE()는 실행할 때마다 시간을 새로 구함.
-- 문자열을 날짜로 변환할 때 시간 정보를 입력하지 않으면 0시 0분 0초로 설정됨.
SELECT * FROM sakila.rental
WHERE rental_date = '2005-05-24';
SELECT * FROM sakila.rental
WHERE rental_date >= '2005-05-24' and rental_date <= '2005-05-25';
SELECT * FROM sakila.rental
WHERE rental_date >= '2005-05-24 00:00:00' and rental_date <= '2005-05-25 23:59:59';

-- null: 아무 데이터도 없다는 걸 표현하기 위한 값.

-- 연산자
-- 산술 연산자(+, -, *, /, DIV, MOD, %)
SELECT 10 / 3, 10 DIV 3, 10 MOD 3, 10 % 3;
-- 비교 연산자(=, !=, <>, >, >=, <, <=)
SELECT 10 = 20 - 10, 1 != 2, 1 <> 2, 10 > 20, 100 < 10;
-- 논리 연산자(AND, OR, NOT, &&, ||, !)
SELECT 1 AND 1, 1 AND 0, 0 AND 1, 0 AND 0;
SELECT 1 OR 1, 1 OR 0, 0 OR 1, 0 OR 0;
SELECT NOT 1, NOT 0;
SELECT 1 && 1, 1 && 0, 0 && 1, 0 && 0;
SELECT 1 || 1, 1 || 0, 0 || 1, 0 || 0;
SELECT !1, !0;
SELECT Name, LifeExpectancy, GNP FROM country
WHERE LifeExpectancy > 70 AND GNP > 5000;
SELECT Name, Region FROM country
WHERE Region = 'North America' OR Region = 'South America';

-- LIKE, NOT LIKE: 문자열 비교 연산자
SELECT * FROM country WHERE name = 'South Korea';
SELECT * FROM country WHERE name LIKE 'South Korea';
SELECT * FROM country WHERE name LIKE '%Korea';  -- 여러 글자 와일드카드
SELECT * FROM country WHERE Region LIKE '%America'; -- ???America 검색
SELECT * FROM country WHERE name LIKE 'South Kore%'; -- South Kore??? 검색
SELECT * FROM country WHERE name LIKE 'South Kore_';  -- 한 글자 와일드카드
SELECT * FROM country WHERE name LIKE '_Korea'; -- ?Korea 검색
SELECT * FROM country WHERE name = '%Korea';  -- = 연산자와 와일드카드 사용 불가

-- BETWEEN A AND B: 값이 A와 B 사이에 있는지 검사
SELECT * FROM city WHERE population BETWEEN 1000 AND 2000;
SELECT * FROM city WHERE population >= 1000 AND population <= 2000;
SELECT * FROM sakila.rental
WHERE rental_date BETWEEN '2005-05-24 00:00:00' AND '2005-05-25 00:00:40';

-- IN (A, B, C, ...), NOT IN(A, B, C, ...): 멤버십 연산자
SELECT * FROM country
WHERE Region IN ('North America', 'Central America', 'South America');
SELECT * FROM country
WHERE name IN ('South Korea', 'North Korea');

-- IS, IS NOT: 값이 bool이거나 null인지 검사
SELECT 1 = 1, 1 IS TRUE, 1 IS NULL;
SELECT 0 = 0, 0 IS FALSE, 0 IS NULL;
SELECT 1 = '1', '1' IS TRUE, '' IS NULL;

-- city 테이블에서, 한국에 있는 도시를 모두 선택하세요.
SELECT * FROM city WHERE CountryCode LIKE 'KOR';
-- city 테이블에서, 한국, 일본, 중국에 있는 도시를 모두 선택하세요.
SELECT * FROM city WHERE CountryCode IN ('KOR', 'JPN', 'CHN');
-- countrylanguage 테이블에서, 중국에서 사용하는 언어를 모두 선택하세요.
SELECT * FROM countrylanguage WHERE CountryCode LIKE 'CHN';
-- country 테이블에서, 정부형태가 Republic이거나 Federal Republic인 국가를 모두 선택하세요.
SELECT * FROM country WHERE GovernmentForm LIKE '%Republic';
SELECT * FROM country WHERE GovernmentForm IN ('Republic', 'Federal Republic');
-- country 테이블에서, 독립한 년도가 1940~1950 사이인 국가를 모두 선택하세요.
SELECT * FROM country WHERE IndepYear BETWEEN 1940 AND 1950;
-- country 테이블에서, 독립한 적 있는 국가를 모두 선택하세요.
SELECT * FROM country WHERE IndepYear IS NOT NULL;








