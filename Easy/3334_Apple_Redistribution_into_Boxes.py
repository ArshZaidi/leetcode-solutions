# Problem: Apple Redistribution into Boxes
# Problem ID: 3334
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        boxes = 0
        curr = 0

        for c in capacity:
            curr += c
            boxes += 1
            if curr >= total:
                return boxes

        return boxes