# Problem: Climbing Stairs
# Problem ID: 70
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for _ in range(n - 1):
            one, two = one + two, one

        return one