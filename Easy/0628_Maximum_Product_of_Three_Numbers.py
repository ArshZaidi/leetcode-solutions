# Problem: Maximum Product of Three Numbers
# Problem ID: 628
# Difficulty: Easy
# Language: Python
# Runtime: 34 ms
# Memory: 13.1 MB
# Synced From: LeetCode
# Date: 2026-07-26

class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])