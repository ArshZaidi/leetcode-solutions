# Problem: Merge Strings Alternately
# Problem ID: 1894
# Difficulty: Easy
# Language: Python
# Runtime: 20 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = []
        i = j = 0

        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            ans.append(word1[i])
            i += 1

        while j < len(word2):
            ans.append(word2[j])
            j += 1

        return "".join(ans)