# Problem: Minimum Operations to Exceed Threshold Value I
# Problem ID: 3331
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0

        for num in nums:
            if num < k:
                count += 1

        return count