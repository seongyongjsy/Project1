-- ORDER BY 절: 테이블 조회 결과 정렬할 기준 열을 지정할 때 사용하는 문법
-- 기본은 오름차순 정렬
SELECT * FROM city WHERE countrycode LIKE 'KOR' ORDER BY population;
-- 열 이름 뒤에 ASC 붙이면 오름차순 정렬
SELECT * FROM city WHERE countrycode LIKE 'KOR' ORDER BY population ASC;
-- 열 이름 뒤에 DESC 붙이면 내림차순 정렬
SELECT * FROM city WHERE countrycode LIKE 'KOR' ORDER BY population DESC;
-- 문자열 값을 저장하는 열도 지정 가능(사전 순, 알파벳 순으로 정렬)
-- 기준 열 여러 개 제시 가능
SELECT name, region, population FROM country ORDER BY region ASC, population DESC;
-- 열 이름 대신 열 순서 제시 가능, 이때 SELECT 절의 열의 순서를 입력해야 함
-- ex) 4번째 열(region) 오름차순, 7번 열(population) 내림차순 정렬
SELECT * FROM country ORDER BY 4 ASC, 7 DESC;
-- ex) 2번 열(region) 오름차순, 7번 열(population) 내림차순 정렬
SELECT name, region, population FROM country ORDER BY 2 ASC, 3 DESC;


-- DISTINCT: 열 이름 앞에 써서 중복값을 제거할 때 사용
SELECT DISTINCT countrycode FROM city;  -- 국가 코드가 일치하면 중복 제거
SELECT DISTINCT id, countrycode FROM city;  -- id와 국가 코드가 모두 일치하면 중복 제거 => 의미 없음!
SELECT DISTINCT countrycode, isofficial FROM countrylanguage
WHERE isofficial LIKE 'F';  -- 국가 코드, 공식 언어 여부가 모두 일치하면 중복 제거 => 실제로 제거됨


-- LIMIT n: 출력 결과 행을 n개만큼 제한할 때 사용
SELECT * FROM city ORDER BY id DESC LIMIT 3;


-- 함수
-- 수학 관련 함수
SELECT PI(), RAND();  -- PI(): 원주율(파이)을 구하는 함수. / RAND(): 0 이상 1 미만의 임의의 실수를 구하는 함수.
SELECT DEGREES(PI()), RADIANS(180);  -- DEGREES(), RADIANS(): 각도<=>라디안 구하는 함수.
SELECT SIGN(PI()), COS(PI()), TAN(PI());  -- SIGN(), COS(), TAN(): 삼각함수를 구하는 함수.

SELECT ABS(1), ABS(-1);  -- ABS(): 절대값을 구하는 함수.
SELECT CEIL(3.1), CEILING(3.9), CEIL(-3.1);  -- CEIL(): 올림 처리하는 함수.
SELECT FLOOR(3.1), FLOOR(3.9), FLOOR(-3.1);  -- FLOOR() 내림 처리하는 함수.
SELECT TRUNCATE(3.12345, 0), TRUNCATE(3.98765, 0);  -- TRUNCATE(): 0에 가깝게 올림/내림 처리하는 함수
SELECT TRUNCATE(-3.12345, 0), TRUNCATE(-3.98765, 0);  -- 양수일 때 => FLOOR, 음수일 때 => CEIL
SELECT ROUND(1.4), ROUND(1.5), ROUND(1.6);  -- ROUND(): 반올림 처리하는 함수.
SELECT ROUND(-1.4), ROUND(-1.5), ROUND(-1.6);

SELECT POW(2, 3), POWER(10, 10), SQRT(4);  -- POW(), POWER(): 거듭제곱 / SQRT(): 제곱근


-- 문자열 관련 함수
SELECT LOWER('HELLO'), LCASE('WORLD');  -- LOWER(), LCASE(): 문자열을 소문자로 변환해주는 함수.
SELECT UPPER('hi'), UCASE('students');  -- UPPER(), UCASE(): 문자열을 대문자로 변환해주는 함수.

