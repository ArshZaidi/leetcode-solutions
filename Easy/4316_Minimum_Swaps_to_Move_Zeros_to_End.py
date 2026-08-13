# Problem: Minimum Swaps to Move Zeros to End
# Problem ID: 4316
# Difficulty: Easy
# Language: Python3
# Runtime: 2 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:

        zeros = nums.count(0)
        swaps = 0

        for i in range(len(nums) - zeros):
            if nums[i] == 0:
                swaps += 1

        return swaps