# Problem: Maximum Gap
# Problem ID: 164
# Difficulty: Medium
# Language: Python
# Runtime: 250 ms
# Memory: 23.9 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        difference = list()
        for i in range(1,len(nums)):
            difference.append(abs(nums[i] - nums[i-1]))
        return max(difference) if len(difference) >= 1 else 0
        