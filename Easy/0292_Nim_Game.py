# Problem: Nim Game
# Problem ID: 292
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0