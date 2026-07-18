# Problem: Find First Palindromic String in the Array
# Problem ID: 2231
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""