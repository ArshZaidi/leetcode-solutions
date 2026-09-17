# Problem: Range Sum Query - Immutable
# Problem ID: 303
# Difficulty: Easy
# Language: Python3
# Runtime: 11 ms
# Memory: 22.9 MB
# Synced From: LeetCode
# Date: 2026-09-17

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]