# Last updated: 17/07/2026, 15:02:27
class Solution:
    def generateTrees(self, n):

        if n == 0:
            return []

        def build(start, end):
            trees = []

            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):

                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)
        