# Problem: Check If String Is a Prefix of Array
# Problem ID: 2093
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.2 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def isPrefixString(self, s, words):
        curr = ""

        for word in words:
            curr += word
            if not s.startswith(curr):
                return False
            if curr == s:
                return True

        return False