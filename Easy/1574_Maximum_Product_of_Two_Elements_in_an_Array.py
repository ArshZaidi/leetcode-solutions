# Problem: Maximum Product of Two Elements in an Array
# Problem ID: 1574
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def maxProduct(self, nums):
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)