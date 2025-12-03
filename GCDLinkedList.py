class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head

        while temp.next:
            curr = temp
            x = curr.next
            
            node = ListNode(math.gcd(curr.val, x.val))
            node.next = x
            curr.next = node

            temp = x

        return head
