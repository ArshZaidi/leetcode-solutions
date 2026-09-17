# Problem: Word Pattern
# Problem ID: 290
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # Check char → word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False

            # Check word → char
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True