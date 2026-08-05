# Problem: Substring Matching Pattern
# Problem ID: 3684
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split("*")

        for i in range(len(s) + 1):
            if s.startswith(left, i):
                j = i + len(left)
                while j <= len(s):
                    if s.startswith(right, j):
                        return True
                    j += 1

        return False