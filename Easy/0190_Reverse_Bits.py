# Problem: Reverse Bits
# Problem ID: 190
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result