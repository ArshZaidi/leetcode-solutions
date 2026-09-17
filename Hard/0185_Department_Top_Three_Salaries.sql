-- Problem: Department Top Three Salaries
-- Problem ID: 185
-- Difficulty: Hard
-- Language: MySQL
-- Runtime: 1964 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-09-17

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
      AND e2.salary > e.salary
);