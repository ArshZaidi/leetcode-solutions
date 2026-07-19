# Problem: Smallest Subsequence of Distinct Characters
# Problem ID: 1159
# Difficulty: Medium
# Language: Python
# Runtime: 3 ms
# Memory: 12.3 MB
# Synced From: LeetCode
# Date: 2026-07-19

class Solution(object):
    def smallestSubsequence(self, s):
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            
            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            
            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)
    