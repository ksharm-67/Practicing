# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)
            return max(left_height, right_height) + 1
        
        max_depth = height(root)
        def dfs(root, curr):
            nonlocal res
            if not root:
                return 0
            if curr == max_depth:
                res += root.val
                return 

            dfs(root.left, curr + 1)
            dfs(root.right, curr + 1)
        
        res = 0
        dfs(root, 1)
        return res
