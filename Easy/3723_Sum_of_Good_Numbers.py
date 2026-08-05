# Problem: Sum of Good Numbers
# Problem ID: 3723
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            good = True

            if i - k >= 0 and nums[i] <= nums[i - k]:
                good = False

            if i + k < n and nums[i] <= nums[i + k]:
                good = False

            if good:
                ans += nums[i]

        return ans