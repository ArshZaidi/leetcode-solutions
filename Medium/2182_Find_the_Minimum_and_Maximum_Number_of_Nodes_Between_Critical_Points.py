# Problem: Find the Minimum and Maximum Number of Nodes Between Critical Points
# Problem ID: 2182
# Difficulty: Medium
# Language: Python3
# Runtime: 68 ms
# Memory: 63.5 MB
# Synced From: LeetCode
# Date: 2026-08-31

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)
                    max_dist = index - first

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [min_dist, max_dist]