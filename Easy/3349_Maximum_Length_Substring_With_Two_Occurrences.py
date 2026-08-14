# Problem: Maximum Length Substring With Two Occurrences
# Problem ID: 3349
# Difficulty: Easy
# Language: Python3
# Runtime: 4 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-14

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans