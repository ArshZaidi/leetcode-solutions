# Problem: Minimum Operations to Make Array Sum Divisible by K
# Problem ID: 3846
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k