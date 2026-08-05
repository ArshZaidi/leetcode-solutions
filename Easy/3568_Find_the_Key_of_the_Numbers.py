# Problem: Find the Key of the Numbers
# Problem ID: 3568
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        key = ""

        for i in range(4):
            key += str(min(int(s1[i]), int(s2[i]), int(s3[i])))

        return int(key)