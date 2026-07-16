-- Problem: Bank Account Summary II
-- Problem ID: 1734
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 776 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    u.name,
    SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;