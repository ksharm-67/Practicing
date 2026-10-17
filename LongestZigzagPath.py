# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        # last: true then left, otherwise right
        def dfs(root, last, longest):
            nonlocal res
            if not root:
                return
            res = max(res, longest)
            
            if last:
                if root.left:
                    dfs(root.left, False, longest + 1)
                if root.right:
                    dfs(root.right, True, 1)
            else:
                if root.right:
                    dfs(root.right, True, longest + 1)
                if root.left:
                    dfs(root.left, False, 1)

        res = 0
        dfs(root, False, 0)
        dfs(root, True, 0)

        return res
