# Problem: Pascal's Triangle II
# Problem ID: 119
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

            row.append(1)

        return row