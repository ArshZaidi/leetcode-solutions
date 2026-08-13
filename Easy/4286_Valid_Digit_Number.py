# Problem: Valid Digit Number
# Problem ID: 4286
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        return s[0] != str(x) and str(x) in s