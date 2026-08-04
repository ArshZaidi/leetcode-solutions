# Problem: Remove Trailing Zeros From a String
# Problem ID: 2819
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == "0":
            num = num[:-1]
        return num