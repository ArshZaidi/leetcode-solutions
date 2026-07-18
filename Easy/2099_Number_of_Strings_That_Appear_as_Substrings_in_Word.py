# Problem: Number of Strings That Appear as Substrings in Word
# Problem ID: 2099
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(pattern in word for pattern in patterns)