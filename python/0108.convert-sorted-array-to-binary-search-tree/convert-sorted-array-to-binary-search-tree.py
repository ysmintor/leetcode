# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            midPos = len(nums) // 2
            root = TreeNode(nums[midPos])
            root.left = self.sortedArrayToBST(nums[0:midPos])
            root.right = self.sortedArrayToBST(nums[midPos+1:])
            return root