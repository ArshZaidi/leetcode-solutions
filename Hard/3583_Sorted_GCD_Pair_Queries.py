# Problem: Sorted GCD Pair Queries
# Problem ID: 3583
# Difficulty: Hard
# Language: Python
# Runtime: 1056 ms
# Memory: 33.3 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        for g in range(1, mx + 1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]
            exact[g] = cnt * (cnt - 1) // 2

        for g in range(mx, 0, -1):
            for multiple in range(g * 2, mx + 1, g):
                exact[g] -= exact[multiple]

        pref = [0] * (mx + 1)
        for g in range(1, mx + 1):
            pref[g] = pref[g - 1] + exact[g]

        ans = []
        for q in queries:
            target = q + 1
            lo, hi = 1, mx
            while lo < hi:
                mid = (lo + hi) // 2
                if pref[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)

        return ans