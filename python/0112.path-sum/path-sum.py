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