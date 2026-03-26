# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0 and not l1.next: return l2
        if l2.val == 0 and not l2.next: return l1

        res = ListNode(0)
        temp, carry, curr = res, 0, 0
        
        while l1 or l2 or carry:
            sum_nodes = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_nodes // 10
            curr = sum_nodes % 10
            
            temp.val = curr
    
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if l1 or l2 or carry:
                temp.next = ListNode(0)  
                temp = temp.next          

        return res
            
        
