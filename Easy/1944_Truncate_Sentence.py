# Problem: Truncate Sentence
# Problem ID: 1944
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def truncateSentence(self, s, k):
        count = 0

        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                if count == k:
                    return s[:i]

        return s