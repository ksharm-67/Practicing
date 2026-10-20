class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        if not head.next:
            return head

        prev, slow, fast = None, head, head.next
        chg = False

        while fast:
            while fast and slow.val == fast.val:
                fast = fast.next
                chg = True

            if chg:
                if slow != head:
                    prev.next = fast
                else:
                    head = fast
                chg = False
            else:
                prev = slow

            slow = fast
            if fast:
                fast = fast.next

        return head
