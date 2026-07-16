# Problem: Generate a String With Characters That Have Odd Counts
# Problem ID: 1490
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def generateTheString(self, n):
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n - 1) + "b"