# Problem: Daily Temperatures
# Problem ID: 739
# Difficulty: Medium
# Language: Python3
# Runtime: 90 ms
# Memory: 28.1 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer