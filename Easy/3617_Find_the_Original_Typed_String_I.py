# Problem: Find the Original Typed String I
# Problem ID: 3617
# Difficulty: Easy
# Language: Python3
# Runtime: 49 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                ans += count - 1
                count = 1

        ans += count - 1

        return ans