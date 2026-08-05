# Problem: Maximum Difference Between Adjacent Elements in a Circular Array
# Problem ID: 3747
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = []

        for i in range(len(nums) - 1):
            answer.append(abs(nums[i + 1] - nums[i]))

        answer.append(abs(nums[-1] - nums[0]))

        return max(answer)