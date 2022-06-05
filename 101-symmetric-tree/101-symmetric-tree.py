# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return is_mirror(a.left, b.right) and is_mirror(a.right, b.left)
        return not root or is_mirror(root.right, root.left)