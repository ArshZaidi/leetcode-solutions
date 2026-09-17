# Problem: Single Number
# Problem ID: 136
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 21.1 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result