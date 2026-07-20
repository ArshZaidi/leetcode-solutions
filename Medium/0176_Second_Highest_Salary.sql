-- Problem: Second Highest Salary
-- Problem ID: 176
-- Difficulty: Medium
-- Language: MySQL
-- Runtime: 269 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-20

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;