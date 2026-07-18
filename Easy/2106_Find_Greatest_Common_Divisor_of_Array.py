# Problem: Find Greatest Common Divisor of Array
# Problem ID: 2106
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.6 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def findGCD(self, nums):
        num1 = min(nums)
        num2 = max(nums)
        answer = []
        for i in range(1,min(nums)+1):
            if num1 % i == 0 and num2 % i == 0:
                answer.append(i)
        return max(answer)
        