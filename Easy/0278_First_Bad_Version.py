# Problem: First Bad Version
# Problem ID: 278
# Difficulty: Easy
# Language: Python3
# Runtime: 43 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left