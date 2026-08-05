# Problem: Button with Longest Push Time
# Problem ID: 3632
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.6 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans = events[0][0]
        longest = events[0][1]

        for i in range(1, len(events)):
            idx = events[i][0]
            time = events[i][1] - events[i - 1][1]

            if time > longest:
                longest = time
                ans = idx
            elif time == longest:
                ans = min(ans, idx)

        return ans