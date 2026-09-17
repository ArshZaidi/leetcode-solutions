# Problem: Best Time to Buy and Sell Stock
# Problem ID: 121
# Difficulty: Easy
# Language: Python3
# Runtime: 46 ms
# Memory: 28.7 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit