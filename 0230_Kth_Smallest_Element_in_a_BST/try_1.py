# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def dfs(root: TreeNode, nums: List[int]) -> int:
            if root is None:
                return
            nums.append(root.val)
            return dfs(root.left, nums), dfs(root.right, nums)
        
        nums = []
        dfs(root, nums)
        nums.sort()
        return nums[k-1]