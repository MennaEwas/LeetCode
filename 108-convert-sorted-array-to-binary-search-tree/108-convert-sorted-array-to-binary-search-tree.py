# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l < 0 or r >= len(nums) or l > r or l >= len(nums):
                return None
            md = (l + r) // 2
            first = TreeNode(val = nums[md])
            first.left = dfs(l, md - 1)
            first.right = dfs(md + 1, r)
            return first
        return dfs(0, len(nums) - 1)
        
            
            
        
        
        
        