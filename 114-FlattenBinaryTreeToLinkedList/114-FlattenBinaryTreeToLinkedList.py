# Last updated: 17/07/2026, 15:02:04
class Solution:
    def flatten(self, root):
        current = root

        while current:
            if current.left:
                prev = current.left

                while prev.right:
                    prev = prev.right

                prev.right = current.right
                current.right = current.left
                current.left = None

            current = current.right
        