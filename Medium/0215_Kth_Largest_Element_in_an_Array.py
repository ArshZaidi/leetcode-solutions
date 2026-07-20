# Problem: Kth Largest Element in an Array
# Problem ID: 215
# Difficulty: Medium
# Language: Python
# Runtime: 80 ms
# Memory: 20.2 MB
# Synced From: LeetCode
# Date: 2026-07-20

class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]