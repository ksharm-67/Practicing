# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1, -1]

        res = [float('inf'), -float('inf')]
        lastCritical, firstCritical, i = 0, 0, 0

        prev, curr, = head, head.next
        while curr.next:
            i += 1
            if (prev.val > curr.val and curr.next.val > curr.val) or (prev.val < curr.val and curr.next.val < curr.val):
                if lastCritical == 0:
                    firstCritical = i
                    lastCritical = i
                else:
                    res[0] = min(res[0], i - lastCritical)
                    res[1] = max(res[1], i - firstCritical)
                    lastCritical = i
            
            prev = prev.next
            curr = curr.next
                
        return res if res != [float('inf'), -float('inf')] else [-1, -1]
