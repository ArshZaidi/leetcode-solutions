# Problem: Maximum Product of Word Lengths
# Problem ID: 318
# Difficulty: Medium
# Language: Python3
# Runtime: 253 ms
# Memory: 22.4 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []

        for word in words:
            mask = 0

            for char in word:
                mask |= 1 << (ord(char) - ord('a'))

            masks.append((mask, len(word)))

        answer = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i][0] & masks[j][0] == 0:
                    answer = max(
                        answer,
                        masks[i][1] * masks[j][1]
                    )

        return answer