-- Problem: Group Sold Products By The Date
-- Problem ID: 1625
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 396 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;