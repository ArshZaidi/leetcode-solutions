# Problem: Count Odd Numbers in an Interval Range
# Problem ID: 1630
# Difficulty: Easy
# Language: Python
# Runtime: 16 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def countOdds(self, low, high):
        return (high + 1) // 2 - low // 2