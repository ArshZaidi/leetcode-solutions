# Problem: Check if Two Chessboard Squares Have the Same Color
# Problem ID: 3553
# Difficulty: Easy
# Language: Python3
# Runtime: 45 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1 = (ord(coordinate1[0]) - ord('a') + int(coordinate1[1])) % 2
        c2 = (ord(coordinate2[0]) - ord('a') + int(coordinate2[1])) % 2

        return c1 == c2