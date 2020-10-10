# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        answer = []
        while (1):
            self.goAlongLeftBranch(root, stack)
            if len(stack) == 0:
                break
            root = stack.pop()
            answer.append(root.val)
            root = root.right
        return answer
    def goAlongLeftBranch(self, root: TreeNode, stack: List[int]) -> List[list]:
        while root:
            stack.append(root)
            root = root.left