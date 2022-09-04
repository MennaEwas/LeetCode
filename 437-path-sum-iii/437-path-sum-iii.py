# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0 
        def helper(node, cur):
            if not node:
                return 
            helper(node.right, cur + node.val)
            helper(node.left, cur + node.val)
            if cur + node.val == targetSum: self.total += 1
        def dfs(node):
            if not node: return
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.total
        
            