-- Problem: Rearrange Products Table
-- Problem ID: 1948
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 715 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-17

SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL

UNION ALL

SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL

UNION ALL

SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL;