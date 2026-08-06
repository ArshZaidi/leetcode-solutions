# Problem: Smallest Divisible Digit Product I
# Problem ID: 3626
# Difficulty: Easy
# Language: Python3
# Runtime: 1 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-06

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            check = str(n)
            multiply = 1

            for num in check:
                multiply *= int(num)

            if multiply % t == 0:
                return n

            n += 1
            