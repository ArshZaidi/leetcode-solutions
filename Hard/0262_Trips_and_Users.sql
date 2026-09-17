-- Problem: Trips and Users
-- Problem ID: 262
-- Difficulty: Hard
-- Language: MySQL
-- Runtime: 929 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-09-17

SELECT
    t.request_at AS Day,
    ROUND(
        AVG(
            CASE
                WHEN t.status = 'completed' THEN 0
                ELSE 1
            END
        ),
        2
    ) AS `Cancellation Rate`
FROM Trips t
JOIN Users c
    ON t.client_id = c.users_id
JOIN Users d
    ON t.driver_id = d.users_id
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
  AND c.banned = 'No'
  AND d.banned = 'No'
GROUP BY t.request_at;