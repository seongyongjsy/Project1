-- 1~5번 문제는 world 데이터베이스를 사용하세요.
USE world;


-- 1.
# city 테이블의 모든 레코드 수(A)를 구하는 쿼리를 작성하세요.
SELECT COUNT(*) FROM city;
# country 테이블의 모든 레코드 수(B)를 구하는 쿼리를 작성하세요.
SELECT COUNT(*) FROM country;
# city 테이블과 country 테이블의 모든 레코드의 조합의 수(C)를 구하는 쿼리를 작성하세요.
SELECT COUNT(*) FROM city CROSS JOIN country;
# A와 B를 곱하면 C와 같은지 확인하세요. 차이가 있다면 이유는 무엇인지 서술하세요.
# A와 B의 곱과 C가 서로 같음.


-- 2.
# city.countrycode 열의 데이터와 country.code 열의 데이터가 일치하는 경우에 한해서,
# 두 테이블의 레코드의 조합을 구해서 출력하는 쿼리를 작성하세요.
# 또한 이 때의 레코드의 수(A)를 확인하세요.
	SELECT COUNT(*) FROM city INNER JOIN country ON city.countrycode = country.code;
	SELECT COUNT(*) FROM country INNER JOIN city ON country.code = city.countrycode;
	SELECT COUNT(*) FROM city, country WHERE city.countrycode = country.code;
		# 4079개의 레코드 확인.
# city.countrycode 열의 데이터와 country.code 열의 데이터가 일치하는 경우에 한해서,
# 두 테이블의 레코드의 조합을 구해서 출력하는 쿼리를 작성하세요.
# 단, 레코드의 조합에 사용되지 않은 city 테이블의 데이터가 누락되지 않고 모두 출력되도록 하세요.
# 또한 이 때의 레코드의 수(B)를 확인하세요.
	SELECT COUNT(*) FROM city LEFT OUTER JOIN country ON city.countrycode = country.code;
    SELECT COUNT(*) FROM country RIGHT OUTER JOIN city ON country.code = city.countrycode;
		# 4079개의 레코드 확인.
# city.countrycode 열의 데이터와 country.code 열의 데이터가 일치하는 경우에 한해서,
# 두 테이블의 레코드의 조합을 구해서 출력하는 쿼리를 작성하세요.
# 단, 레코드의 조합에 사용되지 않은 country 테이블의 데이터가 누락되지 않고 모두 출력되도록 하세요.
# 또한 이 때의 레코드의 수(C)를 확인하세요.
	SELECT COUNT(*) FROM city RIGHT OUTER JOIN country ON city.countrycode = country.code;
    SELECT COUNT(*) FROM country LEFT OUTER JOIN city ON country.code = city.countrycode;
		# 4086개의 레코드 확인.
# A, B, C가 서로 같은지 확인하세요. 차이가 있다면 이유는 무엇인지 서술하세요.
	# 도시 데이터가 등록되지 않은 7개의 국가 데이터가 존재함!
# 도시가 등록되지 않은 국가 데이터를 출력하는 쿼리를 작성하세요.
	SELECT * FROM country LEFT OUTER JOIN city ON country.code = city.countrycode WHERE city.id IS NULL;
	SELECT * FROM country WHERE capital IS NULL;



-- 3.
# country 테이블에서 국가 코드, 국가 이름, 국가 인구 수를 출력하는 쿼리를 작성하세요.
SELECT code, name, population FROM country;
# city 테이블에서 소속 국가 코드, 도시 이름, 도시 인구 수를 출력하는 쿼리를 작성하세요.
SELECT countrycode, name, population FROM city;
# 두 테이블의 국가 코드를 이용해서 INNER JOIN(EQUI-JOIN) 하고, 국가 이름, 국가 인구 수, 도시 이름, 도시 인구 수를 출력하는 쿼리를 작성하세요.
SELECT country.name, country.population, city.name, city.population FROM country INNER JOIN city ON country.code = city.countrycode;
SELECT co.name, co.population, ci.name, ci.population FROM country co, city ci WHERE co.code = ci.countrycode;
# 위 쿼리에서, 대한민국과 그에 속한 도시 데이터만 출력하는 조건을 추가하세요.
SELECT co.name, co.population, ci.name, ci.population FROM country co, city ci WHERE co.code = ci.countrycode AND co.code LIKE 'KOR';
SELECT co.name, co.population, ci.name, ci.population FROM country co, city ci WHERE co.code = ci.countrycode AND co.name LIKE 'South Korea';
# 위 쿼리에서, city 테이블의 국가 코드로 그룹을 묶고 도시 인구 수의 합계를 구하는 열을 추가하세요.
SELECT co.name, co.population, ci.name, ci.population, SUM(ci.population)
FROM country co, city ci
WHERE co.code = ci.countrycode AND co.code LIKE 'KOR'
GROUP BY ci.countrycode;
# 위 쿼리에서, 도시 수, (도시 인구 수 총합 / 국가 인구 수) 비율을 구하는 열을 추가하세요.
SELECT co.name, co.population, ci.name, ci.population, SUM(ci.population), COUNT(ci.id), SUM(ci.population) / co.population
FROM country co, city ci
WHERE co.code = ci.countrycode AND co.code LIKE 'KOR'
GROUP BY ci.countrycode;
# 대한민국 특정 도시의 인구수가 대한민국 전체 인구 수의 몇 퍼센트를 차지하는지 구하는 쿼리.
SELECT co.name, co.population, ci.name, ci.population, ci.population / co.population as ratio
FROM country co, city ci
WHERE co.code = ci.countrycode AND co.code LIKE 'KOR' AND ci.name LIKE 'Kwangju';


