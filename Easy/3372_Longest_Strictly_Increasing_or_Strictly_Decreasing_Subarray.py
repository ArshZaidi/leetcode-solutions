# Problem: Longest Strictly Increasing or Strictly Decreasing Subarray
# Problem ID: 3372
# Difficulty: Easy
# Language: Python3
# Runtime: 4 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            ans = max(ans, inc, dec)

        return ans