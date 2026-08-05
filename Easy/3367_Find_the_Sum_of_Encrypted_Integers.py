# Problem: Find the Sum of Encrypted Integers
# Problem ID: 3367
# Difficulty: Easy
# Language: Python3
# Runtime: 60 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            s = str(num)
            mx = max(s)
            ans += int(mx * len(s))

        return ans