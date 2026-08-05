# Problem: Minimum Right Shifts to Sort the Array
# Problem ID: 3045
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        idx = -1

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                idx = i

        if count == 0:
            return 0
        if count > 1:
            return -1

        return n - idx - 1