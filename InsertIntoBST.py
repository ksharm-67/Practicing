# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def find(root, val):
            if not root:
                return TreeNode(val)

            elif val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    find(root.left, val)

            else:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    find(root.right, val)
                
        find(root, val)
        return root

        # for example tree -> find(4, 5)
        # find(7, 5)
        
