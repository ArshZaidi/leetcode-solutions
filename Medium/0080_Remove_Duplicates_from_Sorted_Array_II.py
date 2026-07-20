# Problem: Remove Duplicates from Sorted Array II
# Problem ID: 80
# Difficulty: Medium
# Language: Python
# Runtime: 95 ms
# Memory: 15.2 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def removeDuplicates(self, nums):
        count = dict()
        i = 0
        while i < len(nums):
            if nums[i] not in count:
                count[nums[i]] = 1
                i += 1
            elif count[nums[i]] >= 2:
                nums.pop(i)
            else:
                count[nums[i]] += 1
                i += 1
        return len(nums)
