# Problem: Length of Longest Subarray With at Most K Frequency
# Problem ID: 3225
# Difficulty: Medium
# Language: Python3
# Runtime: 243 ms
# Memory: 35.3 MB
# Synced From: LeetCode
# Date: 2026-08-12

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans