"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        mp = {None: None}
        newList = Node(0)
        newTemp, temp = newList, head

        while temp:
            newTemp.val = temp.val
            mp[temp] = newTemp

            if temp.next: newTemp.next = Node(0)

            temp = temp.next
            newTemp = newTemp.next

        newTemp, temp = newList, head
        while temp:
            newTemp.random = mp[temp.random]

            temp = temp.next
            newTemp = newTemp.next

        return newList
