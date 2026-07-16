# Problem: Check If Two String Arrays are Equivalent
# Problem ID: 1781
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)