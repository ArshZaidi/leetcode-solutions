# Problem: Special Array I
# Problem ID: 3429
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False

        return True