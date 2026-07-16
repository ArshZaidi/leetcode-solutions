-- Problem: Patients With a Condition
-- Problem ID: 1670
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 393 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';