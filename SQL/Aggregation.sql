-- MySQL

-- Revising Aggregations - The Count Function
-- https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
SELECT COUNT(*)
    FROM CITY
    WHERE population > 100000;

-- Revising Aggregations - The Sum Function
-- https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
SELECT SUM(population)
    FROM CITY
    WHERE district = 'California';

-- Revising Aggregations - Averages
-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
SELECT AVG(population)
    FROM CITY
    WHERE district = 'California';

-- Average Population
-- https://www.hackerrank.com/challenges/average-population/problem
SELECT FLOOR(AVG(population))
    FROM CITY;

-- Japan Population
-- https://www.hackerrank.com/challenges/japan-population/problem
SELECT SUM(population)
    FROM CITY
    WHERE CountryCode = 'JPN';

-- Population Density Difference
-- https://www.hackerrank.com/challenges/population-density-difference/problem
SELECT MAX(population) - MIN(population)
    FROM CITY;

-- The Blunder
-- https://www.hackerrank.com/challenges/the-blunder/problem
SELECT CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))
    FROM EMPLOYEES;

-- Top Earners
--


-- Weather Observation Station 2
-- https://www.hackerrank.com/challenges/weather-observation-station-2/problem
SELECT ROUND(SUM(lat_n), 2), ROUND(SUM(long_w), 2)
    FROM STATION;

-- Weather Observation Station 13
-- https://www.hackerrank.com/challenges/weather-observation-station-13/problem
SELECT ROUND(SUM(lat_n), 4)
    FROM STATION
    WHERE (
        lat_n > 38.7880
        AND lat_n < 137.2345
    );

-- Weather Observation Station 14
-- https://www.hackerrank.com/challenges/weather-observation-station-14/problem
SELECT ROUND(MAX(lat_n), 4)
    FROM STATION
    WHERE lat_n < 137.2345;

-- Weather Observation Station 15
-- https://www.hackerrank.com/challenges/weather-observation-station-15/problem
SELECT ROUND(long_w, 4)
    FROM STATION
    WHERE lat_n < 137.2345
    ORDER BY lat_n DESC
    LIMIT 1;

-- Weather Observation Station 16
-- https://www.hackerrank.com/challenges/weather-observation-station-16/problem
SELECT ROUND(MIN(lat_n), 4)
    FROM STATION
    WHERE lat_n > 38.7780;