# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def find_path_recursive(current, S, currentq):
            if not current: 
                return 0
            summ, count = 0, 0
            currentq.append(current.val)
            #for loop 
            for i in range(len(currentq)-1, -1, -1):
                summ += currentq[i]
                if summ == S:
                    count += 1  
            count += find_path_recursive(current.left, S, currentq)
            count += find_path_recursive(current.right, S,  currentq) 
            del currentq[-1]
            return count
        return find_path_recursive(root, targetSum, [])