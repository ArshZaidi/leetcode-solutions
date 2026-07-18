-- Problem: The Latest Login in 2020
-- Problem ID: 2041
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 618 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-18

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id
ORDER BY user_id;