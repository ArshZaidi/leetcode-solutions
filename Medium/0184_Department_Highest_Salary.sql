-- Problem: Department Highest Salary
-- Problem ID: 184
-- Difficulty: Medium
-- Language: MySQL
-- Runtime: 1075 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-20

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);