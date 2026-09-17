# Problem: Bitwise AND of Numbers Range
# Problem ID: 201
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift