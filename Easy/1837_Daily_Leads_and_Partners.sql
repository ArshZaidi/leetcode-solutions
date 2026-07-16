-- Problem: Daily Leads and Partners
-- Problem ID: 1837
-- Difficulty: Easy
-- Language: MySQL
-- Runtime: 696 ms
-- Memory: 0B
-- Synced From: LeetCode
-- Date: 2026-07-16

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;