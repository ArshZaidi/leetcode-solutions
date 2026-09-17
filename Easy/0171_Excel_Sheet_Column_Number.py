# Problem: Excel Sheet Column Number
# Problem ID: 171
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result