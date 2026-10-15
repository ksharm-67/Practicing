# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        heap, q = [], deque([root])
        heapq.heapify_max(heap)

        while q:
            curr, s = list(q), 0
            q.clear()
            for node in curr:
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            heapq.heappush_max(heap, s)
        
        while heap:
            curr = heapq.heappop_max(heap)
            k -= 1
            if k == 0:
                return curr
        return -1
