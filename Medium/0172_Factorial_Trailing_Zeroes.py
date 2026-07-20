# Problem: Factorial Trailing Zeroes
# Problem ID: 172
# Difficulty: Medium
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        while n:
            n //= 5
            count += n
        return count


        