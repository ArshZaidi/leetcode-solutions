# Problem: Compare Version Numbers
# Problem ID: 165
# Difficulty: Medium
# Language: Python
# Runtime: 0 ms
# Memory: 12.2 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        n = max(len(v1), len(v2))

        for i in range(n):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        return 0