# Problem: Count Items Matching a Rule
# Problem ID: 1899
# Difficulty: Easy
# Language: Python
# Runtime: 3 ms
# Memory: 16.6 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]

        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1

        return count