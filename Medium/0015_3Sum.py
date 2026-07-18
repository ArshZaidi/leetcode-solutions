# Problem: 3Sum
# Problem ID: 15
# Difficulty: Medium
# Language: Python
# Runtime: 799 ms
# Memory: 19 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return answer