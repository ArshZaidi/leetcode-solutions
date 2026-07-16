-- Problem: The Number of Employees Which Report to Each Employee
-- Problem ID: 1882
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 654 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    e.employee_id,
    e.name,
    COUNT(r.employee_id) AS reports_count,
    ROUND(AVG(r.age), 0) AS average_age
FROM Employees e
JOIN Employees r
ON e.employee_id = r.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id;