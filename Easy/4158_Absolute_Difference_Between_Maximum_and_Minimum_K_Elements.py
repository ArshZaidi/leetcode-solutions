# Problem: Absolute Difference Between Maximum and Minimum K Elements
# Problem ID: 4158
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = sum(nums[:k])
        high = sum(nums[-k:])
        return high - low