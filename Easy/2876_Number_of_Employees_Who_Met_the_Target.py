# Problem: Number of Employees Who Met the Target
# Problem ID: 2876
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0

        for hour in hours:
            if hour >= target:
                count += 1

        return count