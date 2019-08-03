"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


"""

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