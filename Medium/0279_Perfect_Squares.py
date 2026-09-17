# Problem: Perfect Squares
# Problem ID: 279
# Difficulty: Medium
# Language: Python3
# Runtime: 1812 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]