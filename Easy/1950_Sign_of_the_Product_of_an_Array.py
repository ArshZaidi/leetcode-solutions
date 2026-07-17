# Problem: Sign of the Product of an Array
# Problem ID: 1950
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.7 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def arraySign(self, nums):
        sign = 1

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign *= -1

        return sign