# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = ""
        a2 = ""
        while l1.next != None:
            a1 += str(l1.val)
            l1 = l1.next
        while l2.next != None:
            a2 += str(l2.val)
            l2 = l2.next
        a1 += str(l1.val)
        a2 += str(l2.val)
        a1 = a1[::-1]
        a2 = a2[::-1]
        a3 = int(a1) + int(a2)
        a3 = list(str(a3))  
        x = ListNode()
        for i in range(0,len(a3)):
            if i == len(a3)-1:
                x.val = a3[i]
            else:
                temp = ListNode()
                temp.val = a3[i]
                temp.next = x.next
                x.next = temp
        return x

            
            
            