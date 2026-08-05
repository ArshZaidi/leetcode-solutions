# Problem: Harshad Number
# Problem ID: 3371
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0

        for digit in str(x):
            digit_sum += int(digit)

        if x % digit_sum == 0:
            return digit_sum

        return -1