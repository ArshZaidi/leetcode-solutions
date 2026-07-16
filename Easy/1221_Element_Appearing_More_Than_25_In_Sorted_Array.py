# Problem: Element Appearing More Than 25% In Sorted Array
# Problem ID: 1221
# Difficulty: Easy
# Language: Python
# Runtime: 3024 ms
# Memory: 13.7 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution(object):
    def findSpecialInteger(self, arr):
        check = len(arr) / 4
        for i in range(len(arr)):
            count = 0
            for j in range(i, len(arr)):
                if arr[j] == arr[i]:
                    count += 1 
            if count > check:
                return arr[i]
                break
        