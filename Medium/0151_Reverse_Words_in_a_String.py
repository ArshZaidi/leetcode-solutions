# Problem: Reverse Words in a String
# Problem ID: 151
# Difficulty: Medium
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
        