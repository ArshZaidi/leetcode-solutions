# Problem: Minimum Capacity Box
# Problem ID: 4247
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minimum = float('inf')
        index = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < minimum:
                minimum = capacity[i]
                index = i

        return index