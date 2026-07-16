# Problem: Make The String Great
# Problem ID: 1666
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def makeGood(self, s):
        stack = []

        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)