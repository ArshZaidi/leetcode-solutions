# Problem: Divisible and Non-divisible Sums Difference
# Problem ID: 3172
# Difficulty: Easy
# Language: Python3
# Runtime: 2 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i

        return num1 - num2