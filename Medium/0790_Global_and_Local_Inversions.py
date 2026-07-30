# Problem: Global and Local Inversions
# Problem ID: 790
# Difficulty: Medium
# Language: Python3
# Runtime: 23 ms
# Memory: 30.4 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_suffix = nums[-1]

        for i in range(len(nums) - 3, -1, -1):
            min_suffix = min(min_suffix, nums[i + 2])

            if nums[i] > min_suffix:
                return False

        return True