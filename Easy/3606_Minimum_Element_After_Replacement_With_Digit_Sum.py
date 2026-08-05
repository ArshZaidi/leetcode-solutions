# Problem: Minimum Element After Replacement With Digit Sum
# Problem ID: 3606
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10
            ans = min(ans, digit_sum)

        return ans