# Problem: Lexicographically Smallest Palindrome
# Problem ID: 2816
# Difficulty: Easy
# Language: Python3
# Runtime: 43 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if s[left] < s[right]:
                    s[right] = s[left]
                else:
                    s[left] = s[right]
            left += 1
            right -= 1

        return "".join(s)