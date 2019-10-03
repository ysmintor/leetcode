# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 上下限递归检测
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            return helper(node.left, lower, val) and helper(node.right, val, upper)

        return helper(root)

    # 中序非递归
    def isValidBST2(self, root: TreeNode) -> bool:
        stack, preValue = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if preValue >= root.val:
                return False
            preValue = root.val
            root = root.right

        return True