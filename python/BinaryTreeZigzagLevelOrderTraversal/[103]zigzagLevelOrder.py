"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        odd = True # indicate the order to lookup at each level
        while root and level:
            cur_nodes = [node.val for node in level]
            if not odd:
                cur_nodes.reverse()
            odd = not odd

            ans.append(cur_nodes)
            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return ans
