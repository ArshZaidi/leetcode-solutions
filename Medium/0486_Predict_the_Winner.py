# Problem: Predict the Winner
# Problem ID: 486
# Difficulty: Medium
# Language: Python3
# Runtime: 1 ms
# Memory: 20 MB
# Synced From: LeetCode
# Date: 2026-08-01

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        from functools import lru_cache
        from typing import List
        @lru_cache(None)
        def solve(i, j):
            if i == j:
                return nums[i]

            left = nums[i] - solve(i + 1, j)
            right = nums[j] - solve(i, j - 1)

            return max(left, right)

        return solve(0, len(nums) - 1) >= 0