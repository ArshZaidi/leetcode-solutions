# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Problem ID: 3236
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-11

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        while total in nums:
            total += 1

        return total