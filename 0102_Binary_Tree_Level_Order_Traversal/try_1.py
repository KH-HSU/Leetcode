# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return 
        q = []
        ans = []
        q.append(root)
        while len(q) > 0:
            temp = []
            for i in range(len(q)):
                curr = q.pop(0)
                temp.append(curr.val)
                
                if curr.left is not None:
                    q.append(curr.left)

                if curr.right is not None:
                    q.append(curr.right)
            ans.append(temp)
        return ans