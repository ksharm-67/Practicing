# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val

        temp, stk = head, []
        while temp:
            stk.append(temp.val)
            temp = temp.next

        stk = stk[len(stk) // 2:]
        temp = head
        res = 0

        while stk:
            twin = stk.pop()
            res = max(res, twin + temp.val)
            temp = temp.next

        return res
