-- Last updated: 17/07/2026, 15:01:28
# Write your MySQL query statement below
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;