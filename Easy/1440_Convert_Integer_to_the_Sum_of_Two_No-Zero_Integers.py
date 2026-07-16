# Problem: Convert Integer to the Sum of Two No-Zero Integers
# Problem ID: 1440
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.7 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def getNoZeroIntegers(self, n):
        def noZero(x):
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in range(1, n):
            b = n - a
            if noZero(a) and noZero(b):
                return [a, b]