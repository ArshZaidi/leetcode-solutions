# Problem: Number of Changing Keys
# Problem ID: 3312
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += 1

        return ans