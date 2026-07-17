# Last updated: 17/07/2026, 15:02:05
class Solution:
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))