# Problem: Score of a String
# Problem ID: 3379
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score