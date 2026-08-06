# Problem: Validate Stack Sequences
# Problem ID: 983
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-06

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for num in pushed:
            stack.append(num)

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return len(stack) == 0