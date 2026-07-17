-- Last updated: 17/07/2026, 15:00:28
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id IS NULL
   OR referee_id <> 2;