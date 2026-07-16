# Problem: Thousand Separator
# Problem ID: 1660
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def thousandSeparator(self, n):
        s = str(n)
        ans = ""

        count = 0
        for i in range(len(s) - 1, -1, -1):
            ans = s[i] + ans
            count += 1
            if count % 3 == 0 and i != 0:
                ans = "." + ans

        return ans