-- MySQL

--
--


-- African Cities
-- https://www.hackerrank.com/challenges/african-cities/problem
SELECT name
    FROM CITY
    WHERE CountryCode IN
        (
            SELECT code 
                FROM COUNTRY 
                WHERE continent = 'Africa'
        );