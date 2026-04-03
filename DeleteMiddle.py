# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # n = 1
        if not head.next:
            return None

        # n = 2
        if not head.next.next:
            head.next = None
            return head
        
        # n = 3
        if not head.next.next.next:
            head.next = head.next.next
            return head
        
        # n = 4 or 5
        if not head.next.next.next.next or not head.next.next.next.next.next:
            head.next.next = head.next.next.next
            return head

        cnt = 0

        slow, fast = head, head.next
        while fast and fast.next and fast.next.next:
            cnt += 1
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return head
