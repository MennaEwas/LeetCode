# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        level = deque()
        level.append(root)
        while any(level):
            depth+=1
            len_list = len(level)
            for _ in range(len_list):
                node = level.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
        