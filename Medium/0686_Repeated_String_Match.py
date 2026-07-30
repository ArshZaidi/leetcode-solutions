# Problem: Repeated String Match
# Problem ID: 686
# Difficulty: Medium
# Language: Python3
# Runtime: 3 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        original = a
        count = 1

        while True:
            if b in a:
                return count
            elif len(a) > len(b) + len(original):
                return -1
            else:
                a += original
                count += 1