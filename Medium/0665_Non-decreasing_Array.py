# Problem: Non-decreasing Array
# Problem ID: 665
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 20.7 MB
# Synced From: LeetCode
# Date: 2026-07-26

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if changed:
                    return False

                changed = True

                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True