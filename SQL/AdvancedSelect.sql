-- MySQL

-- Type of Triangle
-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem
SELECT CASE
    WHEN A + B > C AND B + C > A AND A + C > B THEN
        CASE
            WHEN A = B AND B = C THEN 'Equilateral'
            WHEN A = B OR A = C OR B = C THEN 'Isosceles'
            ELSE 'Scalene'
        END
    ELSE
        'Not A Triangle'
    END
FROM TRIANGLES;

-- The PADS
-- https://www.hackerrank.com/challenges/the-pads/problem
SELECT
    CASE
        WHEN occupation = 'Doctor' THEN CONCAT(name, '(D)')
        WHEN occupation = 'Professor' THEN CONCAT(name, '(P)')
        WHEN occupation = 'Singer' THEN CONCAT(name, '(S)')
        WHEN occupation = 'Actor' THEN CONCAT(name, '(A)')
    END
    FROM OCCUPATIONS
    ORDER BY name;
SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.')
    FROM OCCUPATIONS
    GROUP BY occupation
    ORDER BY COUNT(occupation), occupation;