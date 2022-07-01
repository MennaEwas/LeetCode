# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        if head is None:
            return None
        while head.next is not None:
            if head in d.keys():
                return head 
            d[head] = head.next
            head = head.next
        return None