# Problem: Minimum Distance to the Target Element
# Problem ID: 1975
# Difficulty: Easy
# Language: Python
# Runtime: 4 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i, x in enumerate(nums) if x == target)