# Problem: Split Strings by Separator
# Problem ID: 2881
# Difficulty: Easy
# Language: Python3
# Runtime: 4 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []

        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part != "":
                    answer.append(part)

        return answer