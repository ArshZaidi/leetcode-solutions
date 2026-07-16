# Problem: Average Salary Excluding the Minimum and Maximum Salary
# Problem ID: 1584
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def average(self, salary):
        salary.sort()
        return sum(salary[1:-1]) * 1.0 / (len(salary) - 2)