class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        curr = root
        def recursion(curr):
            if curr is None:
                return 0
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            return self.invertTree(curr.left),  self.invertTree(curr.right)
        recursion(curr)
        return root