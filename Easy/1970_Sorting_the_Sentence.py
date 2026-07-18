# Problem: Sorting the Sentence
# Problem ID: 1970
# Difficulty: Easy
# Language: Python
# Runtime: 14 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        ans = [""] * len(words)

        for word in words:
            index = int(word[-1]) - 1
            ans[index] = word[:-1]

        return " ".join(ans)