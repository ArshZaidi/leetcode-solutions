# Problem: Valid Palindrome
# Problem ID: 125
# Difficulty: Easy
# Language: Python3
# Runtime: 12 ms
# Memory: 19.7 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True