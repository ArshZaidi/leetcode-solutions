# Problem: Final Prices With a Special Discount in a Shop
# Problem ID: 1570
# Difficulty: Easy
# Language: Python
# Runtime: 13 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def finalPrices(self, prices):
        ans = prices[:]

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans[i] = prices[i] - prices[j]
                    break

        return ans