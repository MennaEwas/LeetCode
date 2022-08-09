# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            # connect all nodes of this level
            for i in range(0, levelSize):
                currentNode = queue.popleft()
                if i == levelSize - 1:
                    result.append(currentNode.val)
                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return result