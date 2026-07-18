# Problem: Insert Interval
# Problem ID: 57
# Difficulty: Medium
# Language: Python
# Runtime: 4 ms
# Memory: 14.2 MB
# Synced From: LeetCode
# Date: 2026-07-18

class Solution(object):
    def insert(self, intervals, newInterval):
        answer = []

        for interval in intervals:

            if interval[1] < newInterval[0]:
                answer.append(interval)

            elif interval[0] > newInterval[1]:
                answer.append(newInterval)
                newInterval = interval

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        answer.append(newInterval)

        return answer