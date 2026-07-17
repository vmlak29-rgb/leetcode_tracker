-- Last updated: 17/07/2026, 15:01:24
# Write your MySQL query statement below
SELECT
    email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;