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
            return

        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            count = 0 
            # connect all nodes of this level
            for _ in range(levelSize):
                currentNode = queue.popleft()
                count += 1 
                if count == levelSize:
                    result.append(currentNode.val)

                # insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return result