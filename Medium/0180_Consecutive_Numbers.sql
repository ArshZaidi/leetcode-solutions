-- Problem: Consecutive Numbers
-- Problem ID: 180
-- Difficulty: Medium
-- Language: MySQL
-- Runtime: 553 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-20

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id = l2.id - 1
JOIN Logs l3
    ON l2.id = l3.id - 1
WHERE l1.num = l2.num
  AND l2.num = l3.num;