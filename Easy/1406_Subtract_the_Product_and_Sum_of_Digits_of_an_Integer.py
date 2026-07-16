# Problem: Subtract the Product and Sum of Digits of an Integer
# Problem ID: 1406
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        count = 0
        for i in str(n):
            product *= int(i)
            count += int(i)
        return product - count
