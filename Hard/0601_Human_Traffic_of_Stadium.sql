-- Problem: Human Traffic of Stadium
-- Problem ID: 601
-- Difficulty: Hard
-- Language: MySQL
-- Runtime: 545 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-09-17

SELECT DISTINCT s.*
FROM Stadium s
WHERE s.people >= 100
  AND (
      (
          s.id + 1 IN (SELECT id FROM Stadium WHERE people >= 100)
          AND s.id + 2 IN (SELECT id FROM Stadium WHERE people >= 100)
      )
      OR
      (
          s.id - 1 IN (SELECT id FROM Stadium WHERE people >= 100)
          AND s.id + 1 IN (SELECT id FROM Stadium WHERE people >= 100)
      )
      OR
      (
          s.id - 1 IN (SELECT id FROM Stadium WHERE people >= 100)
          AND s.id - 2 IN (SELECT id FROM Stadium WHERE people >= 100)
      )
  )
ORDER BY s.visit_date;