# Problem: Valid Elements in an Array
# Problem ID: 4290
# Difficulty: Easy
# Language: Python3
# Runtime: 6 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []

        left_max = nums[0]
        right_max = [0] * n
        right_max[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(nums[i], right_max[i + 1])

        for i in range(n):
            if i == 0 or i == n - 1:
                ans.append(nums[i])
            elif nums[i] > left_max or nums[i] > right_max[i + 1]:
                ans.append(nums[i])

            left_max = max(left_max, nums[i])

        return ans