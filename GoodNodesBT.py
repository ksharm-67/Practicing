# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, msf):
            if not root:
                return 0

            cnt = 0
            if root.val >= msf:
                cnt = 1
            
            msf = max(msf, root.val)
            return dfs(root.left, msf) + dfs(root.right, msf) + cnt

        return dfs(root, root.val)
