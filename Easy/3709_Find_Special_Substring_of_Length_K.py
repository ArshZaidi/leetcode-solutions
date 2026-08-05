# Problem: Find Special Substring of Length K
# Problem ID: 3709
# Difficulty: Easy
# Language: Python3
# Runtime: 7 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        for i in range(n - k + 1):
            if len(set(s[i:i + k])) != 1:
                continue

            if i > 0 and s[i - 1] == s[i]:
                continue

            if i + k < n and s[i + k] == s[i]:
                continue

            return True

        return False