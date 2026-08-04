# Problem: Buy Two Chocolates
# Problem ID: 2756
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money - (prices[0] + prices[1]) >= 0:
            return money - (prices[0] + prices[1])
        else:
            return money