-- 4.
# country, city 테이블을 INNER JOIN(EQUI-JOIN) 하고, 국가 이름, 도시 수를 출력하는 쿼리를 작성하세요.
SELECT co.name, COUNT(ci.id) FROM country co, city ci WHERE co.code = ci.countrycode GROUP BY ci.countrycode;
# country, countrylanguage 테이블을 INNER JOIN(EQUI-JOIN) 하고, 국가 이름, 사용 언어 수를 출력하는 쿼리를 작성하세요.
SELECT co.name, COUNT(la.language) FROM country co, countrylanguage la WHERE co.code = la.countrycode GROUP BY la.countrycode;


-- 5.
# country, countrylanguage 테이블을 JOIN 하고, 국가 이름, 사용 언어를 출력하는 쿼리를 작성하세요.
SELECT co.name, la.language FROM country co, countrylanguage la
WHERE co.code = la.countrycode;
# 위 쿼리에서, 사용 언어가 'English'인 경우만 출력하는 조건을 추가하세요.
SELECT co.name, la.language FROM country co, countrylanguage la
WHERE co.code = la.countrycode AND la.language LIKE 'English';
# 위 쿼리에서, 공식 언어 여부가 'T'인 경우만 출력하는 조건을 추가하세요.
SELECT co.name, la.language, la.isofficial FROM country co, countrylanguage la
WHERE co.code = la.countrycode AND la.language LIKE 'English' AND la.isofficial LIKE 'T';


-- 6~10번 문제는 sakila 데이터베이스를 사용하세요.
USE sakila;


-- 6.
# store, address 테이블을 사용해서 영업점 ID, 관리자 직원 ID, 주소, 우편 번호, 전화번호를 출력하는 쿼리를 작성하세요.
SELECT store_id, manager_staff_id, address, postal_code, phone  FROM store st, address ad WHERE st.address_id = ad.address_id;
# staff, address 테이블을 사용해서 이름, 성, 이메일, 주소, 우편 번호, 전화번호를 출력하는 쿼리를 작성하세요.
SELECT first_name, last_name, email, address, postal_code, phone FROM staff st, address ad WHERE st.address_id = ad.address_id;
# customer, address 테이블을 사용해서 이름, 성, 이메일, 주소, 우편 번호, 전화번호를 출력하는 쿼리를 작성하세요.
SELECT first_name, last_name, email, address, postal_code, phone FROM customer cu, address ad WHERE cu.address_id = ad.address_id;


-- 7.
# inventory, film 테이블을 사용해서 상품(재고) ID, 영화 제목, 영업점 ID를 출럭하는 쿼리를 작성하세요.
SELECT inventory_id, title, store_id FROM inventory, film WHERE inventory.film_id = film.film_id;
# rental, inventory 테이블을 사용해서 대여 건 ID, 영화 ID, 영업점 ID, 고객 ID를 출력하는 쿼리를 작성하세요.
SELECT rental_id, film_id, store_id, customer_id FROM rental, inventory WHERE rental.inventory_id = inventory.inventory_id;
# payment, rental 테이블을 사용해서 지불 건 ID, 상품(재고) ID, 고객 ID를 출력하는 쿼리를 작성하세요.
SELECT payment_id, inventory_id, payment.customer_id, rental.customer_id FROM payment, rental WHERE payment.rental_id = rental.rental_id;
# payment, rental 테이블을 사용해서 지불 건 ID, 상품(재고) ID, 점원 ID를 출력하는 쿼리를 작성하세요.
SELECT payment_id, inventory_id, payment.staff_id, payment.staff_id FROM payment, rental WHERE payment.rental_id = rental.rental_id;


-- 8.
# film, actor, film_actor 테이블을 사용해서 영화 제목, 출시 년도, 배우 이름, 배우 성을 출력하는 쿼리를 작성하세요.
SELECT film.title, film.release_year, actor.first_name, actor.last_name
FROM film, actor, film_actor
WHERE film.film_id = film_actor.film_id AND actor.actor_id = film_actor.actor_id;
# film, category, film_category 테이블을 사용해서 영화 제목, 관람 등급, 분류 이름을 출력하는 쿼리를 작성하세요.
SELECT film.title, film.rating, category.name
FROM film, category, film_category
WHERE film.film_id = film_category.film_id AND category.category_id = film_category.category_id;
# film, film_text 테이블을 사용해서 영화 제목, 영화 텍스트 제목을 출력하는 쿼리를 작성하세요.
SELECT film.title, film_text.title
FROM film, film_text
WHERE film.film_id = film_text.film_id;
# film, film_text 테이블을 사용해서 영화 설명, 영화 텍스트 설명을 출력하는 쿼리를 작성하세요.
SELECT film.description, film_text.description
FROM film, film_text
WHERE film.film_id = film_text.film_id;


-- 9. 고객 이름, 고객 성, 등록된 주소, 해당 도시 이름, 소속 국가 이름을 출력하는 쿼리를 작성하세요.
SELECT
	cu.first_name, cu.last_name,
    ad.address,
    ci.city,
    co.country
FROM
	customer cu, address ad, city ci, country co
WHERE
	cu.address_id = ad.address_id
    AND
    ad.city_id = ci.city_id
    AND
    ci.country_id = co.country_id;


-- 10. 대여일, 대여한 영화 제목, 대여한 고객의 '이름 성'을 출력하는 쿼리를 작성하세요.
SELECT
	r.rental_date, f.title, CONCAT_WS(' ', c.first_name, c.last_name) AS 'customer name'
FROM
	rental r, film f, customer c, inventory i
WHERE
	r.customer_id = c.customer_id
    AND
    r.inventory_id = i.inventory_id
    AND
    i.film_id = f.film_id;
