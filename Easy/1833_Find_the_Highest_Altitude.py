# Problem: Find the Highest Altitude
# Problem ID: 1833
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.4 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])

        return max(altitudes)