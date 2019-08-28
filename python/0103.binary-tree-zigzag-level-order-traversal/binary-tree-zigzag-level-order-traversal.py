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
