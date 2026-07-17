-- Last updated: 17/07/2026, 15:00:10
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    ELSE 'm'
END;