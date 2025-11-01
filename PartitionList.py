# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head
        
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        
        less = []
        more = []
        for i in range(len(l)):
            if l[i] < x:
                less.append(l[i])
            else:
                more.append(l[i])

        less.extend(more)

        res = ListNode(less[0])
        del less[0]
        temp = res
        while less:
            popped = less.pop(0)
            nextNode = ListNode(popped)
            temp.next = nextNode
            temp = temp.next
        
        return res
