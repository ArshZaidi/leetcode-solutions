-- Problem: Nth Highest Salary
-- Problem ID: 177
-- Difficulty: Medium
-- Language: MySQL
-- Runtime: 398 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-20

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;

    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END