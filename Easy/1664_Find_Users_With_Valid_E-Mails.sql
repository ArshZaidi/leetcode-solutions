-- Problem: Find Users With Valid E-Mails
-- Problem ID: 1664
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 754 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT *
FROM Users
WHERE REGEXP_LIKE(
    mail,
    '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$',
    'c'
);