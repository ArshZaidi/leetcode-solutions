# Problem: Type of Triangle
# Problem ID: 3321
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"

        return "scalene"