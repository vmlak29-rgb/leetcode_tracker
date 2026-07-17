-- Last updated: 17/07/2026, 14:59:01
# Write your MySQL query statement below
SELECT
    session_id,
    user_id,
    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes,
    SUM(event_type = 'scroll') AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING
    -- Duration more than 30 minutes
    session_duration_minutes > 30

    -- At least 5 scroll events
    AND scroll_count >= 5

    -- Click to scroll ratio less than 0.20
    AND (
        SUM(event_type = 'click') / SUM(event_type = 'scroll')
    ) < 0.20

    -- No purchases
    AND SUM(event_type = 'purchase') = 0

ORDER BY
    scroll_count DESC,
    session_id ASC;