-- film 테이블에서, 관람 등급 별 평균 상영 시간을 출력하세요.
SELECT rating, AVG(length) FROM film GROUP BY rating; 
	
-- film 테이블에서, 관람 등급 별 평균 상영 시간, 총합 교체 비용을 출력하세요.
SELECT rating, AVG(length), SUM(replacement_cost) FROM film GROUP BY rating;

-- film 테이블에서, 대여 기간 별 최소, 최대 대여 요금을 출력하세요.
SELECT rental_duration, MIN(rental_rate), MAX(rental_rate) FROM film GROUP BY rental_duration;

-- film 테이블에서, 대여 기간, 대여 요금 별 평균 교체 비용을 출력하세요.
SELECT rental_duration, rental_rate, AVG(replacement_cost) FROM film 
GROUP BY rental_duration, rental_rate
ORDER BY rental_duration, rental_rate;

-- payment 테이블에서, 고객 ID로 그룹을 묶어서,
-- 고객 ID 및 평균 대여 시각을 출력하세요.
SELECT customer_id, AVG(HOUR(payment_date)) FROM payment GROUP BY customer_id;
SELECT customer_id, payment_date, HOUR(payment_date);

-- payment 테이블에서, 고객 ID로 그룹을 묶어서,
-- 고객 ID가 10번 미만인 경우에 대해서,
-- 고객 ID 및 평균 대여 시각을 출력하세요.
SELECT customer_id FROM payment GROUP BY customer_id;


-- payment 테이블에서, 고객 ID로 그룹을 묶어서,
-- 평균 대여 시각이 12시 이전인 경우에 대해서,
-- 고객 ID 및 평균 대여 시각을 출력하세요.
#SELECT customer_id, AVG(HOUR(payment_date)) FROM payment
-- GROUP BY customer_id HAVING AVG(HOUR(payment_date)) FROM paymen


-- payment 테이블에서, 고객 ID로 그룹을 묶어서,
-- 고객 ID가 10번 미만이고, 평균 대여 시각이 12시 이전인 경우에 대해서,
-- 고객 ID 및 평균 대여 시각을 출력하세요.
	

-- city 테이블에서, 국가별 도시 수를 출력하세요.

-- city 테이블에서, 도시 이름 첫 글자로 그룹을 묶어서,
-- 도시 이름 첫 글자와 그룹 별 도시 수를 출력하세요.

-- city 테이블에서, 도시 이름 첫 글자로 그룹을 묶어서,
-- 도시 이름 첫 글자가 모음(A, E, I, O, U)으로 시작하는 경우에 대해서,
-- 도시 이름 첫 글자와 그룹 별 도시 수를 출력하세요.

-- country 테이블에서, 국가 이름 글자 수로 그룹을 묶어서,
-- 국가 이름 글자 수와 그룹 별 국가 수를 출력하세요.

-- country 테이블에서, 국가 이름 글자 수로 그룹을 묶어서,
-- 그룹 별 레코드 수가 10개를 넘는 경우에 대해서,
-- 국가 이름 글자 수와 그룹 별 국가 수를 출력하세요.


-- film_category 테이블에서, 장르 ID 별 영화 수를 출력하세요.

-- film_text 테이블에서, 영화 개요 문자열의 앞에서 세 번째 단어로 그룹을 묶어서,
-- 그룹 별 영화 수를 출력하세요.
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(description, ' ', 3) AS 'desc', COUNT(*) 
FROM film_text 
GROUP BY SUBSTRING_INDEX(SUBSTRING_INDEX(description, ' ', 3), ' ', -1)
ORDER BY 1;
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(description, ' ', 3), ' ', -1) FROM film_text;

-- film_actor 테이블에서, 1~99번 영화, 100~199번 영화, 200~299번 영화, ...로 그룹을 묶어서,
-- 그룹 별 총 출연 배우 수를 출력하세요.
/*
1 / 100 => 0.01 => FLOOR(...AS SIGNED) => 0
2 / 100 => 0.02 => FLOOR(...AS SIGNED) => 0
3 / 100 => 0.03 => FLOOR(...AS SIGNED) => 0
...
99 / 100 => 0.99 => FLOOR(...AS SIGNED) => 0
100 / 100 => 1.00 => FLOOR(...AS SIGNED) => 1
101 / 100 => 1.01 => FLOOR(...AS SIGNED) => 1
...
199 / 100 => 1.99 => FLOOR(...AS SIGNED) => 1
*/
SELECT FLOOR(film_id / 100 AS SIGNED) AS group_id, COUNT(*)
FROM film_actor 
GROUP BY FLOOR(film_id / 10 AS SIGNED);
SELECT film_id / 10, COUNT(actor_id)
FROM film_actor
GROUP BY film_id / 10;
SELECT CONVERT(film_id / 10, UNSIGNED), COUNT(actor_id)
FROM film_actor
GROUP BY CONVERT(film_id / 10, UNSIGNED);

-- rental 테이블에서, 시간별 대여 건 수를 출력하세요.
SELECT HOUR(rental_date), COUNT(*) FROM rental GROUP BY HOUR(rental_date) ORDER BY 1;

-- DAYNAME() 함수는 날짜 데이터를 입력받아서 요일 이름을 반환하는 함수입니다.
-- rental 테이블에서, 요일별 대여 건 수를 출력하세요.
SELECT
	rental_date,
    CASE WEEKDAY(rental_date)
		WHEN 0 THEN '월요일'
        WHEN 1 THEN '화요일'
        WHEN 2 THEN '수요일'
	END AS '요일'
FROM rental;
SELECT DAYNAME(rental_date), COUNT(*) FROM rental GROUP BY DAYNAME(rental_date);

-- YEARWEEK() 함수는 날짜 데이터를 입력받아서 년도 및 몇 번째 주인지 그 값을 정수 형태로 반환하는 함수입니다.
-- rental 테이블에서, 2005년 각 주간 대여 건 수를 출력하세요.
SELECT rental_date, WEEK(rental_date), WEEKOFYEAR(rental_date), YEARWEEK(rental_date) FROM rental;
SELECT WEEKOFYEAR(rental_date), COUNT(*) FROM rental GROUP BY YEARWEEK(rental_date);

-- rental 테이블에서, 대여 기간으로 그룹을 묶어서,
-- 대여 기간이 7일 이상이고, 그룹 별 레코드 수가 1000건을 넘는 경우에 대해서,
-- 대여 기간 및 대여 건 수를 출력하세요.
SELECT DATEDIFF(return_date, rental_date), TIMESTAMPDIFF(DAY, rental_date, return_date)
FROM rental;
SELECT DATEDIFF(return_date, rental_date), COUNT(*)
FROM rental
GROUP BY DATEDIFF(return_date, rental_date)
ORDER BY DATEDIFF(return_date, rental_date);