# Problem: Maximum Swap
# Problem ID: 670
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-07-26

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        last = {}
        for i, d in enumerate(digits):
            last[d] = i

        for i in range(len(digits)):
            # Try bigger digits first
            for d in range(9, int(digits[i]), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num