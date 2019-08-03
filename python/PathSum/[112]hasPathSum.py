"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1 use recursive method
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum-root.val) or \
               self.hasPathSum(root.right, sum-root.val)

# solution 2 use queue to add sum
from collections import deque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root:
            queue = deque([(root, root.val)])
            while queue:
                p, s = queue.popleft()
                left, right = p.left, p.right
                if left:
                    queue.append((left, left.val + s))
                if right:
                    queue.append((right, right.val + s))
                if not left and not right and s == sum:
                    return True
            return False
        return False