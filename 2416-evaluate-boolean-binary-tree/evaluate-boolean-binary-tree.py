class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root or root.val == 0:
            return False
        if root.val == 1:
            return True
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
        return False
