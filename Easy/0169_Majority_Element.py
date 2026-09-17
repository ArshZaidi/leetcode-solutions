# Problem: Majority Element
# Problem ID: 169
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 21.5 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate