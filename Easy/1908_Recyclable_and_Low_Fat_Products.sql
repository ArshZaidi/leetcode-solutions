-- Problem: Recyclable and Low Fat Products
-- Problem ID: 1908
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 600 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-17

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';