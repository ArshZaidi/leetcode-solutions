# Problem: Monotone Increasing Digits
# Problem ID: 738
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        marker = len(digits)

        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i

        for i in range(marker, len(digits)):
            digits[i] = '9'

        return int("".join(digits))