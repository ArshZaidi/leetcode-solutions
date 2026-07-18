-- Problem: Employees With Missing Information
-- Problem ID: 2110
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 557 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-18

SELECT employee_id
FROM Employees
LEFT JOIN Salaries USING(employee_id)
WHERE salary IS NULL

UNION

SELECT employee_id
FROM Salaries
LEFT JOIN Employees USING(employee_id)
WHERE name IS NULL

ORDER BY employee_id;