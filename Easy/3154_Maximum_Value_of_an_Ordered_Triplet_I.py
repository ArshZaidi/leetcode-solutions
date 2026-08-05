# Problem: Maximum Value of an Ordered Triplet I
# Problem ID: 3154
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        ans = 0

        for j in range(1, n - 1):
            ans = max(ans, (left_max[j - 1] - nums[j]) * right_max[j + 1])

        return ans