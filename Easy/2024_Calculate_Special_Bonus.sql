-- Problem: Calculate Special Bonus
-- Problem ID: 2024
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 630 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-17

SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;