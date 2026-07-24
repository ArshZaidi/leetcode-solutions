# Problem: Number of Unique XOR Triplets II
# Problem ID: 3820
# Difficulty: Medium
# Language: Python3
# Runtime: 10202 ms
# Memory: 20 MB
# Synced From: LeetCode
# Date: 2026-07-24

class Solution:
    def uniqueXorTriplets(self, nums):
        dp0 = {0}
        dp1 = set()
        dp2 = set()
        dp3 = set()

        for v in nums:
            ndp1 = dp1.copy()
            ndp2 = dp2.copy()
            ndp3 = dp3.copy()

            # use current index once
            for x in dp2:
                ndp3.add(x ^ v)
            for x in dp1:
                ndp2.add(x ^ v)
            for x in dp0:
                ndp1.add(x ^ v)

            # use current index twice
            for x in dp1:
                ndp3.add(x)
            for x in dp0:
                ndp2.add(x)

            # use current index three times
            for x in dp0:
                ndp3.add(x ^ v)

            dp1, dp2, dp3 = ndp1, ndp2, ndp3

        return len(dp3)