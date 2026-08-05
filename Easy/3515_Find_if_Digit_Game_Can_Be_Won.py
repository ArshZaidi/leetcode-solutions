# Problem: Find if Digit Game Can Be Won
# Problem ID: 3515
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0

        for num in nums:
            if num < 10:
                single += num
            else:
                double += num

        return single != double