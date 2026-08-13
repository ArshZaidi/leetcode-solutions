# Problem: Check Adjacent Digit Differences
# Problem ID: 4305
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(1, len(s)):
            if abs(int(s[i]) - int(s[i - 1])) > 2:
                return False

        return True