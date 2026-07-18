# Problem: Maximum Product Difference Between Two Pairs
# Problem ID: 2042
# Difficulty: Easy
# Language: Python
# Runtime: 141 ms
# Memory: 13.4 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]