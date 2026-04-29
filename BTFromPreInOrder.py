# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        def constructTree(preorder, inorder):
            if not preorder:
                return None

            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])

            root.left = constructTree(preorder[1:1 + i], inorder[:i])
            root.right = constructTree(preorder[1 + i:], inorder[i + 1:])

            return root

        return constructTree(preorder, inorder)
