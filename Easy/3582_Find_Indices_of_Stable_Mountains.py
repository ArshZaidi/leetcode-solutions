# Problem: Find Indices of Stable Mountains
# Problem ID: 3582
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-05

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = list()
        for i in range(1,len(height)):
            if height[i-1] > threshold:
                answer.append(i)
        return answer