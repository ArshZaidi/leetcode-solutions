# Problem: Make Three Strings Equal
# Problem ID: 3207
# Difficulty: Easy
# Language: Python3
# Runtime: 4 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0

        while i < min(len(s1), len(s2), len(s3)):
            if s1[i] == s2[i] == s3[i]:
                i += 1
            else:
                break

        if i == 0:
            return -1

        return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)