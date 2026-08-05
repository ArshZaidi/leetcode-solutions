# Problem: Find Minimum Operations to Make All Elements Divisible by Three
# Problem ID: 3476
# Difficulty: Easy
# Language: Python3
# Runtime: 1 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            rem = num % 3
            ans += min(rem, 3 - rem)

        return ans