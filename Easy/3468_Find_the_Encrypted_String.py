# Problem: Find the Encrypted String
# Problem ID: 3468
# Difficulty: Easy
# Language: Python3
# Runtime: 36 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n

        ans = ""

        for i in range(n):
            ans += s[(i + k) % n]

        return ans