# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Problem ID: 1566
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()

        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i + 1

        return -1