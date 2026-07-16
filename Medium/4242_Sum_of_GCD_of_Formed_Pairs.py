# Problem: Sum of GCD of Formed Pairs
# Problem ID: 4242
# Difficulty: Medium
# Language: Python
# Runtime: 707 ms
# Memory: 22.4 MB
# Synced From: LeetCode
# Date: 2026-07-16

class Solution:
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefixGcd = []
        mx = 0

        for num in nums:
            if num > mx:
                mx = num
            prefixGcd.append(gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        left, right = 0, len(prefixGcd) - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans