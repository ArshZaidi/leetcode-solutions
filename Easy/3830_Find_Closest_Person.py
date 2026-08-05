# Problem: Find Closest Person
# Problem ID: 3830
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x - z)
        d2 = abs(y - z)

        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0