-- Last updated: 17/07/2026, 15:00:21
# Write your MySQL query statement below
SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;