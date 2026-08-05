# Problem: Valid Word
# Problem ID: 3396
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant