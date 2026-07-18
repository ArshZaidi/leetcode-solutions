# Problem: Minimum Operations to Make the Array Increasing
# Problem ID: 1938
# Difficulty: Easy
# Language: Python
# Runtime: 88 ms
# Memory: 13 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def minOperations(self, nums):
        operations = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                need = nums[i] + 1 - nums[i + 1]
                nums[i + 1] += need
                operations += need

        return operations