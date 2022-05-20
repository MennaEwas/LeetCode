# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head) #creating a dummy node at the begin
        prev = dummy 
        current = head 
        while current:
            nxt = current.next 
            if current.val == val:
                prev.next = nxt 
            else:
                prev = current
            current = nxt
        
        return dummy.next 
        
        