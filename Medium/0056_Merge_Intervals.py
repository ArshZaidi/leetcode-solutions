# Problem: Merge Intervals
# Problem ID: 56
# Difficulty: Medium
# Language: Python
# Runtime: 7 ms
# Memory: 16.1 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            last = answer[-1]

            if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])
            else:
                answer.append(intervals[i])

        return answer