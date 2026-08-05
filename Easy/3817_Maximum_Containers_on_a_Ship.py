# Problem: Maximum Containers on a Ship
# Problem ID: 3817
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)