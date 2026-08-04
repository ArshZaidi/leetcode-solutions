# Problem: Number of Senior Citizens
# Problem ID: 2727
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for uid in details:
            if int(uid[11:13]) > 60:
                count += 1
        return count

