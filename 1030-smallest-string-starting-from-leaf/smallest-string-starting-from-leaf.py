# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = '{'

        def dfs(node, path):
            nonlocal smallest
            if node:
                path.append(chr(ord('a') + node.val))
                if node.left is None and node.right is None:
                    current_string = ''.join(reversed(path))
                    smallest = min(smallest, current_string)
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()

        dfs(root, [])
        return smallest
