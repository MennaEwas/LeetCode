# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = [root]
        if not root: return False
        while q:
            node = q.pop(0) #return the first element 
            if node.left == None and node.right == None: #leaves 
                if node.val == targetSum:
                    return True
            
            
            if node.left:
                node.left.val = node.val + node.left.val
                q.append(node.left)
            if node.right:
                node.right.val = node.val + node.right.val
                q.append(node.right)
                
        return False
            
            
                
            