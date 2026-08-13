# Problem: Limit Occurrences in Sorted Array
# Problem ID: 4312
# Difficulty: Easy
# Language: Python3
# Runtime: 3 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        answer = []

        for num in nums:
            if not answer or answer[-1] != num:
                answer.append(num)
            elif answer.count(num) < k:
                answer.append(num)

        return answer