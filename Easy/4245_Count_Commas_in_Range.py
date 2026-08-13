# Problem: Count Commas in Range
# Problem ID: 4245
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if n < 1000:
            return 0
        elif n >= 1000 and n < 10000:
            return n - 999
        elif n >= 10000 and n < 100000:
            return 9000 + (n - 9999)
        else:
            return 99001