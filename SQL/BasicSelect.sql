-- MySQL

-- Revising the Select Query I
-- https://www.hackerrank.com/challenges/revising-the-select-query/problem
SELECT *
    FROM CITY
    WHERE CountryCode='USA'
    AND Population > 100000;

-- Revising the Select Query II
-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
SELECT Name
    FROM CITY
    WHERE Population > 120000
    AND CountryCode='USA';

-- Select All
-- https://www.hackerrank.com/challenges/select-all-sql/problem
SELECT *
    FROM CITY;

-- Select By ID
-- https://www.hackerrank.com/challenges/select-by-id/problem
SELECT *
    FROM CITY
    WHERE id=1661;

-- Japanese Cities' Attributes
-- https://www.hackerrank.com/challenges/japanese-cities-attributes/problem
SELECT *
    FROM CITY
    WHERE CountryCode="JPN";

-- Japanese Cities' Names
-- https://www.hackerrank.com/challenges/japanese-cities-name/problem
SELECT name
    FROM CITY
    WHERE CountryCode="JPN";

-- Weather Observation Station 1
-- https://www.hackerrank.com/challenges/weather-observation-station-1/problem
SELECT city, state
    FROM STATION;

-- Weather Observation Station 3
-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem
SELECT Distinct city
    FROM STATION
    WHERE id % 2 = 0;

-- Weather Observation Station 4
-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem
SELECT COUNT(city) - COUNT(Distinct city)
    FROM STATION;

-- Weather Observation Station 5
-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem
SELECT city, LENGTH(city)
    FROM STATION
    ORDER BY LENGTH(city), city
    LIMIT 1;
SELECT city, LENGTH(city)
    FROM STATION
    ORDER BY LENGTH(city) DESC, city
    LIMIT 1;

-- Weather Observation Station 6
-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city REGEXP '^[aeiou].*';

-- Weather Observation Station 7
-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city REGEXP '.[aeiou]$';

-- Weather Observation Station 8
-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city REGEXP '^[aeiou].*[aeiou]$';

-- Weather Observation Station 9
-- https://www.hackerrank.com/challenges/weather-observation-station-9/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city NOT REGEXP "^[aeiou].*";

-- Weather Observation Station 10
-- https://www.hackerrank.com/challenges/weather-observation-station-10/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city NOT REGEXP ".[aeiou]$";

-- Weather Observation Station 11
-- https://www.hackerrank.com/challenges/weather-observation-station-11/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city REGEXP "^[^aeiou]|[^aeiou]$";

-- Weather Observation Station 12
-- https://www.hackerrank.com/challenges/weather-observation-station-12/problem
SELECT DISTINCT city
    FROM STATION
    WHERE city REGEXP "^[^aeiou].*[^aeiou]$";

-- Employee Names
-- https://www.hackerrank.com/challenges/name-of-employees/problem
SELECT name
    FROM Employee
    ORDER BY name;

-- Employee Salaries
-- https://www.hackerrank.com/challenges/salary-of-employees/problem
SELECT name
    FROM Employee
    WHERE (
        salary > 2000
        AND months < 10
    )
    ORDER BY employee_id;

-- Higher Than 75 Marks
-- https://www.hackerrank.com/challenges/more-than-75-marks/problem
SELECT name
    FROM STUDENTS
    WHERE marks > 75
    ORDER BY RIGHT(name, 3), id;

