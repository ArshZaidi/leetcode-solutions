# Problem: Remove Comments
# Problem ID: 722
# Difficulty: Medium
# Language: Python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Synced From: LeetCode
# Date: 2026-07-30

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        inBlock = False
        curr = []

        for line in source:
            i = 0

            while i < len(line):
                if inBlock:
                    if i + 1 < len(line) and line[i] == "*" and line[i + 1] == "/":
                        inBlock = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == "/" and line[i + 1] == "/":
                        break
                    elif i + 1 < len(line) and line[i] == "/" and line[i + 1] == "*":
                        inBlock = True
                        i += 2
                    else:
                        curr.append(line[i])
                        i += 1

            if not inBlock and curr:
                ans.append("".join(curr))
                curr = []

        return ans