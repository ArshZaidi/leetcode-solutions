# Problem: Latest Time by Replacing Hidden Digits
# Problem ID: 1858
# Difficulty: Easy
# Language: Python
# Runtime: 0 ms
# Memory: 12.6 MB
# Synced From: LeetCode
# Date: 2026-07-17

class Solution(object):
    def maximumTime(self, time):
        chars = list(time)
        for i in range(len(chars)):
            if i == 0 and chars[i] == '?':
                if chars[i + 1] == '?':
                    chars[i] = '2'
                elif int(chars[i + 1]) <= 3:
                    chars[i] = '2'
                else:
                    chars[i] = '1'
            elif i == 1 and chars[i] == '?':
                chars[i] = '9' if chars[i-1] == '1' or chars[i-1] == '0' else '3'
            elif i == 3 and chars[i] == '?':
                chars[i] = '5'
            elif i == 4 and chars[i] == '?':
                chars[i] = '9'
            else:
                continue
        return "".join(chars)
        