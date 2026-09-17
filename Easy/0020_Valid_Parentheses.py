# Problem: Valid Parentheses
# Problem ID: 20
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0