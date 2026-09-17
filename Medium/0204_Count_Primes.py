# Problem: Count Primes
# Problem ID: 204
# Difficulty: Medium
# Language: Python3
# Runtime: 9467 ms
# Memory: 86.2 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2

        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False

            p += 1

        return sum(is_prime)