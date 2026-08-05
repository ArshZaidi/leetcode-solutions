# Problem: Check if a String Is an Acronym of Words
# Problem ID: 2977
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = ""
        for word in words:
            x += word[0]
        return True if x == s else False