# Last updated: 17/07/2026, 15:02:07
class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # if left is missing, go right side only
        if not root.left:
            return 1 + self.minDepth(root.right)

        # if right is missing, go left side only
        if not root.right:
            return 1 + self.minDepth(root.left)

        # both sides exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))