# Problem: String Matching in an Array
# Problem ID: 1524
# Difficulty: Easy
# Language: Python
# Runtime: 6 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def stringMatching(self, words):
        ans = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    ans.append(words[i])
                    break

        return ans