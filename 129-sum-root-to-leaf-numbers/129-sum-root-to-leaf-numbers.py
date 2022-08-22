# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, current, pathSum):
        if not current: return 0 
        pathSum = 10 * pathSum + current.val
        if not (current.left or current.right):
            return pathSum
        return self.recursive(current.left, pathSum) + self.recursive(current.right, pathSum)
        
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root, 0)
    
    
        