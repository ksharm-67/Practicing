# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        flip = 0

        q = deque([root])
        res, curr = [], []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if flip % 2 == 0:
                res.append(curr)
            else:
                res.append(curr[::-1])
            flip += 1
            curr = []
    
        return res
