# Problem: Remove K Digits
# Problem ID: 402
# Difficulty: Medium
# Language: Python3
# Runtime: 19 ms
# Memory: 20.2 MB
# Synced From: LeetCode
# Date: 2026-07-22

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        ans = "".join(stack).lstrip('0')

        return ans if ans else "0"