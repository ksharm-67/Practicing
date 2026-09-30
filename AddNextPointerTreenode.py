class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                temp = q.popleft()
                if i < size - 1:
                    temp.next = q[0]
                if temp.left:
                   q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

        return root
                
