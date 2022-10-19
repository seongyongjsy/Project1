-- 서브쿼리 예제
USE world;

# 전체 4079개의 도시의 평균 인구 수를 구하는 쿼리.
SELECT AVG(population) FROM city;
# 전체 도시 인구 수 평균을 넘는 도시 목록을 출력하는 쿼리.
SELECT name, population FROM city
WHERE population > (SELECT AVG(population) FROM city);

# 국가 별 도시의 평균 인구 수를 구하는 쿼리.
SELECT countrycode, AVG(population) FROM city GROUP BY countrycode;
# 도시 이름, 인구 수, 해당 도시가 위치한 국가의 평균 인구 수를 구하는 쿼리.
SELECT
	name, population,
    (SELECT
		AVG(population)
	FROM city c1
    WHERE c1.countrycode LIKE c2.countrycode
    GROUP BY countrycode) AS 'avg_pop_per_country'
FROM city c2;

# 대한민국의 자치 구역 별 도시의 평균 인구 수를 구하는 쿼리.
SELECT district, AVG(population) FROM city
WHERE countrycode LIKE 'KOR' GROUP BY district;
# 대한민국의 도시들 중 자치 구역 별 평균 인구 수 이상인 도시들만 출력하는 쿼리.
SELECT
	c1.name, c1.district, c1.population
FROM
	city c1, (
		SELECT district, AVG(population) AS 'avg_pop_per_dist'
        FROM city
		WHERE countrycode LIKE 'KOR'
        GROUP BY district
    ) c2
WHERE
	c1.countrycode LIKE 'KOR'
    AND c1.district LIKE c2.district
    AND c1.population >= c2.avg_pop_per_dist;


USE sakila;

# 각 배우의 영화 출연 횟수.
SELECT actor_id, COUNT(*) AS 'total_count' FROM film_actor GROUP BY actor_id;
# 모든 배우들의 평균 영화 출연 횟수.
SELECT AVG(total_count) FROM
	(SELECT COUNT(*) AS 'total_count' FROM film_actor GROUP BY actor_id) t;
# 모든 배우들의 평균 영화 출연 횟수보다 더 많이 출연한 배우들 목록.
SELECT actor_id, COUNT(*) AS 'total_count' FROM film_actor GROUP BY actor_id
HAVING COUNT(*) >
	(SELECT AVG(total_count) FROM
		(SELECT COUNT(*) AS 'total_count' FROM film_actor GROUP BY actor_id) t);

# 각 영화의 출연자 수.
SELECT film_id, COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id;
# 모든 영화들의 평균 출연자 수.
SELECT AVG(total_count) FROM
	(SELECT COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id) t;
# 모든 영화들의 평균 출연자 수보다 더 많은 출연자 수를 가지는 영화들 목록.
SELECT film_id, COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id
HAVING COUNT(*) >
	(SELECT AVG(total_count) FROM
		(SELECT COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id) t);
# 위 쿼리에서, 영화 제목 출력하기
SELECT title, total_count
FROM film,
	(SELECT film_id, COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id
		HAVING COUNT(*) >
			(SELECT AVG(total_count) FROM
				(SELECT COUNT(*) AS 'total_count' FROM film_actor GROUP BY film_id) t)) t
WHERE film.film_id = t.film_id;







