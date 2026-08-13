# Problem: Number of Elapsed Seconds Between Two Times
# Problem ID: 4357
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1, m1, s1 = map(int, startTime.split(":"))
        h2, m2, s2 = map(int, endTime.split(":"))

        start = h1 * 3600 + m1 * 60 + s1
        end = h2 * 3600 + m2 * 60 + s2

        return end - start