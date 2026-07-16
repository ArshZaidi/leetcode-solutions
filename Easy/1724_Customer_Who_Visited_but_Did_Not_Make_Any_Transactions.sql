-- Problem: Customer Who Visited but Did Not Make Any Transactions
-- Problem ID: 1724
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 1344 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;