-- Last updated: 17/07/2026, 15:00:29
# Write your MySQL query statement below
SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;