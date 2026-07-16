# Problem: Find Numbers with Even Number of Digits
# Problem ID: 1421
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count