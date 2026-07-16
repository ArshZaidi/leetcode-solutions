# Problem: Mean of Array After Removing Some Elements
# Problem ID: 1210
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 12.6 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def trimMean(self, arr):
        arr.sort()
        k = len(arr) // 20
        return float(sum(arr[k:len(arr) - k])) / (len(arr) - 2 * k)