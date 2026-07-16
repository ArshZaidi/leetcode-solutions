-- Problem: Fix Names in a Table
-- Problem ID: 1811
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 700 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM Users
ORDER BY user_id;