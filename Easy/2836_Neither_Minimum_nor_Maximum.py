# Problem: Neither Minimum nor Maximum
# Problem ID: 2836
# Difficulty: Easy
# Language: Python3
# Runtime: 10 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return sorted(nums)[1] if len(nums) > 2 else -1