# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Iterative solution
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        if  not root:
            return ans

        level = [(root, str(root.val))]
        while level:
            node, path = level.pop()
            if not node.right and not node.left:
                ans.append(path)
            if node.left:
                level.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                level.append((node.right, path+'->'+str(node.right.val)))
        return ans

    # Recursive solution
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return self.getPath(root)

    def getPath(self, root: TreeNode) -> List[str]:
        # root is leaf
        if not root.left and not root.right:
            return ['%s' % root.val]

        paths = []
        if root.left:
            paths.extend(self.getPath(root.left))
        if  root.right:
            paths.extend(self.getPath(root.right))

        return ['%s->%s' % (root.val, path) for path in paths]