# Problem: Find the Duplicate Number
# Problem ID: 287
# Difficulty: Medium
# Language: Python3
# Runtime: 32 ms
# Memory: 33.6 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find a meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow