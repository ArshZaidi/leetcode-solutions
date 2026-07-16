# Problem: Check If All 1's Are at Least Length K Places Away
# Problem ID: 1548
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 16.5 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def kLengthApart(self, nums, k):
        prev = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i

        return True