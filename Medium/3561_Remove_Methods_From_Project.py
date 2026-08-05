# Problem: Remove Methods From Project
# Problem ID: 3561
# Difficulty: Medium
# Language: Python3
# Runtime: 247 ms
# Memory: 107.1 MB
# Synced From: LeetCode
# Date: 2026-08-05

from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)

        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        ans = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans