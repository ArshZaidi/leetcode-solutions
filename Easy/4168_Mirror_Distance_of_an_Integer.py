# Problem: Mirror Distance of an Integer
# Problem ID: 4168
# Difficulty: Easy
# Language: Python3
# Runtime: 1 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = str(n)
        y = x[::-1]

        return abs(int(x) - int(y))