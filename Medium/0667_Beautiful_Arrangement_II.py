# Problem: Beautiful Arrangement II
# Problem ID: 667
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 20.1 MB
# Synced From: LeetCode
# Date: 2026-07-26

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []

        left, right = 1, k + 1

        while left <= right:
            ans.append(left)
            left += 1
            if left <= right:
                ans.append(right)
                right -= 1

        ans.extend(range(k + 2, n + 1))

        return ans