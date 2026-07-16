# Problem: Can Make Arithmetic Progression From Sequence
# Problem ID: 1626
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()

        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True