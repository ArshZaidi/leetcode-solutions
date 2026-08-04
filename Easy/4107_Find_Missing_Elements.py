# Problem: Find Missing Elements
# Problem ID: 4107
# Difficulty: Easy
# Language: Python3
# Runtime: 7 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(min(nums), max(nums) + 1):
            if i not in nums:
                answer.append(i)

        return answer