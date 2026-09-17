# Problem: Summary Ranges
# Problem ID: 228
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")

            i += 1

        return result