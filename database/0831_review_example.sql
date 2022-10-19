-- actor 테이블은 배우 ID, 이름, 성 등을 기록합니다.
-- 이 테이블에서, 이름이 C로 시작하는 레코드에 대해서,
-- 이름, 성을 출력하세요.
-- 이 때, 이름 오름차순, 성 내림차순으로 정렬하세요.
SELECT first_name, last_name FROM actor
WHERE first_name LIKE 'C%'
ORDER BY first_name ASC, last_name DESC;

-- film 테이블은 영화 ID, 제목, 대여 기간, 대여 요금, 길이(상영 시간) 등을 기록합니다.
-- 이 테이블에서, 길이가 2시간 이상인 레코드에 대해서,
-- 대여 기간, 대여 요금을 출력하세요.
-- 이 때, 중복된 데이터는 제외하고 대여 기간 오름차순으로 정렬하세요.
SELECT DISTINCT rental_duration, reental_rate FROM film
WHERE length >= 120
ORDER BY rental_duration;

-- customer 테이블은 고객 ID, 등록된 가게 ID, 이름, 성, 이메일, 이용 가능 상태 등을 기록합니다.
-- 이 테이블에서, 등록된 가게 ID가 1이고 이용 가능 상태가 1인 레코드에 대해서,
-- 이름, 성, 이메일 앞 부분, 이메일 뒷 부분을 출력하세요.
-- 이 때, 이메일 앞, 뒷 부분은 @ 기호를 기준으로 나누고,
-- 데이터 생성일 오름차순으로 정렬하세요.
SELECT 
	first_name, last_name, email,
#	LEFT(email, INSTR(email, '@')-1),
#	RIGHT(email, CHAR_LENGTH(email) - INSTR(email, '@')) AS 'email_back',
	SUBSTRING_INDEX(email, '@', 1) AS 'customer_email_id',
    SUBSTRING_INDEX(email, '@', -1) AS 'customer_email_domain'
FROM customer
WHERE store_id = 1 AND active = 1
ORDER BY creat_date;	



-- address 테이블은 주소, 해당 주소가 속한 도시 ID, 우편 번호, 전화 번호 등을 기록합니다.
-- 이 테이블에서, 전화 번호가 12자리인 레코드에 대해서,
-- 도시 ID, 주소, 전화번호를 출력하세요.
-- 이 때, 주소는 숫자-... 형식으로,
-- 전화번호는 1234-5678-0123 형식으로 출력하세요.
SELECT 
	city_id,
    CONCAT(SUBSTRING(address, 1, INSTR(address, ' ')-1),'-...'),
    CONCAT(
    SUBSTRING(address, 1, INSTR(address, ' ')-1),
    '-',
    SUBSTRING(address, INSTR(address, ' ')+1)
    ) AS adr,
    INSERT(address, INSTR(address, '  '), 1, '-') AS adr2,
    phone
FROM address
WHERE CHAR_LENGTH(phone) = 12;


-- rental 테이블은 대여 건 ID, 대여 일자, 반납 일자 등을 기록합니다.
-- 이 테이블에서, 5월에 대여된 건에 대해서,
-- 대여 일자, 반납 일자, 대여 기간을 출력하세요.
-- 이 때, 대여 기간은 일(day) 단위로 계산하세요.
SELECT
	rental_date, return_date,
    DATEDIFF(return_date, rental_date) AS 'rental_duration1',
    TIMESTAMPDIFF(DAY, rental_date, return_date) AS 'rental_duration2'
FROM rental
# WHERE MONTH(rental_date) = 5;
WHERE rental_date BETWEEN '2005-05-01 00:00:00' AND '2005-05-31 23:59:59';


-- payment 테이블은 지불 건 ID, 고객 ID, 대여 건 ID, 지불 금액, 지불 일자 등을 기록합니다.
-- 이 테이블에서, 고객 ID가 1인 레코드에 대해서,
-- 고객 ID, 대여 건 ID, 지불 금액, 지불 일자를 출력하세요.
-- 이 때, 지불 금액은 소수점 두 번째 자리에서 반올림하고, 
-- 지불 일자는 mm-dd 형식으로 출력하세요.



SELECT
	customer_id, rental_id,
	ROUND(amount, 1) AS 'amnt',
	/*CONCAT(
    LPAD(MONTH(payment_date), 2, '0'),
	'-',
    LPAD(DAY(payment_date), 2, '0')
    ) AS 'payment_id' */
    DATE_FORMAT(payment_date, '%m-%d')
FROM payment
WHERE customer_id = 1;





