/*Revising the Select Query I*/
/*https://www.hackerrank.com/challenges/revising-the-select-query/problem*/
SELECT *
    FROM CITY
    WHERE CountryCode='USA'
    AND Population > 100000;

/*Revising the Select Query II*/
/*https://www.hackerrank.com/challenges/revising-the-select-query-2/problem*/
SELECT Name
    FROM CITY
    WHERE Population > 120000
    AND CountryCode='USA';

/*Select All*/
/*https://www.hackerrank.com/challenges/select-all-sql/problem*/
SELECT *
    FROM CITY;

/*Select By ID*/
/*https://www.hackerrank.com/challenges/select-by-id/problem*/
SELECT *
    FROM CITY
    WHERE id=1661;

/*Japanese Cities' Attributes*/
/*https://www.hackerrank.com/challenges/japanese-cities-attributes/problem*/
SELECT *
    FROM CITY
    WHERE CountryCode="JPN";

/*Japanese Cities' Names*/
/*https://www.hackerrank.com/challenges/japanese-cities-name/problem*/
SELECT Name
    FROM CITY
    WHERE CountryCode="JPN";

/*Weather Observation Station 1*/
/*https://www.hackerrank.com/challenges/weather-observation-station-1/problem*/
SELECT City, State
    FROM STATION;

/*Weather Observation Station 3*/
/*https://www.hackerrank.com/challenges/weather-observation-station-3/problem*/
SELECT Distinct City
    FROM STATION
    WHERE id % 2 = 0;

/*Weather Observation Station 4*/
/*https://www.hackerrank.com/challenges/weather-observation-station-4/problem*/
SELECT COUNT(City) - COUNT(Distinct City)
    FROM STATION;

/**/
/**/


/**/
/**/


/**/
/**/