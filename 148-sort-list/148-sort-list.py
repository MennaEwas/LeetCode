# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        s, f = head, head.next 
        while f and f.next:
            s = s.next 
            f = f.next.next
        return s
    
    def merge(self, list1, list2):
        d = ListNode() #new list
        tail = d #pointer of the new list 
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return d.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        #splitting into 2 heads
        l = head
        r = self.getMid(head)
        t = r.next 
        r.next = None
        r = t
        
        l = self.sortList(l)
        r = self.sortList(r)
        
        #collecting
        return self.merge(l, r)
    
    
            
        
        
        