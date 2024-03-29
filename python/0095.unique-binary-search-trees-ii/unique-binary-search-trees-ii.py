# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive solution
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)


    def helper(self, s, e):
        res = []
        if s > e:
            res.append(None)
            return res
        for i in range(s, e+1):
            left_res = self.helper(s, i-1)
            right_res = self.helper(i+1, e)
            for ls in left_res:
                for rs in right_res:
                    newRoot = TreeNode(i)
                    newRoot.left = ls
                    newRoot.right = rs
                    res.append(newRoot)

        return res