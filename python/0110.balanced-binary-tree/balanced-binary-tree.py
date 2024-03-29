# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root: TreeNode):
            if not root:
                return 0
            left = check(root.left)
            if left == -1:
                return -1
            right = check(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        return check(root) != -1