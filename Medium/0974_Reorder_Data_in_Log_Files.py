# Problem: Reorder Data in Log Files
# Problem ID: 974
# Difficulty: Medium
# Language: Python3
# Runtime: 3 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-08-06

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            identifier, rest = log.split(" ", 1)

            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((rest, identifier, log))

        letters.sort()

        answer = []

        for _, _, log in letters:
            answer.append(log)

        answer.extend(digits)

        return answer