# Problem: Container With Most Water
# Problem ID: 11
# Difficulty: Medium
# Language: Python
# Runtime: 123 ms
# Memory: 20.6 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        best = 0

        while i < j:
            area = min(height[i], height[j])*(j-i)
            best = max(area, best)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return best