# Problem: Running Sum of 1d Array
# Problem ID: 1603
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums