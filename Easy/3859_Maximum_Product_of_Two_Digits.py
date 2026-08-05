# Problem: Maximum Product of Two Digits
# Problem ID: 3859
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n:
            digits.append(n % 10)
            n //= 10

        digits.sort(reverse=True)

        return digits[0] * digits[1]