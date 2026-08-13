# Problem: First Matching Character From Both Ends
# Problem ID: 4264
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] == s[len(s) - i -1]:
                return i
                break
        else:
            return -1