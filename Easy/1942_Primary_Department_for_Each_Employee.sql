-- Problem: Primary Department for Each Employee
-- Problem ID: 1942
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 519 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-17

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
   OR employee_id IN (
        SELECT employee_id
        FROM Employee
        GROUP BY employee_id
        HAVING COUNT(*) = 1
   );