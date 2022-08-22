# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_path = []
        def recursive_sum(current, currentPath, all_path):
            if not current : return 
            currentPath = currentPath + str(current.val)
            if not current.right and not current.left:
                all_path.append(currentPath)
            else:
                recursive_sum(current.left, currentPath + "->", all_path)
                recursive_sum(current.right, currentPath + "->", all_path)

            
            
        recursive_sum(root,"", all_path)
        return all_path