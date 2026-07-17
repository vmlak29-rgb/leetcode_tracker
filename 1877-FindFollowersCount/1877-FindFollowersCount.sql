-- Last updated: 17/07/2026, 14:59:16
# Write your MySQL query statement below
SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;