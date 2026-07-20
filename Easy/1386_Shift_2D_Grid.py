# Problem: Shift 2D Grid
# Problem ID: 1386
# Difficulty: Easy
# Language: Python
# Runtime: 1 ms
# Memory: 12.6 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        k %= (m * n)
        arr = arr[-k:] + arr[:-k]

        ans = []
        for i in range(0, len(arr), n):
            ans.append(arr[i:i+n])

        return ans