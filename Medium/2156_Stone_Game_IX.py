# Problem: Stone Game IX
# Problem ID: 2156
# Difficulty: Medium
# Language: Python3
# Runtime: 64 ms
# Memory: 30.9 MB
# Synced From: LeetCode
# Date: 2026-08-16

class Solution:
    def stoneGameIX(self, stones):
        c0 = c1 = c2 = 0

        for x in stones:
            if x % 3 == 0:
                c0 += 1
            elif x % 3 == 1:
                c1 += 1
            else:
                c2 += 1

        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        else:
            return abs(c1 - c2) > 2