# Problem: Trim Trailing Vowels
# Problem ID: 4229
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = "aeiou"

        while s and s[-1] in vowels:
            s = s[:-1]

        return s