# Problem: Furthest Point From Origin
# Problem ID: 3019
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')

        return abs(left - right) + blank