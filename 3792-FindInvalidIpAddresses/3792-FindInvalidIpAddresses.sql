-- Last updated: 17/07/2026, 14:58:56
# Write your MySQL query statement below
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    -- Not exactly 4 octets
    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3

    OR

    -- Any octet > 255
    CAST(SUBSTRING_INDEX(ip, '.', 1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(ip, '.', -1) AS UNSIGNED) > 255

    OR

    -- Leading zeros
    (
        LENGTH(SUBSTRING_INDEX(ip, '.', 1)) > 1
        AND LEFT(SUBSTRING_INDEX(ip, '.', 1), 1) = '0'
    )
    OR (
        LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1)) > 1
        AND LEFT(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1), 1) = '0'
    )
    OR (
        LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1)) > 1
        AND LEFT(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1), 1) = '0'
    )
    OR (
        LENGTH(SUBSTRING_INDEX(ip, '.', -1)) > 1
        AND LEFT(SUBSTRING_INDEX(ip, '.', -1), 1) = '0'
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;