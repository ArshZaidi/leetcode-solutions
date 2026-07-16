# Problem: Replace Elements with Greatest Element on Right Side
# Problem ID: 1231
# Difficulty: Easy
# Language: Python
# Runtime: 22 ms
# Memory: 13.8 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def replaceElements(self, arr):
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            if temp > max_right:
                max_right = temp

        return arr