# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums, temp, prev = set(nums), head, None

        while temp:
            if temp and temp.val in nums:
                if temp == head:
                    head = head.next
                else:
                    prev.next = temp.next

            else:
                prev = temp
            temp = temp.next   

        return head 
                

