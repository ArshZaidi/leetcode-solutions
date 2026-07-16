# Problem: Decrypt String from Alphabet to Integer Mapping
# Problem ID: 1434
# Difficulty: Easy
# Language: Python
# Runtime: 4 ms
# Memory: 12.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def freqAlphabets(self, s):
        ans = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                num = int(s[i:i + 2])
                ans += chr(ord('a') + num - 1)
                i += 3
            else:
                num = int(s[i])
                ans += chr(ord('a') + num - 1)
                i += 1

        return ans