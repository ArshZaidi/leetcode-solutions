# Problem: Minimum Moves to Equal Array Elements III
# Problem ID: 4116
# Difficulty: Easy
# Language: Python3
# Runtime: 11 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-10

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer += (max(nums) - i)
        return answer
