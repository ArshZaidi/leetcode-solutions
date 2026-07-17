-- Problem: Find Total Time Spent by Each Employee
-- Problem ID: 1892
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 530 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-17

SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day;