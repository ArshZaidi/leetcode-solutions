# Problem: Stone Game II
# Problem ID: 1240
# Difficulty: Medium
# Language: Python3
# Runtime: 183 ms
# Memory: 27.2 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, m):
            if i >= n:
                return 0

            if (i, m) in dp:
                return dp[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                # Stones the current player can get
                # = remaining stones - opponent's maximum
                opponent = solve(i + x, max(m, x))
                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, m)] = best
            return best

        return solve(0, 1)