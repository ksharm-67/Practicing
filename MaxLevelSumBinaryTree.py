# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        maxSum, q, maxLvl = -float('inf'), deque([root]), 1

        currLvl = 1
        while q:
            node, curr = list(q), 0
            q.clear()
            
            for n in node:
                curr += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            if curr > maxSum:
                maxSum, maxLvl = curr, currLvl
            currLvl += 1
        
        return maxLvl
