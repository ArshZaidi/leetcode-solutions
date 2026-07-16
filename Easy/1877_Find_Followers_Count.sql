-- Problem: Find Followers Count
-- Problem ID: 1877
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 614 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;