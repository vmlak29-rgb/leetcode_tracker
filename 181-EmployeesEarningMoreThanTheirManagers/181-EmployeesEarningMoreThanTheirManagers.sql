-- Last updated: 17/07/2026, 15:01:25
# Write your MySQL query statement below
SELECT
    e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;