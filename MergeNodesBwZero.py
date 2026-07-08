# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        last_zero, seen = None, False
        so_far = 0

        while temp:
            so_far += temp.val

            if not seen and temp.val == 0:
                last_zero = temp
                seen = True
            
            elif seen and temp.val == 0:
                last_zero.next = temp
                temp.val = so_far

                so_far = 0
                last_zero = last_zero.next
            
            temp = temp.next

        return head.next
