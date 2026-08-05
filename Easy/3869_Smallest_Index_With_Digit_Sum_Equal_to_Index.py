# Problem: Smallest Index With Digit Sum Equal to Index
# Problem ID: 3869
# Difficulty: Easy
# Language: Python3
# Runtime: 2 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            num = nums[i]

            if num == 0:
                digit_sum = 0
            else:
                while num:
                    digit_sum += num % 10
                    num //= 10

            if digit_sum == i:
                return i

        return -1