# Problem: Check if Array Is Sorted and Rotated
# Problem ID: 1878
# Difficulty: Easy
# Language: Python
# Runtime: 4 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def check(self, nums):
        n = len(nums)
        drops = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1

        return drops <= 1