# Problem: Calculate Money in Leetcode Bank
# Problem ID: 1817
# Difficulty: Easy
# Language: Python
# Runtime: 7 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def totalMoney(self, n):
        total = 0

        for i in range(n):
            week = i // 7
            day = i % 7
            total += week + day + 1

        return total