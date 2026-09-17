# Problem: Sqrt(x)
# Problem ID: 69
# Difficulty: Easy
# Language: Python3
# Runtime: 4 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        return right