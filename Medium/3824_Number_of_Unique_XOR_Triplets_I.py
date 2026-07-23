# Problem: Number of Unique XOR Triplets I
# Problem ID: 3824
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 32.1 MB
# Synced From: LeetCode
# Date: 2026-07-23

class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n < 3:
            return n

        return 1 << n.bit_length()