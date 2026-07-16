-- Problem: Replace Employee ID With The Unique Identifier
-- Problem ID: 1509
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 1325 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    e.unique_id,
    p.name
FROM Employees p
LEFT JOIN EmployeeUNI e
ON p.id = e.id;