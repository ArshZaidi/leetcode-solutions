# Problem: Maximum Ascending Subarray Sum
# Problem ID: 1927
# Difficulty: Easy
# Language: Python
# Runtime: 1 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def maxAscendingSum(self, nums):
        curr = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                curr = nums[i]

            ans = max(ans, curr)

        return ans