SELECT ASCII('A'), ASCII('a');  -- ASCII(문자): 아스키 코드 번호 값을 구하는 함수.
SELECT ORD('A'), ORD('a');  -- ORD(문자): 아스키 코드 번호 값을 구하는 함수.
SELECT CHAR(65 USING utf8), CHAR(97 USING utf8);  -- CHAR(번호 USING 인코딩): 아스키 코드 문자를 구하는 함수.

SELECT BIN(10), OCT(10), HEX(10);  -- BIN, OCT, HEX(): 2, 8, 16진법 표기 문자열을 반환하는 함수.

SELECT BIT_LENGTH('a'), BIT_LENGTH('AB');  -- BIT_LENGTH(문자열): 문자열 비트 크기를 계산.
SELECT CHAR_LENGTH('a'), CHAR_LENGTH('AB');  -- CHAR_LENGTH(문자열): 문자 개수를 계산.
SELECT LENGTH('a'), LENGTH('AB');  -- LENGTH(문자열): 문자 바이트 수를 계산.
SELECT CHAR_LENGTH('와'), LENGTH('우');  -- 한글, 한자, 일본어 문자, ...은 한 글자당 3bytes 차지.
-- CHAR(255) VARCHAR(65535) 자료형은 최대 문자 개수 제한을 입력하며, 이때 용량은 자동으로 설정됨.

SELECT INSTR('abcde', 'c');  -- INSTR(원본str, 찾을str): 문자열이 몇 번째에 있는지 구하는 함수.
SELECT POSITION('c' IN 'abcde');  -- POSITION(찾을str IN 원본str): 문자열이 몇 번째에 있는지 구하는 함수.
SELECT LOCATE('c', 'abcde');  -- LOCATE(찾을str, 원본str): 문자열이 몇 번째에 있는지 구하는 함수.
SELECT LOCATE('A', 'ABCABC'), LOCATE('A', 'ABCABC', 2);  -- 특정 위치부터 찾을지 설정 가능

SELECT SUBSTRING('abcde', 3);  -- SUBSTRING(원본str, 위치): 특정 위치부터 끝까지 부분문자열 추출
SELECT SUBSTRING('abcde', 3, 1);  -- SUBSTRING(원본str, 위치, 개수): 특정 위치부터 특정 개수 부분문자열 추출

-- SUBSTRING_INDEX(원본str, 구분자str, i번째):
-- 원본 문자열에서 구분자로 문자열을 나누고, 왼쪽에서부터 특정 번째까지 부분문자열 추출
SELECT SUBSTRING_INDEX('C:/workspace/files/test.jpg', '/', 3);
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX('www.naver.com/search', '.', -1), '/', -1);
SELECT LEFT('abcde', 3), RIGHT('abcde', 3);  -- LEFT, RIGHT(문자열, 개수): 왼/오른쪽에서 개수만큼 부분문자열 추출

-- LPAD, RPAD(원본str, 폭, 채울str): 폭 만큼 공간을 할당하고 남는 공간의 왼쪽/오른쪽에 문자열을 채움.
SELECT LPAD('abcde', 10, '+'), RPAD('abcde', 10, '-');
SELECT LPAD(1, 2, '+');
SELECT name, LPAD(population, CHAR_LENGTH(population)+1, '+') AS 'population' FROM city
WHERE countrycode LIKE 'KOR';

-- LTRIM, RTRIM, TRIM(문자열): 문자열 왼쪽/오른쪽/양쪽의 공백을 제거.
SELECT LTRIM('  AB  CD  '), CHAR_LENGTH(LTRIM('  AB  CD  '));
SELECT RTRIM('  AB  CD  '), CHAR_LENGTH(RTRIM('  AB  CD  '));
SELECT TRIM('  AB  CD  '), CHAR_LENGTH(TRIM('  AB  CD  '));

