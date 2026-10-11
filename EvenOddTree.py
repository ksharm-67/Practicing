# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        lvl = 0
        q = deque([root])

        while q:
            curr = list(q)
            q.clear()
            for i in range(len(curr)):
                if lvl % 2 == 0:
                    if curr[i].val % 2 == 0 or (i > 0 and curr[i].val <= curr[i - 1].val):
                        return False
                else:
                    if curr[i].val % 2 != 0 or (i > 0 and curr[i].val >= curr[i - 1].val):
                        return False
                
                if curr[i].left:
                    q.append(curr[i].left)
                if curr[i].right:
                    q.append(curr[i].right)
            
            lvl += 1

        return True

