"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])
        while q:
            for i in range(len(q)):
                if i == 0:
                    curr = q.popleft()
                else:
                    curr = q.popleft()
                    prev.next = curr
                
                prev = curr    
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            
            curr.next = None

        return root
