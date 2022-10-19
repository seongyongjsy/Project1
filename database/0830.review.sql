-- world.city 테이블 사용
-- 1. 서울, 대전, 대구, 부산의 도시명, 관할 구역, 인구 수 출력하기
SELECT name, district, population FROM city
WHERE district IN ('Seoul', 'Taejon', 'Taegu', 'Pusan');

-- 2. 대한민국의 도시들 중 인구 수가 10만 미만이거나 100만 초과인 모든 도시들의 도시명, 인구 수 출력하기
SELECT name, population FROM city
WHERE countrycode = 'KOR' AND (population < 100000 OR population > 1000000);

-- 3. 대한민국의 도시들 중 관할 구역이 전라도인 모든 도시들의 도시명, 관할 구역, 인구 수 출력하기
SELECT name, district, population FROM city
WHERE countrycode = 'KOR' AND district LIKE 'Cholla%';
SELECT name, district, population FROM city
WHERE countrycode = 'KOR' AND district IN('Chollabuk','Chollanam');

-- world.country 테이블 사용
-- 4. 아시아에 속한 모든 국가들의 국가 코드, 국가명, 지역 출력하기
SELECT code, name, region FROM country
WHERE region LIKE '%Asia';

-- 5. 국가명, 국토 면적, 인구 수, 국토 면적 당 인구 수 출력하기
SELECT name, surfacearea, population, population / surfacearea FROM country;
SELECT name, population, surfacearea, population / surfacearea FROM country;

-- 6. 국가명, 국토 면적, GNP, 국토 면적 당 GNP 출력하기
SELECT name, surfacearea, gnp, gnp / surfacearea AS ratio FROM country;
SELECT name, gnp, population, gnp / population AS ratio FROM country; -- 인구 1명당 생산량(GNP)

-- world.country.
-- 7. 한국어를 사용하는 모든 국가들의 국가 코드, 언어, 사용 비율 출력하기
SELECT countrycode, language, percentage FROM countrylanguage
WHERE language = 'Korean';
SELECT * FROM country WHERE code = 'PRK';

-- 8. 영어를 국가 공식 언어로 사용하는 모든 국가들의 국가 코드 출력하기
SELECT countrycode, IsOfficial FROM countrylanguage
WHERE language LIKE '%english' AND isofficial LIKE 'T';

-- 9. 국가 공식 언어의 사용 비율이 10% 미만인 모든 국가들의 국가 코드, 사용 비율 출력하기.
SELECT countrycode, percentage FROM countrylanguage
WHERE isofficial LIKE 'T' AND percentage < 10.0;