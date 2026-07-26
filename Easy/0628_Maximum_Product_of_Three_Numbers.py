# Problem: Maximum Product of Three Numbers
# Problem ID: 628
# Difficulty: Easy
# Language: Python3
# Runtime: 17 ms
# Memory: 20.3 MB
# Synced From: LeetCode
# Date: 2026-07-26

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1],
            nums[0] * nums[1] * nums[2]
        )
