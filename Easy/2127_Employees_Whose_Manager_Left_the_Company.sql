-- Problem: Employees Whose Manager Left the Company
-- Problem ID: 2127
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 301 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-18

SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND m.employee_id IS NULL
ORDER BY e.employee_id;