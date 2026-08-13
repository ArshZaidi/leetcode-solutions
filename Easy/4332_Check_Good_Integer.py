# Problem: Check Good Integer
# Problem ID: 4332
# Difficulty: Easy
# Language: Python3
# Runtime: 2 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits = [int(x) for x in str(n)]

        digit_sum = sum(digits)
        square_sum = sum(x * x for x in digits)

        return square_sum - digit_sum >= 50