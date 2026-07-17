# Problem: Determine Color of a Chessboard Square
# Problem ID: 1920
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def squareIsWhite(self, coordinates):
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])

        return (col + row) % 2 == 1