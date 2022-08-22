# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_path = []
        def recursive_sum(current, targetSum, currentPath, all_path):
            if not current : return 
            currentPath.append(current.val)
            if current.val == targetSum and not current.right and not current.left:
                all_path.append(list(currentPath))
            else:
                recursive_sum(current.left, targetSum - current.val, currentPath, all_path)
                recursive_sum(current.right, targetSum - current.val, currentPath, all_path)

            del currentPath[-1]
            
        recursive_sum(root, targetSum, [], all_path)
        return all_path
    
    