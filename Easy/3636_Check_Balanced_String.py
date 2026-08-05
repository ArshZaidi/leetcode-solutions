# Problem: Check Balanced String
# Problem ID: 3636
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i in range(len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])
        return True if even == odd else False