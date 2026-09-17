# Problem: Single Number III
# Problem ID: 260
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 20.8 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0

        # XOR everything
        for num in nums:
            xor_all ^= num

        # Rightmost bit where the two unique numbers differ
        diff = xor_all & -xor_all

        a = 0
        b = 0

        # Separate into two groups and XOR
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]