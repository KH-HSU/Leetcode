# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.recursive(root, output)
        return output
    def recursive(self, root: TreeNode, output: List[int]) -> List[int]:
        if root is None:
            return
        self.recursive(root.left, output)
        output.append(root.val)
        self.recursive(root.right, output)