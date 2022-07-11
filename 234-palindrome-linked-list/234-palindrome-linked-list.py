# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def size(self, head):
        count = 0
        current_node = head
        while(current_node != None):
            count += 1
            current_node = current_node.next
        return count
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = self.size(head)
        md = n // 2
        c = 0
        stack = []
        current = head
        if n == 1:
            return True
        if n == 2:
            if current.val != current.next.val:
                return False
            else:
                return True
            
        while c < md and current:
            stack.append(current.val)
            current = current.next 
            c += 1
        if current and n % 2 != 0: #odd
            current = current.next
        
        while current:
            p = stack.pop()
            if p != current.val:
                return False
            current = current.next
        return True
            
        
             
        