# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def avg(a):
            return sum(a) / len(a)
        result = []
        level = [root]
        av = []
        while any(level):
            result.append([node.val for node in level])
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level   
        for l in result:
            av.append(avg(l))
        return av
        