-- Last updated: 17/07/2026, 14:59:20
# Write your MySQL query statement below
SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;