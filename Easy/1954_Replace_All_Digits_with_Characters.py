# Problem: Replace All Digits with Characters
# Problem ID: 1954
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.2 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def replaceDigits(self, s):
        chars = list(s)

        for i in range(1, len(chars), 2):
            chars[i] = chr(ord(chars[i - 1]) + int(chars[i]))

        return "".join(chars)