# Problem: Three Consecutive Odds
# Problem ID: 1293
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def threeConsecutiveOdds(self, arr):
        count = 0

        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False