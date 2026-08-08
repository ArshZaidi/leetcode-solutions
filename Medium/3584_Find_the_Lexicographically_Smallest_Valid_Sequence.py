# Problem: Find the Lexicographically Smallest Valid Sequence
# Problem ID: 3584
# Difficulty: Medium
# Language: Python3
# Runtime: 407 ms
# Memory: 46.8 MB
# Synced From: LeetCode
# Date: 2026-08-08

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not used:
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    used = True

        return ans if j == m else []