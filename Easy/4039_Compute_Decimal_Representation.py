# Problem: Compute Decimal Representation
# Problem ID: 4039
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        place = 1

        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * place)
            n //= 10
            place *= 10

        return result[::-1]