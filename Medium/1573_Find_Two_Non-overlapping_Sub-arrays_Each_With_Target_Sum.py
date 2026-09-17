# Problem: Find Two Non-overlapping Sub-arrays Each With Target Sum
# Problem ID: 1573
# Difficulty: Medium
# Language: Python3
# Runtime: 96 ms
# Memory: 31 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        best = [INF] * n

        left = 0
        curr_sum = 0
        answer = INF
        min_len = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if answer == INF else answer