-- Last updated: 17/07/2026, 15:00:13
# Write your MySQL query statement below
SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;