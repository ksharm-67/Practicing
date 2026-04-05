# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        
        self.res = 0
        def height(self, root):
            if not root: return -1

            left_height = height(self, root.left)
            right_height = height(self, root.right)

            # diameter
            self.res = max(self.res, 2 + left_height + right_height)

            return 1 + max(left_height, right_height)

        height(self, root)
        return self.res
