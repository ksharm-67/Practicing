# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            curr_level = []
            node = list(q)
            q.clear()

            for n in node:
                curr_level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            res.append(curr_level)
        
        return res[::-1]
