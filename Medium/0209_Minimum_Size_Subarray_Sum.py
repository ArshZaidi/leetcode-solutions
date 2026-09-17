# Problem: Minimum Size Subarray Sum
# Problem ID: 209
# Difficulty: Medium
# Language: Python3
# Runtime: 17 ms
# Memory: 30.6 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length