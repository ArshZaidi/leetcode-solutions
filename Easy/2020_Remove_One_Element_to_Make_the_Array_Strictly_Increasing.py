# Problem: Remove One Element to Make the Array Strictly Increasing
# Problem ID: 2020
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.6 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def canBeIncreasing(self, nums):
        removed = False

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                if removed:
                    return False

                removed = True

                if i > 0 and nums[i - 1] >= nums[i + 1]:
                    nums[i + 1] = nums[i]
                    
        return True