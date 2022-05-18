# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sizeof(self, headA: ListNode):
        count = 0
        current = headA
        while current is not None:
            current = current.next 
            count += 1 
        return count 
            
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = self.sizeof(headA)
        b = self.sizeof(headB)
        if a == b: 
            while headA:
                if headA is headB:
                    return headA
                headA = headA.next 
                headB = headB.next
                
        if b > a:
            d = b - a 
            for i in range(d):
                headB = headB.next
        else:
            d = a - b 
            for i in range(d):
                headA = headA.next 
        
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next 
            headB = headB.next 
        return None
                
            