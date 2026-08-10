# Problem: Equal Score Substrings
# Problem ID: 4052
# Difficulty: Easy
# Language: Python3
# Runtime: 7 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def scoreBalance(self, s: str) -> bool:
        left = 0
        right = sum(ord(c) - ord('a') + 1 for c in s)

        for i in range(len(s) - 1):
            left += ord(s[i]) - ord('a') + 1
            right -= ord(s[i]) - ord('a') + 1

            if left == right:
                return True

        return False