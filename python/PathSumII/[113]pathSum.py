"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, s, path, res):
            if root:
                path.append(root.val)
                s -= root.val
                left = dfs(root.left, s, path, res)
                right = dfs(root.right, s, path, res)
                if not left and not right and s == 0:
                    res.append(path + [])
                path.pop()
                return True

        res = []
        dfs(root, sum, [], res)
        return res