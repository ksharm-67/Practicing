# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        if not head.next:
            return True
        
        if not head.next.next and head.val != head.next.val:
            return False

        seen = []
        slow, fast = head, head

        while fast and fast.next:
            seen.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast: slow = slow.next

        i = len(seen) - 1
        while slow:
            if slow.val != seen[i]:
                print(f"{slow.val} != {seen[i]}")
                return False
            i -= 1
            slow = slow.next

        return True
