# Problem: Rearrange Spaces Between Words
# Problem ID: 1714
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def reorderSpaces(self, text):
        spaces = text.count(" ")
        words = text.split()

        if len(words) == 1:
            return words[0] + " " * spaces

        gap = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)

        return (" " * gap).join(words) + " " * extra