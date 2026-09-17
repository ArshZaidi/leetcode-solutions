# Problem: House Robber
# Problem ID: 198
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            current = max(prev1, prev2 + money)

            prev2 = prev1
            prev1 = current

        return prev1