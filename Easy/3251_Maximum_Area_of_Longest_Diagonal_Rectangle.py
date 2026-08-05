# Problem: Maximum Area of Longest Diagonal Rectangle
# Problem ID: 3251
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0

        for l, w in dimensions:
            diag = l * l + w * w
            area = l * w

            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area, area)

        return max_area