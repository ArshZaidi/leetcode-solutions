# Problem: Sequential Digits
# Problem ID: 1212
# Difficulty: Medium
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans