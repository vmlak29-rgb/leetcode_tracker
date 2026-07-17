-- Last updated: 17/07/2026, 15:00:14
# Write your MySQL query statement below
SELECT
    MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) t;