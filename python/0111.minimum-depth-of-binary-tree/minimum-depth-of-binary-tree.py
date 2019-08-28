# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution1 BFS, reach the first leaf then return
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            b = len(queue)
            for i in range(b):
                rt = queue.popleft()
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
                if not rt.left and not rt.right:
                    return level
        return -1

# solution2 DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)