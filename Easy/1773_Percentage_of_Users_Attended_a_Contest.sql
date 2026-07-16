-- Problem: Percentage of Users Attended a Contest
-- Problem ID: 1773
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 1478 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    contest_id,
    ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;