# Problem: Consecutive Characters
# Problem ID: 1542
# Difficulty: Easy
# Language: Python
# Runtime: 11 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def maxPower(self, s):
        ans = 1
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            if count > ans:
                ans = count

        return ans