# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total, curr, i = 0, head, k
        while curr:
            if i == 1:
                rem = curr
            curr = curr.next
            i -= 1
            total += 1
        
        curr, i = head, 1
        while curr:
            if i == total - k + 1:
                curr.val, rem.val = rem.val, curr.val
                return head
            i += 1
            curr = curr.next