-- REPLACE(원본str, 대상str, 교체str): 원본 문자열에서 대상 문자열을 교체할 문자열로 교체.
SELECT REPLACE('__AB__CD__', '_', '');
SELECT name, countrycode, REPLACE(countrycode, 'KOR', 'Korea') AS 'country' FROM city
WHERE countrycode LIKE 'KOR';

-- INSERT(원본str, 삽입할위치, 개수, 삽입str):
-- 원본 문자열에서 삽입할 위치에 특정 개수만큼 문자를 지정해서 없애고, 해당 위치에 삽입할 문자열을 입력
SELECT INSERT('abcde', 3, 2, 'CDE');

-- CONCAT(문자열1, 문자열2, ...): 문자열들을 접합시킴.
SELECT '123' + '456', CONCAT('123', '456');
SELECT CONCAT(localname, ' - ', headofstate) FROM country;

-- CONCAT_WS(구분자, 문자열1, 문자열2, ...): 구분자와 함께 문자열들을 접합시킴.
SELECT '123' + '+' + '456', CONCAT_WS('+', '123', '456');
SELECT CONCAT_WS(' - ', localname, headofstate) FROM country;

-- REPEAT(문자열, 횟수): 문자열을 반복함 / REVERSE(): 문자열을 뒤집음
SELECT REPEAT('A', 10), REVERSE('ABCDE');


-- 날짜 관련 함수
-- NOW(): 현재 시간을 구하는 함수. 쿼리 실행 전 현재 시간을 기록함.
SELECT NOW(), SLEEP(2), NOW();
-- SYSDATE(): 현재 시간을 구하는 함수. 쿼리 실행 중 현재 시간을 기록함.
SELECT SYSDATE(), SLEEP(2), SYSDATE();
-- CURRENT_TIMESTAMP(): 현재 시간을 구하는 함수. 쿼리 실행 전 현재 시간을 기록함. TIMESTAMP 자료형으로 반환.
SELECT CURRENT_TIMESTAMP(), SLEEP(2), CURRENT_TIMESTAMP;
-- TIMESTAMP(에폭시간)으로 표현할 수 있는 범위: 1970-01-01 00:00:00 ~ 2038-?-? ?:?:?
-- CURRENT_DATE(), CURDATE(): 현재 날짜를 구하는 함수.
SELECT CURRENT_DATE(), CURDATE(), CURRENT_DATE;
-- CURRENT_TIME(), CURTIME(): 현재 시간을 구하는 함수.
SELECT CURRENT_TIME(), CURTIME(), CURRENT_TIME;

-- STR_TO_DATE(문자열, 날짜형식문자열): 문자열 데이터를 형식에 맞춰서 날짜-시간 데이터로 변환해주는 함수.
SELECT STR_TO_DATE('2023-08-30 12:34:56', '%Y-%m-%d %H:%i:%s');
SELECT STR_TO_DATE('2021/12/25', '%Y/%m/%d');
SELECT STR_TO_DATE('010203', '%H%i%s');
-- DATE_FORMAT(날짜, 날짜형식문자열): 날짜-시간 데이터를 형식에 맞춰서 문자열 데이터로 변환해주는 함수.
SELECT DATE_FORMAT(NOW(), '%Y=%m=%d %H;%m;%s');
SELECT DATE_FORMAT(NOW(), '%Y%m%d');
SELECT DATE_FORMAT(NOW(), '%H%i%s');

-- UNIX_TIMESTAMP(날짜), FROM_UNIXTIME(에폭시간): 날짜<=>에폭시간 변환해주는 함수.
SELECT UNIX_TIMESTAMP(NOW()), FROM_UNIXTIME(1661841355);
SELECT FROM_UNIXTIME(1);  -- TIMESTAMP 자료형은 시간대 정보를 적용함.

