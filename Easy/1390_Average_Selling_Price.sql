-- Problem: Average Selling Price
-- Problem ID: 1390
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 767 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT p.product_id, ROUND(
    IFNULL(SUM(p.price * s.units)/SUM(units),0), 2
    ) AS average_price

FROM Prices AS p
LEFT JOIN UnitsSold AS s
ON p.product_id = s.product_id
AND s.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;