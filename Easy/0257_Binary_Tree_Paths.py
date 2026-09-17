# Problem: Binary Tree Paths
# Problem ID: 257
# Difficulty: Easy
# Language: Python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Synced From: LeetCode
# Date: 2026-09-17

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            # Leaf node
            if not node.left and not node.right:
                result.append(path)
                return

            path += "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return result