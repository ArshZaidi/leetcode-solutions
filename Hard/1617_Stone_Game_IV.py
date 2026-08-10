# Problem: Stone Game IV
# Problem ID: 1617
# Difficulty: Hard
# Language: Python3
# Runtime: 587 ms
# Memory: 20.1 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break

                j += 1

        return dp[n]