-- Problem: Invalid Tweets
-- Problem ID: 1827
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 798 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;