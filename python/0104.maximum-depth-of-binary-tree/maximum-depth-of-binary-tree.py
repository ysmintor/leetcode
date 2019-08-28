# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

class Solution:
    """
    BFS version
    the level work like a queue
    """
    def maxDepth(self, root: TreeNode) -> int:
        depth, level = 0, [root]
        while root and level:
            depth+=1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return depth