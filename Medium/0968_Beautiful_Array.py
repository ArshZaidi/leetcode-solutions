# Problem: Beautiful Array
# Problem ID: 968
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.1 MB
# Synced From: LeetCode
# Date: 2026-08-06

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]

        while len(result) < n:
            temp = []

            for num in result:
                if 2 * num - 1 <= n:
                    temp.append(2 * num - 1)

            for num in result:
                if 2 * num <= n:
                    temp.append(2 * num)

            result = temp

        return result