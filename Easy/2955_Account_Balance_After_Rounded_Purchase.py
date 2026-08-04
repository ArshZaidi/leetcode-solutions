# Problem: Account Balance After Rounded Purchase
# Problem ID: 2955
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-08-04

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = ((purchaseAmount + 5) // 10) * 10
        return 100 - roundedAmount