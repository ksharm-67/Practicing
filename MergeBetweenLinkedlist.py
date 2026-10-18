# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp, prev, curr = list1, None, 0

        while temp:
            if curr == a:
                rem = prev
                break
            prev = temp
            temp = temp.next
            curr += 1

        while temp:
            if curr == b:
                cont = temp
                break
            temp = temp.next
            curr += 1

        rem.next = list2
        
        temp2 = list2
        while temp2.next:
            temp2 = temp2.next

        temp2.next = cont.next
        return list1
