# Problem: Longest Common Prefix
# Problem ID: 14
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix