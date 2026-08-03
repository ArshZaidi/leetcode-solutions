# Problem: Stone Game III
# Problem ID: 1522
# Difficulty: Hard
# Language: Python3
# Runtime: 680 ms
# Memory: 23.9 MB
# Synced From: LeetCode
# Date: 2026-08-03

class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr = 0
            dp[i] = float("-inf")

            for j in range(3):
                if i + j < n:
                    curr += stoneValue[i + j]
                    dp[i] = max(dp[i], curr - dp[i + j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"