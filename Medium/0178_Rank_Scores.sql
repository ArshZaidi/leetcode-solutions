-- Problem: Rank Scores
-- Problem ID: 178
-- Difficulty: Medium
-- Language: MySQL
-- Runtime: 289 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-20

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;