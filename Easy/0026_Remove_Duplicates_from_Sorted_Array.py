# Problem: Remove Duplicates from Sorted Array
# Problem ID: 26
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 20.4 MB
# Synced From: LeetCode
# Date: 2026-08-11

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k