# Problem: Longest Substring of One Repeating Character
# Problem ID: 2319
# Difficulty: Hard
# Language: Python3
# Runtime: 3448 ms
# Memory: 211.7 MB
# Synced From: LeetCode
# Date: 2026-08-13

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        s = list(s)

        # [first_char, last_char, prefix, suffix, best, length]
        tree = [[None, None, 0, 0, 0, 0] for _ in range(4 * n)]

        def merge(node):
            left = tree[node * 2]
            right = tree[node * 2 + 1]

            first = left[0]
            last = right[1]
            length = left[5] + right[5]

            prefix = left[2]
            suffix = right[3]
            best = max(left[4], right[4])

            if left[1] == right[0]:
                best = max(best, left[3] + right[2])

                if left[2] == left[5]:
                    prefix = left[5] + right[2]

                if right[3] == right[5]:
                    suffix = right[5] + left[3]

            tree[node] = [first, last, prefix, suffix, best, length]

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans