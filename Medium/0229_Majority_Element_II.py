# Problem: Majority Element II
# Problem ID: 229
# Difficulty: Medium
# Language: Python3
# Runtime: 1 ms
# Memory: 22.3 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        result = []

        for candidate in [candidate1, candidate2]:
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result