# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        k = 0
        j = head
        while i.next is not None:
            i = i.next
            k+=1
            if k%2 != 0:
                j = j.next
        return j
            
            