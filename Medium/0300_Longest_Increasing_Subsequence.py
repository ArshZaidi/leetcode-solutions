# Problem: Longest Increasing Subsequence
# Problem ID: 300
# Difficulty: Medium
# Language: Python3
# Runtime: 1281 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)