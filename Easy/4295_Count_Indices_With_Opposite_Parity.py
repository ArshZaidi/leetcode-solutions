# Problem: Count Indices With Opposite Parity
# Problem ID: 4295
# Difficulty: Easy
# Language: Python3
# Runtime: 43 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            count = 0

            for j in range(i + 1, n):
                if nums[i] % 2 != nums[j] % 2:
                    count += 1

            answer.append(count)

        return answer