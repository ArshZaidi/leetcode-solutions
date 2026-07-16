# Problem: Decompress Run-Length Encoded List
# Problem ID: 1241
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def decompressRLElist(self, nums):
        ans = []

        for i in range(0, len(nums), 2):
            ans.extend([nums[i + 1]] * nums[i])

        return ans