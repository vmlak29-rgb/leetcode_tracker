-- Last updated: 17/07/2026, 14:59:18
# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;