SELECT
UNIX_TIMESTAMP('2022-08-30 12:00:00')
- UNIX_TIMESTAMP('2022-08-30 23:59:59') AS RESULT;
SELECT
UNIX_TIMESTAMP(DATE_FORMAT('2022-08-30 12:00:00', '%Y-%m-%d %H:%i:%s'))
- UNIX_TIMESTAMP(DATE_FORMAT('2022-08-30 23:59:59', '%Y-%m-%d %H:%i:%s')) AS RESULT;
SELECT UNIX_TIMESTAMP('2039-01-01 00:00:00'), FROM_UNIXTIME(2177420400);

-- YEAR, MONTH, DAY, HOUR, MINUTE, SECOND(): 특정 시간 정보를 추출하는 함수.
SELECT YEAR(NOW()), MONTH(NOW()), DAY(NOW()), HOUR(NOW()), MINUTE(NOW()), SECOND(NOW());
SELECT YEAR('2022-01-01 00:00:00') - YEAR('2011-12-31 23:59:59') AS RESULT;
SELECT MONTH('2022-01-01 00:00:00') - MONTH('2011-12-31 23:59:59') AS RESULT;
SELECT DAY('2022-01-01 00:00:00') - DAY('2011-12-31 23:59:59') AS RESULT;

-- DATEDIFF(날짜1, 날짜2): 두 날짜 사이의 차이 계산
-- TIMEDIFF(시간1, 시간2): 두 시간 사이의 차이 계산
-- TIMESTAMPDIFF(기준, 날짜-시간1, 날짜-시간2): 두 날짜-시간 사이 데이터를 기준에 따라 차이 계산
SELECT UNIX_TIMESTAMP('2022-01-01 00:00:00')-UNIX_TIMESTAMP('2011-12-31 23:59:59') AS RESULT;
SELECT DATEDIFF('2022-01-01', '2011-12-31') AS RESULT;
SELECT TIMEDIFF('00:00:00', '23:59:59') AS RESULT;
SELECT TIMESTAMPDIFF(SECOND, '2022-01-01 00:00:00', '2011-12-31 23:59:59') AS RESULT;
SELECT TIMESTAMPDIFF(HOUR, '2022-08-30 00:00:00', '2022-08-30 23:59:59') AS RESULT;
SELECT
	TIMESTAMPDIFF(YEAR, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS YEAR_RESULT,
    TIMESTAMPDIFF(MONTH, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS MONTH_RESULT,
    TIMESTAMPDIFF(DAY, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS DAY_RESULT,
    TIMESTAMPDIFF(HOUR, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS HOUR_RESULT,
    TIMESTAMPDIFF(MINUTE, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS MINUTE_RESULT,
    TIMESTAMPDIFF(SECOND, '2022-01-01 00:00:00', '2023-02-02 01:01:01') AS SECOND_RESULT
;

-- DATE_ADD(날짜-시간, INTERVAL 수치 기준): 주어진 날짜-시간 데이터에서 기준과 수치만큼 더한 데이터 반환.
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL 1 YEAR) AS RESULT;
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL 1 MONTH) AS RESULT;
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL 1 DAY) AS RESULT;
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL -1 HOUR) AS RESULT;
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL -1 MINUTE) AS RESULT;
SELECT DATE_ADD('2022-06-15 12:30:30', INTERVAL -1 SECOND) AS RESULT;
-- DATE_SUB(날짜-시간, INTERVAL 수치 기준): 주어진 날짜-시간 데이터에서 기준과 수치만큼 뺀 데이터 반환.
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL 1 YEAR) AS RESULT;
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL 1 MONTH) AS RESULT;
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL 1 DAY) AS RESULT;
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL -1 HOUR) AS RESULT;
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL -1 MINUTE) AS RESULT;
SELECT DATE_SUB('2022-06-15 12:30:30', INTERVAL -1 SECOND) AS RESULT;
